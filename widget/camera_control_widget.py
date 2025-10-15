# -*- coding: utf-8 -*-

import sys
import os
import time
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QAbstractButton
# 상위 디렉토리의 ui 모듈을 import하기 위해 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ui.ui_camera_control_widget import Ui_Form
from protocol import Protocol

class CameraControlWidget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()

        self.text=None
        self.protocol=Protocol()

        self.setupUi(self)
        # 제어 토글 이미지 대입
        self.setting_toggle_icon() 
        # 카메라 속도 speed bar 설정
        self.horizontal_slider_cam_speed.valueChanged.connect(self.display_cam_speed)
        # 버튼 클릭 이벤트 연결
        self._wire_button_prints()

    def display_cam_speed(self):
        self.label_cam_speed.setText(f"{self.horizontal_slider_cam_speed.value()}")
        
    def setting_toggle_icon(self):
        # Follow Yaw 토글 버튼 스타일 적용 (프로젝트 icon 폴더 경로 사용)
        icon_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'icon'))
        on_png = os.path.join(icon_dir, 'switch-on.png')
        off_png = os.path.join(icon_dir, 'switch-off.png')
        plus_png= os.path.join(icon_dir, 'plus.png')
        minus_png = os.path.join(icon_dir, 'minus.png')
        # Windows 경로 구분자를 QSS에서 호환되도록 슬래시로 변경
        on_png_qss = on_png.replace('\\', '/')
        off_png_qss = off_png.replace('\\', '/')
        plus_png_qss = plus_png.replace('\\', '/')  
        minus_png_qss = minus_png.replace('\\', '/')  


        self.toggle_active_follow_yaw.setStyleSheet(
            u"QPushButton:checked {\n"
            "    border: none;\n"
            f"    image: url('{on_png_qss}');\n"
            "}\n"
            "QPushButton:!checked {\n"
            "    border: none;\n"
            f"    image: url('{off_png_qss}');\n"
            "}"
        )
        self.toggle_active_motor.setStyleSheet(
            u"QPushButton:checked {\n"
            "    border: none;\n"
            f"    image: url('{on_png_qss}');\n"
            "}\n"
            "QPushButton:!checked {\n"
            "    border: none;\n"
            f"    image: url('{off_png_qss}');\n"
            "}"
        )
        self.toggle_active_osd.setStyleSheet(
            u"QPushButton:checked {\n"
            "    border: none;\n"
            f"    image: url('{on_png_qss}');\n"
            "}\n"
            "QPushButton:!checked {\n"
            "    border: none;\n"
            f"    image: url('{off_png_qss}');\n"
            "}"
        )
        self.button_zoom_in.setStyleSheet(
            u"QPushButton {\n"
        "    border: none;\n"
        f"    background-image: url('{plus_png_qss}');\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center;\n"
        "    min-width: 50px;\n"
        "    min-height: 50px;\n"
        "}")

        self.button_zoom_out.setStyleSheet(
            u"QPushButton {\n"
        "    border: none;\n"
        f"    background-image: url('{minus_png_qss}');\n"
        "    background-repeat: no-repeat;\n"
        "    background-position: center;\n"
        "    min-width: 50px;\n"
        "    min-height: 50px;\n"
        "}")


        # 체크 가능 상태 유지
        self.toggle_active_follow_yaw.setCheckable(True)
        self.toggle_active_motor.setCheckable(True)
        self.toggle_active_osd.setCheckable(True)
        self.button_zoom_in.setCheckable(True)
        self.button_zoom_out.setCheckable(True)

    def _wire_button_prints(self):

        for name in dir(self):
            if name.startswith("button_"):
                obj = getattr(self, name, None)
                if isinstance(obj, QAbstractButton):
                    # 'checked' 인자도 함께 받아서 시그널 시그니처와 일치시킵니다
                    obj.clicked.connect(lambda checked=False, n=name.replace("button_", ""): self.on_button_clicked(n, checked))
    def on_button_clicked(self, btn_name: str, checked: bool=False):
        # 버튼 클릭 시 딕셔너리 생성 후 self.text에 저장
        if "home" in btn_name:
            #home 키 클릭릭
            cmd=btn_name
            mode=""
            value=""
            stop=False

        elif "zoom" in  btn_name:
            #zoom 키 클릭
            cmd,mode=btn_name.split("_")
            value=""
            stop=True
            stop_cmd=cmd
            stop_mode="stop"
        else:
            #방향키 클릭
            cmd=btn_name
            mode="speed"
            value=str(self.horizontal_slider_cam_speed.value())
            stop=True
            stop_cmd="stop"
            stop_mode=""

        self.text = {
            "cmd": cmd,
            "mode": mode,
            "value": value,
        }
        self.protocol.post_event_message(self.text)
        if stop:
            self.stop_text = {
            "cmd": stop_cmd,
            "mode": stop_mode,
            "value": "",
            }
            time.sleep(0.1)
            self.protocol.post_event_message(self.stop_text)

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = CameraControlWidget()
    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


