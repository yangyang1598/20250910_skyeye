import sys, os
import requests
import json
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtWebEngineCore import QWebEngineSettings

server_url = "http://skysys.iptime.org:8000/mission_device_log/?name="
token ="Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537" #device 계정 Token

class MapApp(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.device_data = None
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        path = os.path.abspath("map.html")  # 현재 실행 디렉토리에서 map.html 절대경로
        self.load(QUrl.fromLocalFile(path)) # QWebEngineView가 해당 HTML 파일을 브라우저처럼 렌더링
        self.loadFinished.connect(self.on_load_finished)
        
        # 주기적으로 API 데이터 업데이트
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_device_data)
        self.timer.start(2000)  # 2초마다 업데이트
        
        self.show()

    def get_mission_device_log(self):
        try:
            url = server_url + "MD-2025-02-L" # device name
            headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*', 'Authorization': token}
            response = requests.get(url, headers = headers)
            
            if response.status_code == 200:
                data = response.json()
                # print("API 응답 데이터:", data)
                return data
            else:
                print(f"API 오류: {response.status_code}")
                return None
        except Exception as e:
            print(f"API 요청 오류: {e}")
            return None

    def update_device_data(self):
        """주기적으로 디바이스 데이터를 가져와서 지도에 업데이트"""
        data = self.get_mission_device_log()
                
        if data:
            self.device_data = data
            # JavaScript 함수 호출하여 지도 업데이트
            js_code = f"""
            if (typeof updateDroneData === 'function') {{
                updateDroneData({json.dumps(data)});
            }}
            """
            self.page().runJavaScript(js_code) #self.page => 내부 페이지 객체 접근 메서드
           
    def on_load_finished(self, ok):
        if ok:
            print("✅ HTML 로딩 완료!")
            # 초기 데이터 로드
            self.update_device_data()
        else:
            print("❌ HTML 로딩 실패")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())