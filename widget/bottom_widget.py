import sys
import os
import time
from PySide6.QtWidgets import QApplication, QMessageBox, QWidget, QDialog
from PySide6.QtCore import Signal, QSignalBlocker

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_bottom_widget import Ui_Form
from db.db_poi import Poi
from dialog.popup_patrol_dialog import PopupPatrolDialog
from protocol import Protocol
import protocol as protocol_module

class BottomWidget(QWidget, Ui_Form):
    moveLocationRequested = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.current_camera_pitch = None

        self.cmd_status=None
        self.poi_status=None
        self.mode_status=None

        self.init_command=None
        self.round_command=False

        self.protocol=Protocol()
        self.db_poi=Poi()

        self.button_move_location.clicked.connect(self.on_click_move_location)
        self.button_start_patrol.clicked.connect(self.on_click_start_patrol)
        # 라디오 변경 감지: 변할 때마다 정지 명령 전송 + 버튼 텍스트 초기화
        self.radio_around_patrol.toggled.connect(self.on_radio_btn_toggled)
        self.radio_registered_loction.toggled.connect(self.on_radio_btn_toggled)
        
    def is_registered_patrol_running(self) -> bool:
        """등록지점 순찰이 진행 중인지 여부 반환"""
        try:
            return bool(self.radio_registered_loction.isChecked() and self.button_start_patrol.text() == "순찰 중지")
        except Exception:
            return False

    def on_click_move_location(self):
        """헬리카이트 위치 이동 버튼 클릭 시 위치 이동 신호 발생"""
        self.moveLocationRequested.emit()
    def set_camera_pitch(self, pitch):
        """주변 순찰 시 사용할 camera pitch 값 get"""
        try:
            self.current_camera_pitch = float(pitch) if pitch is not None else None
        except (ValueError, TypeError):
            self.current_camera_pitch = None
    def set_interactive_enabled(self, enabled: bool):
        """버튼/라디오 등의 인터랙션 가능 여부 설정"""
        try:
            self.button_move_location.setEnabled(enabled)
            self.button_start_patrol.setEnabled(enabled)
            self.radio_around_patrol.setEnabled(enabled)
            self.radio_registered_loction.setEnabled(enabled)
        except Exception as e:
            print(f"⚠️ 하단 위젯 인터랙션 설정 오류: {e}")

    def receive_connect_signal(self, cmd: dict):
        """Protocol에서 받은 connect 데이터 출력"""

        self.init_command = True

        self.cmd_status = cmd.get("cmd")
        self.mode_status = cmd.get("mode")
        
        if self.cmd_status =="connect":
            self.poi_status = cmd.get("value").get("poi")

        #해당 변수 소멸(함수 종료)시점까지 라디오버튼에 대한 signal 차단
        blocker1 = QSignalBlocker(self.radio_around_patrol)
        blocker2 = QSignalBlocker(self.radio_registered_loction)

        if self.poi_status == '' or self.mode_status == 'stop':
            self.button_start_patrol.setChecked(False)
            self.button_start_patrol.setText("순찰 시작")
        else:
            if self.poi_status == "round" or (self.cmd_status == "round" and self.mode_status == "start"):
                self.radio_around_patrol.setChecked(True)
            elif self.poi_status == "poi" or (self.cmd_status == "poi" and self.mode_status == "start"):
                self.radio_registered_loction.setChecked(True)

            self.button_start_patrol.setChecked(True)
            self.button_start_patrol.setText("순찰 중지")

        self.init_command = False

    def on_click_start_patrol(self):
        """순찰 시작 중지 설정"""
        if self.button_start_patrol.isChecked():
            if self.radio_around_patrol.isChecked() :
                dialog = PopupPatrolDialog()
                if dialog.exec() == QDialog.Accepted:
                    self.button_start_patrol.setText("순찰 중지")
                    pitch_value = self.current_camera_pitch if self.current_camera_pitch is not None else 0.0
                    self.set_text = {
                        "cmd": "round",
                        "mode": "set",
                        "value": { "yaw": "30", "pitch": f"{pitch_value:.2f}" }
                    }
                    self.protocol.post_event_message(self.set_text)
                    time.sleep(0.1)
                    self.start_text = {
                        "cmd": "round",
                        "mode": "start",
                        "value": { "stay": f"{dialog.line_edit_patrol_second.text()}" }
                    }
                    self.protocol.post_event_message(self.start_text)
                else:
                    self.button_start_patrol.setChecked(False)

            elif self.radio_registered_loction.isChecked():
                
                dialog = PopupPatrolDialog()
                if dialog.exec() == QDialog.Accepted:
                    self.button_start_patrol.setText("순찰 중지")

                    self.db_poi.site_id=protocol_module.SITE_ID
                    poi_data=self.db_poi.select()
                    # DB의 POI 리스트를 프로토콜 포맷으로 변환
                    poi_payload = {}
                    try:
                        if poi_data:
                            for p in poi_data:
                                try:
                                    pid = int(p.poi_id) if p.poi_id is not None else (len(poi_payload) + 1)
                                except Exception:
                                    pid = len(poi_payload) + 1
                                key = f"poi{pid}"
                                lat = float(p.latitude) if p.latitude is not None else 0.0
                                lng = float(p.longitude) if p.longitude is not None else 0.0
                                alt = int(p.altitude) if p.altitude is not None else 0
                                zoomlevel = int(p.zoom_level) if p.zoom_level is not None else 0
                                poi_payload[key] = { "lat": lat, "lng": lng, "alt": alt, "zoomlevel": zoomlevel }
                    except Exception as e:
                        print(f"⚠️ POI 변환 오류: {e}")
                    # self.poi_status에 설정하여 전송에 사용
                    self.poi_status = poi_payload
                    
                    self.set_text = {
                        "cmd": "poi",
                        "mode": "set",
                        "value": self.poi_status #poi 마커의 모든 값 
                    }
                    self.protocol.post_event_message(self.set_text)
                    time.sleep(0.1)
                    self.start_text = {
                        "cmd": "poi",
                        "mode": "start",
                        "value": { "stay": f"{dialog.line_edit_patrol_second.text()}" }
                    }
                    self.protocol.post_event_message(self.start_text)
        else:
            # 현재 선택된 라디오에 따라 정지 명령 cmd 설정
            cmd_type = "round" if self.radio_around_patrol.isChecked() else "poi"
            self.stop_text = {
                    "cmd": cmd_type,
                    "mode": "stop",
                    "value": "" 
                    }
            self.protocol.post_event_message(self.stop_text)
            self.button_start_patrol.setText("순찰 시작")

    def on_radio_btn_toggled(self, checked: bool):

        # 프로그램적 초기화 중 발생한 토글은 무시합니다.
        if self.init_command:
            return
        cmd_type = "poi" if self.radio_around_patrol.isChecked() else "round"
        self.stop_text = {
            "cmd": cmd_type,
            "mode": "stop",
            "value": ""
        }
        self.protocol.post_event_message(self.stop_text)
        self.button_start_patrol.setText("순찰 시작")
        self.button_start_patrol.setChecked(False)
        # 위젯이 보이는 상태에서 체크되었을 때만 안내 문구 표시
        if self.radio_around_patrol.isChecked() and self.isVisible() and not self.round_command:
            QMessageBox.information(
                self,
                "Round View",
                "현재 카메라 Yaw,Pitch 각도를 기준으로 작동합니다.\n (yaw 값은 ± 30º 주기적으로 변경,Pitch 값은 고정)"
            )
            self.round_command=True

        if self.radio_registered_loction.isChecked():
            self.round_command=False
        
    def set_location(self, lat, lng):
        """마우스 커서 위치 위경도 정보 업데이트"""
        self.label_value_latitude.setText(f"{lat:.6f}")
        self.label_value_longitude.setText(f"{lng:.6f}")

       

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = BottomWidget()
    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
