import requests
import json
# ------------------------------
# 설정 상수
# ------------------------------
MISSION_DEVICE_LOG_URL = "http://skysys.iptime.org:8000/mission_device_log/?name="
EVENT_URL = "http://skysys.iptime.org:8000/messages/"
TOKEN = "Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537"
DEVICE_NAME = "MD-2023-03-L"

class Protocol:
    def __init__(self) -> None:
        pass
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