import sys
import os
from PySide6.QtWidgets import QApplication, QWidget,QButtonGroup 


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_ir_camera_set_widget import Ui_Form


class IRCameraSetWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setup_radio_group()

    def setup_radio_group(self):
        self.sensor_group = QButtonGroup(self)
        self.sensor_group.setExclusive(True)
        self.sensor_group.addButton(self.radio_eo)
        self.sensor_group.addButton(self.radio_ir)
        self.sensor_group.addButton(self.radio_EO_IR)
        self.sensor_group.addButton(self.radio_IR_EO)

        # 라디오 버튼 그룹 분리: 컬러 팔레트 그룹
        self.palette_group = QButtonGroup(self)
        self.palette_group.setExclusive(True)
        self.palette_group.addButton(self.radio_white_hot)
        self.palette_group.addButton(self.radio_black_hot)
        self.palette_group.addButton(self.radio_red_hot)
        self.palette_group.addButton(self.radio_ironbow)
        self.palette_group.addButton(self.radio_rainbow)
        self.palette_group.addButton(self.radio_rainbow_hc)
        self.palette_group.addButton(self.radio_hot_iron)
        self.palette_group.addButton(self.radio_lava)
        self.palette_group.addButton(self.radio_arctic)

    def set_radio_image_sensor(self,data):
        image_sensor=data.get('value').get('image_sensor')
        color_palette = data.get('value').get('color_palette')
        
        #영상 센서 형식식
        if image_sensor=="eo1" or image_sensor=="eo":
            self.radio_eo.setChecked(True)
        elif image_sensor=="ir":
            self.radio_ir.setChecked(True)
        elif image_sensor=="eo_ir_pip":
            self.radio_EO_IR.setChecked(True)
        elif image_sensor=="ir_eo_pip":
            self.radio_visible.setChecked(True)
        
        #컬러 팔레트
        if color_palette=="whileHot" or color_palette=="whiteHot":
            self.radio_white_hot.setChecked(True)
        elif color_palette=="blackHot":
            self.radio_black_hot.setChecked(True)
        elif color_palette=="redHot":
            self.radio_red_hot.setChecked(True)
        elif color_palette=="ironbow":
            self.radio_ironbow.setChecked(True)
        elif color_palette=="rainbow":
            self.radio_rainbow.setChecked(True)
        elif color_palette=="rainbowHc":
            self.radio_rainbow_hc.setChecked(True)
        elif color_palette=="hotIron":
            self.radio_hot_iron.setChecked(True)
        elif color_palette=="lava":
            self.radio_lava.setChecked(True)
        elif color_palette=="arctic":
            self.radio_arctic.setChecked(True)

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = IRCameraSetWidget()

    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
