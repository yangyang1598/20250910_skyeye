import sys, os
import requests
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer, QObject, Slot
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

# dialog 폴더의 camera_md_data_dialog import
from dialog.camera_md_data_dialog import CameraMdDataDialog

server_url = "http://skysys.iptime.org:8000/mission_device_log/?name="
token ="Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537" #device 계정 Token
device_name = "MD-2023-04-L"
class WebChannelHandler(QObject):
    """JavaScript와 Python 간의 통신을 위한 핸들러"""
    
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
    
    @Slot('QVariant') 
    # JavaScript의 모든 타입을 QVariant로 전달받음
    def showCameraDialog(self, data):
        """JavaScript에서 호출되는 메서드 - 카메라 다이얼로그 표시"""
        try:
            # QVariant에서 Python dict로 변환
            if isinstance(data, str):
                # 문자열인 경우 JSON 파싱
                data = json.loads(data)
            elif hasattr(data, 'toVariant'):
                # QJsonValue인 경우 Python 객체로 변환
                data = data.toVariant()
            
            print(f"카메라 다이얼로그 데이터 수신: {type(data)}")
            self.main_window.show_camera_dialog(data)
        except Exception as e:
            print(f"카메라 다이얼로그 표시 오류: {e}")
            import traceback
            traceback.print_exc()

class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.device_data = None
        
        # 웹 뷰 생성 (전체 화면)
        self.web_view = QWebEngineView()
        
        # 메인 위젯과 레이아웃 설정
        self.setup_ui()
        
        # WebChannel 설정 (JavaScript와 Python 통신)
        self.setup_web_channel()
        
        # 웹 엔진 설정
        self.web_view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        path = os.path.abspath("map.html")
        self.web_view.load(QUrl.fromLocalFile(path))
        self.web_view.loadFinished.connect(self.on_load_finished)
        
        # 주기적으로 API 데이터 업데이트
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_device_data)
        self.timer.start(2000)  # 2초마다 업데이트
        
        # 윈도우 설정
        self.setWindowTitle("SkyEye Map Application")
        self.setGeometry(100, 100, 1400, 800)
        
        # 다이얼로그 변수 초기화
        self.camera_dialog = None
        
        self.show()

    def show_camera_dialog(self, data):
        """카메라 다이얼로그를 표시하고 데이터 업데이트"""
        print(f"카메라 다이얼로그 표시 - 데이터: {data}")
        
        # 기존 다이얼로그가 있다면 닫기
        if self.camera_dialog:
            self.camera_dialog.close()
        
        # 새 다이얼로그 생성
        self.camera_dialog = CameraMdDataDialog()
        self.camera_dialog.setParent(self)
        
        # 다이얼로그 윈도우 플래그 설정 (타이틀바 포함)
        from PySide6.QtCore import Qt
        self.camera_dialog.setWindowFlags(
            Qt.Dialog | 
            Qt.WindowStaysOnTopHint |
            Qt.WindowCloseButtonHint |
            Qt.WindowTitleHint
        )
        
        # 다이얼로그를 우측에 위치시키기
        main_geometry = self.geometry()
        dialog_width = 310
        dialog_height = 480
        
        # 메인 윈도우 우측에 위치
        x = main_geometry.x() + main_geometry.width() - dialog_width - 20
        y = main_geometry.y() + 50
        
        self.camera_dialog.setGeometry(x, y, dialog_width, dialog_height)
        
        # 데이터 업데이트
        self.camera_dialog.update_data(data)
        
        # 다이얼로그 표시
        self.camera_dialog.show()
        
        # 다이얼로그가 닫힐 때 호출되는 메서드 연결
        self.camera_dialog.finished.connect(self.on_dialog_closed)

    def on_dialog_closed(self):
        """다이얼로그가 닫힐 때 호출되는 메서드"""
        self.camera_dialog = None

    def setup_ui(self):
        """UI 레이아웃 설정"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 메인 레이아웃
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 여백 제거
        layout.addWidget(self.web_view)
        central_widget.setLayout(layout)

    def setup_web_channel(self):
        """JavaScript와 Python 간 통신을 위한 WebChannel 설정"""
        self.channel = QWebChannel()
        self.handler = WebChannelHandler(self)
        self.channel.registerObject("pyHandler", self.handler)
        self.web_view.page().setWebChannel(self.channel)

    def get_mission_device_log(self):
        try:
            url = server_url +device_name  # device name 하드 코딩 추후 변경 필요요
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
        """주기적으로 디바이스 데이터를 가져와서 지도에 업데이트하고, 다이얼로그가 열려있으면 업데이트"""
        data = self.get_mission_device_log()
                
        if data:
            self.device_data = data
            # JavaScript 함수 호출하여 지도 업데이트
            js_code = f"""
            if (typeof updateDroneData === 'function') {{
                updateDroneData({json.dumps(data)});
            }}
            """
            self.web_view.page().runJavaScript(js_code)
            
            # 다이얼로그가 열려있으면 데이터 업데이트
            if self.camera_dialog and self.camera_dialog.isVisible():
                try:
                    self.camera_dialog.update_data(data)
                except Exception as e:
                    print(f"다이얼로그 데이터 업데이트 오류: {e}")
           
    def on_load_finished(self, ok):
        if ok:
            print("✅ HTML 로딩 완료!")
            # WebChannel 초기화 JavaScript 코드 실행
            js_init_code = """
            new QWebChannel(qt.webChannelTransport, function(channel) {
                window.pyHandler = channel.objects.pyHandler;
                console.log("WebChannel 연결 완료");
            });
            """
            # Java -> python 통신용 QWebChannel 초기화
            self.web_view.page().runJavaScript(js_init_code)
            
            # 초기 데이터 로드
            self.update_device_data()
        else:
            print("❌ HTML 로딩 실패")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())