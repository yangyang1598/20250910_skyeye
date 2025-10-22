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
       
    def get_sensor_statuses(self):
        """지도 원 색상을 위한 센서 상태 목록 반환"""
        self.get_fire_sensor()
        return [
            {
                "index": getattr(sensor, "sensor_id", None),
                "flags": getattr(sensor, "flags", None),
                "gas_index": getattr(sensor, "gas_index", None),
            }
            for sensor in self.sensor_list
        ]
    
    def set_fire_sensor(self,index=None) :
        """산불센서 리스트를 UI에 설정"""
        gas_index_config={
            0:"정상",
            100:"산불",
            200:"산 안개"
        }

        flags_config={
            0:"수신 오류",
            1:"정상 수신"
        }
        for sensor in self.sensor_list:
            if sensor.sensor_id==index+1:
                self.label_data_sensor_temp.setText(str(sensor.temp))
                self.label_data_sensor_rh.setText(str(sensor.rh))
                self.label_data_sensor_pressure.setText(str(sensor.pressure))
                self.label_data_sensor_gas_index.setText(gas_index_config.get(sensor.gas_index,"가스센서 인덱스 이상"))
                self.label_data_sensor_trend.setText(str(sensor.trend))
                self.label_data_sensor_vcap.setText(str(sensor.vcap if sensor.vcap else "-"))
                self.label_data_sensor_flags.setText(flags_config.get(sensor.flags,"수신 상태 이상"))
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
