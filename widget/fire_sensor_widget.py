import sys
import os
from PySide6.QtWidgets import QApplication, QWidget

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_fire_sensor_widget import Ui_Form
from db.db_sensor import Sensor

class FireSenSorWidget(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sensor_list=[]

        self.fire_sensor=Sensor()
        
        self.get_fire_sensor()
    
    def get_fire_sensor(self) :
        """인덱스에 해당하는 산불센서 객체 반환"""
        self.sensor_list=self.fire_sensor.select_all()
       

    def set_fire_sensor(self,index=None) :
        """산불센서 리스트를 UI에 설정"""
        for sensor in self.sensor_list:
            if sensor.sensor_id==index:
                self.label_data_sensor_temp.setText(str(sensor.temp))
                self.label_data_sensor_rh.setText(str(sensor.rh))
                self.label_data_sensor_pressure.setText(str(sensor.pressure))
                self.label_data_sensor_gas_index.setText(str(sensor.gas_index))
                self.label_data_sensor_trend.setText(str(sensor.trend))
                self.label_data_sensor_vcap.setText(str(sensor.vcap))
                self.label_data_sensor_flags.setText(str(sensor.flags))
                self.label_data_sensor_checksum.setText(str(sensor.crc))
                break

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = FireSenSorWidget()
    widget.get_fire_sensor()

    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
