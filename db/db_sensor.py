import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from db.database import DATABASE
class Sensor:
    TABLE_NAME = 'sensor'

    def __init__(self) -> None:
        self.sensor_id = 0
        self.timestamp = ''
        self.temp = ''
        self.rh = ''
        self.pressure = None
        self.gas_index = None
        self.trend = ''
        self.vcap = ''
        self.flags = ''
        self.crc = ''

    
    def select_all(self):
        db = DATABASE()
        params = []
        
        try:
            sql = f"""SELECT * FROM {self.TABLE_NAME}"""

            rows = db.fetch_all(sql, params)
            sensor_list = []

            if rows:
                for r in rows:
                    sensor = Sensor()
                    sensor.sensor_id = r.get('sensor_id')
                    sensor.timestamp = r.get('timestamp')
                    sensor.temp = r.get('temp')
                    sensor.rh = r.get('rh')
                    sensor.pressure = r.get('pressure')
                    sensor.gas_index = r.get('gas_index')
                    sensor.trend = r.get('trend')
                    sensor.vcap = r.get('vcap')
                    sensor.flags = r.get('flags')
                    sensor.crc = r.get('crc')
                    sensor_list.append(sensor)
            return sensor_list
        except Exception as e:
            print(f"select error: {e}")
            return None
