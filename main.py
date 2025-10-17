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
from widget.bottom_widget import BottomWidget
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
            self.main_window.show_camera_control_widget()
            self.main_window.show_bottom_widget()

        except Exception as e:
            print(f"❌ 카메라 다이얼로그 표시 오류: {e}")
            import traceback
            traceback.print_exc()

    @Slot(float, float)
    def updateCursorLatLng(self, lat, lng):
        """JavaScript → Python: 마우스 커서 위젯 위치 업데이트"""
        self.main_window.update_cursor_latlng(lat, lng)

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
        self.bottom_widget = BottomWidget()

        self.protocol = Protocol()
        
        self.setup_ui()
        self.setup_web_channel()
        self.setup_timer()
        self.setup_sse_event()
        
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

        self.main_layout.setRowStretch(0, 10)
        self.main_layout.setRowStretch(1, 0)

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

    def setup_sse_event(self):
        # 핸들러 등록: handle_sse_event 메서드를 protocol의 self.sse_event_handler로 등록
        #  sse_event_handler 값이 등록되는 경우 해당 함수 자동 호출
        self.protocol.set_sse_event_handler(self.handle_sse_event)

        # 스트림 연결 시작
        self.protocol.open_sse_stream()
        self.text = {
            "cmd": "connect",
            "mode": "",
            "value": ""
        }
        self.protocol.post_event_message(self.text)
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

    def show_camera_control_widget(self):
        """카메라 제어 위젯 표시"""

        if self.camera_control_widget and self.camera_control_widget.isVisible():
            self.camera_control_widget.hide()
            return

        if not self.camera_control_widget:
            self.camera_control_widget = CameraControlWidget()
            self.right_layout.addWidget(self.camera_control_widget)

        self.camera_control_widget.show()

    # --------------------------
    # 하단 위젯 표시 관련
    # --------------------------
    def show_bottom_widget(self):
        """하단 위젯 표시"""

        if self.bottom_widget:
            if self.bottom_widget.isVisible():
                self.bottom_widget.hide()
                return
            self.bottom_widget.moveLocationRequested.connect(self.center_map_on_tracked)
            self.main_layout.addWidget(self.bottom_widget,1,0)
            # 기존 데이터가 있으면 초기 동기화
            if self.device_data:
                self.bottom_widget.set_camera_pitch(self.device_data.get('camera_pitch'))
            
        self.bottom_widget.show()
    
    def center_map_on_tracked(self):
        """현재 추적 위치로 지도 중심 이동"""

        js_code = """
        if (typeof focusTracked === 'function') { focusTracked(); }
        """
        self.web_view.page().runJavaScript(js_code)
        
    def update_cursor_latlng(self, lat, lng):
        if self.bottom_widget:
            self.bottom_widget.set_location(lat, lng)
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

        # BottomWidget에 카메라 pitch 전달
        if self.bottom_widget:
            try:
                self.bottom_widget.set_camera_pitch(data.get('camera_pitch'))
            except Exception as e:
                print(f"⚠️ BottomWidget pitch 업데이트 오류: {e}")

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

    def handle_sse_event(self, data):
        """SSE 이벤트 수신 처리: connect 포함 시 BottomWidget에서 출력"""
        data=json.loads(data) #다시 dict 형식으로 변환
        # print(f"main App {data},{type(data)},{data.get('cmd')},{isinstance(data, dict)}")
       
        if isinstance(data, dict) and data.get('cmd') == 'connect':
            if self.bottom_widget:
                self.bottom_widget.print_connect_cmd(data)
            return

# ------------------------------
# 실행부
# ------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())


