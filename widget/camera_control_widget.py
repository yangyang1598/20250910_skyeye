# -*- coding: utf-8 -*-

import sys
import os
from PySide6.QtWidgets import QApplication, QWidget
import math
# 상위 디렉토리의 ui 모듈을 import하기 위해 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ui.ui_camera_control_widget import Ui_Form


class CameraControlWidget(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setting_toggle_icon()
        self.horizontal_slider_cam_speed.valueChanged.connect(self.display_cam_speed)

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

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = CameraControlWidget()
    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()