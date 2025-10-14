import sys, os
import requests
import json
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QHBoxLayout, QWidget, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer, QObject, Slot, Qt
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

# widget 폴더의 camera_md_data_widget import
from widget.camera_md_data_widget import CameraMdDataWidget
from widget.camera_control_widget import CameraControlWidget

server_url = "http://skysys.iptime.org:8000/mission_device_log/?name="
token ="Token 8dd64a2d6c5f87da2078e0e09b4b99db29614537" #device 계정 Token
device_name = "MD-2023-03-L"
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
            self.main_window.show_camera_md_data_widget(data)
            self.main_window.show_camera_control()
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
        self.camera_md_data_widget = None
        self.camera_control_widget=None
        self.right_container = None
        self.right_layout = None
        
        self.show()

    def show_camera_md_data_widget(self, data):
        """카메라 위젯을 메인 창 오른쪽에 도킹해서 표시"""
        print(f"카메라 위젯 표시 - 데이터: {data}")

        # 이미 열려있으면 숨김(토글) 후 종료
        if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
            self.camera_md_data_widget.hide()
            return

        # 기존 위젯이 있으면 재사용, 없으면 생성해 우측 컨테이너에 추가
        if not self.camera_md_data_widget:
            # 우측 컨테이너가 없으면 생성하여 메인 레이아웃에 추가 (상/하 분할용)
            if not self.right_container:
                self.right_container = QWidget()
                self.right_layout = QVBoxLayout(self.right_container)
                self.right_layout.setContentsMargins(0, 0, 0, 0)
                # 우측 컨테이너를 그리드의 (0, 1)에 명시적으로 배치
                self.main_layout.addWidget(self.right_container, 0, 1)
                # 열 비율을 10:1로 유지
                self.main_layout.setColumnStretch(0, 10)
                self.main_layout.setColumnStretch(1, 1)

            self.camera_md_data_widget = CameraMdDataWidget()
            self.right_layout.addWidget(self.camera_md_data_widget)

        # 데이터 업데이트 및 표시
        try:
            self.camera_md_data_widget.update_data(data)
        except Exception as e:
            print(f"카메라 위젯 데이터 업데이트 오류: {e}")

        self.camera_md_data_widget.show()

    def show_camera_control(self):
        if self.camera_control_widget and self.camera_control_widget.isVisible():
            self.camera_control_widget.hide()
            return
        if not self.camera_control_widget:
            # 우측 컨테이너가 없으면 생성하여 메인 레이아웃에 추가
            if not self.right_container:
                self.right_container = QWidget()
                self.right_layout = QVBoxLayout(self.right_container)
                self.right_layout.setContentsMargins(0, 0, 0, 0)
                # 우측 컨테이너를 그리드의 (0, 1)에 명시적으로 배치
                self.main_layout.addWidget(self.right_container, 0, 1)
                # 열 비율을 10:1로 유지
                self.main_layout.setColumnStretch(0, 10)
                self.main_layout.setColumnStretch(1, 1)

            self.camera_control_widget = CameraControlWidget()
            # 하단에 컨트롤 위젯 배치
            self.right_layout.addWidget(self.camera_control_widget)

        self.camera_control_widget.show()

    def on_dialog_closed(self):
        """다이얼로그가 닫힐 때 호출되는 메서드"""
        self.camera_md_data_widget = None
        self.camera_control_widget=None

    def setup_ui(self):
        """UI 레이아웃 설정"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 메인 레이아웃 (위젯 송출 함수에 사용하기 위해 인스턴스 변수 선언)
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # 좌측: 웹뷰를 (row=0, col=0)에 명시적으로 배치
        self.main_layout.addWidget(self.web_view, 0, 0)
        # 열 비율을 10:1로 설정
        self.main_layout.setColumnStretch(0, 10)
        self.main_layout.setColumnStretch(1, 1)

        central_widget.setLayout(self.main_layout)

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
            if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
                try:
                    self.camera_md_data_widget.update_data(data)
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