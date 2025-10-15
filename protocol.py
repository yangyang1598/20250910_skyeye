import requests
import json
import threading
import time
from queue import Queue
# ------------------------------
# 설정 상수
# ------------------------------
TOKEN = "Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537"
DEVICE_NAME = "MD-2023-03-L"

MISSION_DEVICE_LOG_URL = "http://skysys.iptime.org:8000/mission_device_log/?name="
EVENT_URL = "http://skysys.iptime.org:8000/messages/"
SSE_EVENTS_URL_PREFIX = "http://skysys.iptime.org:8000/events/"
SSE_EVENTS_URL = f"{SSE_EVENTS_URL_PREFIX}{DEVICE_NAME}-GCS"


class Protocol:
    def __init__(self) -> None:
        # SSE 상태/자원
        self.sse_thread = None
        self.sse_session = None
        self.sse_response = None
        self.sse_stop_event = threading.Event()
        self.is_run_sse = False
        self.queue = Queue()
        # SSE URL/핸들러 설정
        self.sse_events_url_prefix = "http://skysys.iptime.org:8000/events/"
        self.sse_default_url = f"{self.sse_events_url_prefix}{DEVICE_NAME}-GCS"
        self.sse_event_handler = None
    def get_mission_device_log(self):
        """서버에서 디바이스 로그 데이터 요청"""
        try:
            url = MISSION_DEVICE_LOG_URL + DEVICE_NAME
            headers = {
                'Content-Type': 'application/json',
                'charset': 'UTF-8',
                'Accept': '*/*',
                'Authorization': TOKEN,
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"⚠️ API 오류: {response.status_code}")
        except Exception as e:
            print(f"❌ API 요청 오류: {e}")
        return None
    def post_event_message(self, msg):
        """서버에 이벤트 메시지 전송"""
        try:
            url = EVENT_URL + DEVICE_NAME
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Authorization': TOKEN,
            }
            # Postman과 동일하게 폼 필드 'text'에 JSON 문자열을 담아 전송
            data = {'text': json.dumps(msg, ensure_ascii=False)}
            response = requests.post(url, headers=headers, data=data)

            # 상태 코드 확인
            if not response.ok:
                print(f"⚠️ 이벤트 메시지 전송 오류: {response.status_code} raw={response.text[:200]}")
                return None

            raw = response.text
            if not raw or not raw.strip():
                print("⚠️ 응답 본문이 비어있음(Empty body)")
                return None

            ctype = response.headers.get('Content-Type', '')
            if 'application/json' in ctype.lower():
                try:
                    return response.json()
                except ValueError as je:
                    print(f"❌ JSON 파싱 오류: {je} raw={raw[:200]}")
                    return None
            else:
                # 서버가 텍스트만 반환하는 경우
                return raw

        except requests.RequestException as re:
            print(f"❌ 네트워크 오류: {re}")
            return None
        except Exception as e:
            print(f"❌ 이벤트 메시지 전송 요청 오류: {e}")
            return None
    class SseEventArgs:
        def __init__(self, obj):
            self.obj = obj

    def set_sse_event_handler(self, handler):
        """SSE 이벤트 콜백 등록: handler(SseEventArgs)"""
        self.sse_event_handler = handler

    def open_sse_stream(self, url=None):
        """SSE 스트림 오픈 (Authorization: Token ...) 후 백그라운드 스레드 시작"""
        headers = {
            'Accept': 'text/event-stream, */*',
            'Authorization': TOKEN,
        }
        self.sse_session = requests.Session()
        target_url = url or self.sse_default_url
        self.sse_response = self.sse_session.get(target_url, headers=headers, stream=True)
        self.start_sse_event_thread(self.sse_response)
        return self.sse_response.raw
    def start_sse_event_thread(self, response):
        """읽기 스레드 시작"""
        self.sse_stop_event.clear()
        self.is_run_sse = True
        self.sse_thread = threading.Thread(
            target=self.read_stream_forever,
            args=(response,),
            daemon=True,
            name="Sse Event Thread"
        )
        self.sse_thread.start()
    def stop_sse_event_thread(self):
        """읽기 스레드 중지 및 연결 종료"""
        if self.sse_thread:
            if threading.current_thread() is not self.sse_thread:
                try:
                    if self.sse_response:
                        self.sse_response.close()
                except Exception:
                    pass
            self.sse_stop_event.set()
            if self.sse_session:
                try:
                    self.sse_session.close()
                except Exception:
                    pass
            self.sse_thread = None
            self.queue = Queue()
    def read_stream_forever(self, response):
        """SSE 응답 스트림을 계속 읽어 큐에 적재 및 출력/콜백 호출"""
        try:
            for line in response.iter_lines(decode_unicode=True):
                if self.sse_stop_event.is_set():
                    break
                if not line:
                    continue
                # SSE 주석 라인은 건너뜀
                if line.startswith(':'):
                    continue
                if line.startswith('data:'):
                    payload = line[5:].strip()
                    # 큐에 원문 적재
                    self.push(payload)
                    # JSON 파싱 시도
                    try:
                        obj = json.loads(payload)
                    except Exception:
                        obj = payload
                    # 핸들러가 있으면 전달, 없으면 기본 출력
                    if self.sse_event_handler:
                        try:
                            self.sse_event_handler(self.SseEventArgs(obj))
                        except Exception:
                            pass
                    else:
                        print(f"event:{obj}")
        except Exception:
            pass
        finally:
            self.queue = Queue()
            self.is_run_sse = False
    def request_event(self, name: str):
        """연결 재시도 루프: /events/{name}-GCS"""
        while not self.is_run_sse:
            try:
                url = f"{self.sse_events_url_prefix}{name}-GCS"
                self.open_sse_stream(url)
                self.is_run_sse = True
            except Exception:
                time.sleep(2.0)
    def push(self, text: str):
        """수신 텍스트를 큐에 적재"""
        try:
            self.queue.put(text)
        except Exception:
            pass