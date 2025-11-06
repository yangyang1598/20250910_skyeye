import sys
import os
from PySide6.QtWidgets import QApplication, QWidget,QButtonGroup


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_ir_camera_set_widget import Ui_Form
from protocol import Protocol

class IRCameraSetWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.image_sensor=None
        self.color_palette=None

        self.protocol=Protocol()
        self.setup_radio_group()


    def setup_radio_group(self):

        # 영상 센서 라디오 그룹
        self.sensor_group = QButtonGroup(self)
        self.sensor_group.setExclusive(True)
        self.sensor_group.addButton(self.radio_eo)
        self.sensor_group.addButton(self.radio_ir)
        self.sensor_group.addButton(self.radio_eo_ir_pip)
        self.sensor_group.addButton(self.radio_ir_eo_pip)
        self.sensor_group.buttonClicked.connect(self.on_sensor_group_clicked)

        # 컬러 팔레트 라디오 그룹
        self.palette_group = QButtonGroup(self)
        self.palette_group.setExclusive(True)
        self.palette_group.addButton(self.radio_whiteHot)
        self.palette_group.addButton(self.radio_blackHot)
        self.palette_group.addButton(self.radio_redHot)
        self.palette_group.addButton(self.radio_ironbow)
        self.palette_group.addButton(self.radio_rainbow)
        self.palette_group.addButton(self.radio_rainbowHc)
        self.palette_group.addButton(self.radio_hotIron)
        self.palette_group.addButton(self.radio_lava)
        self.palette_group.addButton(self.radio_arctic)
        self.palette_group.buttonClicked.connect(self.on_palette_group_clicked)

    def set_radio_image_sensor(self,data):
        self.image_sensor=data.get('value').get('image_sensor')
        self.color_palette = data.get('value').get('color_palette')
        
        #영상 센서 형식식
        if self.image_sensor=="eo1" or self.image_sensor=="eo":
            self.radio_eo.setChecked(True)
        elif self.image_sensor=="ir":
            self.radio_ir.setChecked(True)
        elif self.image_sensor=="eo_ir_pip":
            self.radio_eo_ir_pip.setChecked(True)
        elif self.image_sensor=="ir_eo_pip":
            self.radio_ir_eo_pip.setChecked(True)
        
        #컬러 팔레트
        if self.color_palette=="whileHot" or self.color_palette=="whiteHot":
            self.radio_whiteHot.setChecked(True)
        elif self.color_palette=="blackHot":
            self.radio_blackHot.setChecked(True)
        elif self.color_palette=="redHot":
            self.radio_redHot.setChecked(True)
        elif self.color_palette=="ironbow":
            self.radio_ironbow.setChecked(True)
        elif self.color_palette=="rainbow":
            self.radio_rainbow.setChecked(True)
        elif self.color_palette=="rainbowHc":
            self.radio_rainbowHc.setChecked(True)
        elif self.color_palette=="hotIron":
            self.radio_hotIron.setChecked(True)
        elif self.color_palette=="lava":
            self.radio_lava.setChecked(True)
        elif self.color_palette=="arctic":
            self.radio_arctic.setChecked(True)

    def on_sensor_group_clicked(self, btn):

        self.image_sensor=btn.objectName().replace("radio_", "")
        self.on_radio_clicked()

    def on_palette_group_clicked(self, btn):

        self.color_palette=btn.objectName().replace("radio_", "")
        self.on_radio_clicked()

    def on_radio_clicked(self):
        self.protocol.post_event_message({
            "cmd": "ir",
            "mode": "optical",
            "value": {
                "image_sensor": self.image_sensor,
                "color_palette": self.color_palette,
            },
            "LRF":""
        })


def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = IRCameraSetWidget()

    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
