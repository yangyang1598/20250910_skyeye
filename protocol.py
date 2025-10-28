import requests
import json
import threading
import time
from queue import Queue
# ------------------------------
# 설정 상수
# ------------------------------
TOKEN = "Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537"
DEVICE_NAME = "MD-2020-00-L"
SITE_ID=""

SERVER_URL="http://skysys.iptime.org:8000"
MISSION_DEVICE_LIST_URL = f"{SERVER_URL}/site/"
MISSION_DEVICE_LOG_URL = f"{SERVER_URL}/mission_device_log/?name="
CAMERA_SERIAL_URL = f"{SERVER_URL}/mission_device/?name="
EVENT_URL = f"{SERVER_URL}/messages/"
SSE_EVENTS_URL_PREFIX = f"{SERVER_URL}/events/"
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
        self.sse_event_handler = None  # SSE 이벤트 콜백

    def get_mission_device_list(self):
        headers = {
            'Content-Type': 'application/json',
            'charset': 'UTF-8',
            'Accept': '*/*',
            'Authorization': TOKEN,
        }
        response = requests.get(MISSION_DEVICE_LIST_URL, headers=headers)
        if response.status_code == 200:
            data=response.json()
            # print(data)
            return data
        else:
            print(f"⚠️ API 오류: {response.status_code}")
    def get_mission_device_log(self):
        """서버에서 디바이스 로그 데이터 요청"""
        try:
            # 선택 취소/잘못된 선택 시 요청하지 않음
            if not DEVICE_NAME:
                return None

            url = MISSION_DEVICE_LOG_URL + DEVICE_NAME
            headers = {
                'Content-Type': 'application/json',
                'charset': 'UTF-8',
                'Accept': '*/*',
                'Authorization': TOKEN,
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data=response.json()
                return data
            else:
                print(f"⚠️ 임무장비 데이터 API 오류: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ 임무장비 데이터 API 요청 오류: {e}")
        return None
    def get_camera_serial_number(self):
        """서버에서 카메라 시리얼 번호 요청"""
        try:
            # 선택 취소/잘못된 선택 시 요청하지 않음
            if not DEVICE_NAME:
                return None

            url = CAMERA_SERIAL_URL + DEVICE_NAME
            headers = {
                'Content-Type': 'application/json',
                'charset': 'UTF-8',
                'Accept': '*/*',
                'Authorization': TOKEN,
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data=response.json()
                return data.get('camera_serial_number')
            else:
                print(f"⚠️ 카메라 시리얼 번호 API 오류: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌카메라 시리얼 번호 API 요청 오류: {e}")
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
                print(f"이벤트 메시지 전송 오류: {response.status_code} raw={response.text[:200]}")
                return None

            raw = response.text
            if not raw or not raw.strip():
                print("응답 본문이 비어있음(Empty body)")
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

    def set_sse_event_handler(self, handler):
        """SSE 이벤트 콜백 등록: handler(SseEventArgs)"""
        self.sse_event_handler = handler

    def open_sse_stream(self):
        """SSE 스트림 오픈 (Authorization: Token ...) 후 백그라운드 스레드 시작"""
        headers = {
            'Accept': 'text/event-stream, */*',
            'Authorization': TOKEN,
        }
        # DEVICE_NAME 최신값으로 URL을 매번 생성
        url = f"{SSE_EVENTS_URL_PREFIX}{DEVICE_NAME}-GCS"
        self.sse_session = requests.Session()
        self.sse_response = self.sse_session.get(url, headers=headers, stream=True)
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
        """SSE 응답 스트림을 계속 읽어 큐에 적재"""
        try:
            data_buf = []
            event_type = None
            event_id = None
            for line in response.iter_lines(decode_unicode=True):
                if self.sse_stop_event.is_set():
                    break

                if line is None:
                    continue

                # 이벤트 경계(빈 줄) 처리
                if line == '':
                    if data_buf:
                        data_text = "\n".join(data_buf)

                        # 문자열 분기 제거, 항상 dict로 파싱
                        try:
                            payload_obj = json.loads(data_text)
                        except Exception as e:
                            # print(f"❌ SSE JSON 파싱 오류: {e} raw={data_text[:200]}")
                            # dict가 아니면 전달하지 않음
                            payload_obj = None

                        event = {"event": event_type, "id": event_id, "data": payload_obj}
                        self.push(event)

                        # 등록된 핸들러 즉시 호출 (dict 전달)
                        if self.sse_event_handler and payload_obj is not None:
                            try:
                                self.sse_event_handler(payload_obj)
                            except Exception as eh:
                                print(f"❌ SSE handler error: {eh}")

                    # 다음 이벤트를 위해 초기화
                    data_buf = []
                    event_type = None
                    event_id = None
                    continue

                if line.startswith(':'):
                    continue

                if line.startswith('data:'):
                    data_buf.append(line[len('data:'):].strip())
                elif line.startswith('event:'):
                    event_type = line[len('event:'):].strip()
                elif line.startswith('id:'):
                    event_id = line[len('id:'):].strip()
                else:
                    pass
        except Exception:
            pass
        finally:
            self.queue = Queue()
            self.is_run_sse = False
    def request_event(self):
        """연결 재시도 루프: /events/{name}-GCS"""
        while not self.is_run_sse:
            try:
                
                self.open_sse_stream(SSE_EVENTS_URL)
                self.is_run_sse = True
            except Exception:
                time.sleep(2.0)
    def push(self, text: str):
        """수신 텍스트를 큐에 적재"""
        try:
            self.queue.put(text)
        except Exception:
            pass