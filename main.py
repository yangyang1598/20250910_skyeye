import sys
import os
import json
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout,QSpacerItem,QSizePolicy
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QTimer, QObject, Slot
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWebChannel import QWebChannel

# 위젯 모듈 임포트
from widget.camera_md_data_widget import CameraMdDataWidget
from widget.camera_control_widget import CameraControlWidget
from protocol import Protocol

# ------------------------------
# WebChannel 핸들러
# ------------------------------
class WebChannelHandler(QObject):
    """JavaScript ↔ Python 통신 핸들러"""

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    @Slot('QVariant')
    def showCameraDialog(self, data):
        """JavaScript → Python: 카메라 다이얼로그 호출"""
        try:
            if isinstance(data, str):
                data = json.loads(data)
            elif hasattr(data, 'toVariant'):
                data = data.toVariant()

            print(f"📷 카메라 다이얼로그 데이터 수신: {type(data)}")
            self.main_window.show_camera_md_data_widget(data)
            self.main_window.show_camera_control()

        except Exception as e:
            print(f"❌ 카메라 다이얼로그 표시 오류: {e}")
            import traceback
            traceback.print_exc()


# ------------------------------
# 메인 윈도우 클래스
# ------------------------------
class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.device_data = None
        self.camera_md_data_widget = None
        self.camera_control_widget = None
        self.right_container = None
        self.right_layout = None

        self.protocol = Protocol()
        
        self.setup_ui()
        self.setup_web_channel()
        self.setup_timer()

        self.load_map()
        self.setup_window()

    # --------------------------
    # 초기화 관련 메서드
    # --------------------------
    def setup_ui(self):
        """메인 UI 설정"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.web_view = QWebEngineView()
        self.web_view.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)

        self.main_layout = QGridLayout()
        # self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.web_view, 0, 0)
        self.main_layout.setColumnStretch(0, 10)
        self.main_layout.setColumnStretch(1, 0)

        central_widget.setLayout(self.main_layout)

    def setup_web_channel(self):
        """QWebChannel 설정 (JavaScript ↔ Python 통신)"""
        self.channel = QWebChannel()
        self.handler = WebChannelHandler(self)
        self.channel.registerObject("pyHandler", self.handler)
        self.web_view.page().setWebChannel(self.channel)

    def setup_timer(self):
        """주기적 데이터 갱신 타이머 설정"""
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_device_data)
        self.timer.start(2000)  # 2초마다 업데이트

    def setup_window(self):
        """윈도우 속성 설정"""
        self.setWindowTitle("SkyEye Map Application")
        # self.setGeometry(0, 0, 1000, 800) #화면 사이즈 수동 설정
        self.showMaximized() # 화면 최대화
        self.show()

    def load_map(self):
        """HTML 지도 로드"""
        path = os.path.abspath("map.html")
        self.web_view.load(QUrl.fromLocalFile(path))
        self.web_view.loadFinished.connect(self.on_load_finished)
    # def post_connect_event(self):
    #     """연결 이벤트 전송"""
    #     self.protocol.post_event_message({
    #         "cmd": "connect",
    #         "mode": "",
    #         "value": "",
    #     })
    # --------------------------
    # 우측 위젯 표시 관련
    # --------------------------
    def ensure_right_container(self):
        """오른쪽 컨테이너(레이아웃)가 없으면 생성"""
        if not self.right_container:
            self.right_container = QWidget()
            self.right_layout = QVBoxLayout(self.right_container)
            self.right_layout.setContentsMargins(0, 0, 0, 0)
            self.main_layout.addWidget(self.right_container, 0, 1)

    def show_camera_md_data_widget(self, data):
        """카메라 메타데이터 위젯 표시"""
        print(f"카메라 위젯 표시 - 데이터: {data}")
        self.ensure_right_container()

        if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
            self.camera_md_data_widget.hide()
            return

        if not self.camera_md_data_widget:
            self.camera_md_data_widget = CameraMdDataWidget()
            self.right_layout.addWidget(self.camera_md_data_widget)

            # 위젯 간의 간격 추가(spacer)
            self.horizontalSpacer = QSpacerItem(10, 60, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
            self.right_layout.addItem(self.horizontalSpacer)

        try:
            self.camera_md_data_widget.update_data(data)
        except Exception as e:
            print(f"⚠️ 카메라 데이터 업데이트 오류: {e}")

        self.camera_md_data_widget.show()

    def show_camera_control(self):
        """카메라 제어 위젯 표시"""
        self.ensure_right_container()

        if self.camera_control_widget and self.camera_control_widget.isVisible():
            self.camera_control_widget.hide()
            return

        if not self.camera_control_widget:
            self.camera_control_widget = CameraControlWidget()
            self.right_layout.addWidget(self.camera_control_widget)

        self.camera_control_widget.show()

    # --------------------------
    # 데이터 처리 관련
    # --------------------------


    def update_device_data(self):
        """지도 및 위젯 데이터 업데이트"""
        data = self.protocol.get_mission_device_log()
        if not data:
            return

        self.device_data = data
        js_code = f"""
        if (typeof updateDroneData === 'function') {{
            updateDroneData({json.dumps(data)});
        }}
        """
        self.web_view.page().runJavaScript(js_code)

        if self.camera_md_data_widget and self.camera_md_data_widget.isVisible():
            try:
                self.camera_md_data_widget.update_data(data)
            except Exception as e:
                print(f"⚠️ 다이얼로그 데이터 업데이트 오류: {e}")

    # --------------------------
    # 이벤트 핸들러
    # --------------------------
    def on_load_finished(self, ok):
        if ok:
            print("✅ HTML 로딩 완료!")
            js_init_code = """
            new QWebChannel(qt.webChannelTransport, function(channel) {
                window.pyHandler = channel.objects.pyHandler;
                console.log("WebChannel 연결 완료");
            });
            """
            self.web_view.page().runJavaScript(js_init_code)
            self.update_device_data()
        else:
            print("❌ HTML 로딩 실패")


# ------------------------------
# 실행부
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())
