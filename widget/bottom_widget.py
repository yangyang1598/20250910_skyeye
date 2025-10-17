import sys
import os
import time
from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtCore import Signal

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_bottom_widget import Ui_Form
from dialog.popup_patrol_dialog import PopupPatrolDialog
from protocol import Protocol

class BottomWidget(QWidget, Ui_Form):
    moveLocationRequested = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.current_camera_pitch = None
        self.poi_status=None
        self.protocol=Protocol()

        self.button_move_location.clicked.connect(self.on_click_move_location)
        self.button_start_patrol.clicked.connect(self.on_click_start_patrol)
        
    def on_click_move_location(self):
        """헬리카이트 위치 이동 버튼 클릭 시 위치 이동 신호 발생"""
        self.moveLocationRequested.emit()
    def set_camera_pitch(self, pitch):
        """주변 순찰 시 사용할 camera pitch 값 get"""
        try:
            self.current_camera_pitch = float(pitch) if pitch is not None else None
        except (ValueError, TypeError):
            self.current_camera_pitch = None
    def print_connect_cmd(self, cmd: str):
        """Protocol에서 받은 connect 데이터 출력"""
        self.poi_status=cmd.get("value").get("poi")
        if self.poi_status == '':
            self.button_start_patrol.setChecked(False)
            self.button_start_patrol.setText("순찰 시작")
        else:
            if self.poi_status=="round":
                self.radio_around_patrol.setChecked(True)

            elif self.poi_status=="poi":
                self.radio_registered_loction.setChecked(True)

            self.button_start_patrol.setChecked(True)
            self.button_start_patrol.setText("순찰 중지")


    def on_click_start_patrol(self):
        """순찰 시작 중지 설정정"""
        if self.button_start_patrol.isChecked():
            self.button_start_patrol.setText("순찰 중지")
        else:
            self.stop_text = {
                    "cmd": "round",
                    "mode": "stop",
                    "value": "" 
                    }


            self.protocol.post_event_message(self.stop_text)
            self.button_start_patrol.setText("순찰 시작")


        if self.radio_around_patrol.isChecked() and self.button_start_patrol.isChecked():
            """주변 순찰 모드"""
            dialog = PopupPatrolDialog()
            if dialog.exec() == QDialog.Accepted:
                print(dialog.line_edit_patrol_second.text())
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
