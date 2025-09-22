# -*- coding: utf-8 -*-

import sys
import os
from PySide6.QtWidgets import QApplication, QDialog
import math
# 상위 디렉토리의 ui 모듈을 import하기 위해 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ui.ui_camera_md_data_dialog import Ui_dialog

isIR=False #현재 하드코딩, 추후 서버 내 값 불러와서 설정정

class CameraMdDataDialog(QDialog,Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)    
    
    def update_data(self, data):
        """데이터 업데이트 함수"""
        try:
            # Mission Device (MD) 데이터 업데이트
            if 'latitude' in data:
                self.label_data_md_lat.setText(f"{float(data['latitude']):.6f}")

            if 'longitude' in data:
                self.label_data_md_lng.setText(f"{float(data['longitude']):.6f}")

            if 'altitude' in data and data['altitude'] is not None:
                self.label_data_md_alt.setText(f"{float(data['altitude']):.2f}")
            else:
                self.label_data_md_alt.setText("N/A ")

            if 'roll' in data:
                self.label_data_md_roll.setText(f"{float(data['roll']):.2f}")
            if 'pitch' in data:
                self.label_data_md_pitch.setText(f"{float(data['pitch']):.2f}")
            if 'yaw' in data:
                self.label_data_md_yaw.setText(f"{float(data['yaw']):.2f}")
            
            # Camera 데이터 업데이트
            # if 'camera_latitude' in data:
            #     self.label_data_cam_lat.setText(f"{float(data['camera_latitude']):.6f}")
            # elif 'latitude' in data:  # camera_latitude가 없으면 기본 latitude 사용
            #     self.label_data_cam_lat.setText(f"{float(data['latitude']):.6f}")
                
            # if 'camera_longitude' in data:
            #     self.label_data_cam_lng.setText(f"{float(data['camera_longitude']):.6f}")
            # elif 'longitude' in data:  # camera_longitude가 없으면 기본 longitude 사용
            #     self.label_data_cam_lng.setText(f"{float(data['longitude']):.6f}")
                
            if 'camera_roll' in data:
                self.label_data_cam_roll.setText(f"{float(data['camera_roll']):.2f}")
            if 'camera_pitch' in data:
                self.label_data_cam_pitch.setText(f"{float(data['camera_pitch']):.2f}")
            if 'camera_yaw' in data:
                self.label_data_cam_yaw.setText(f"{float(data['camera_yaw']):.2f}")
            if 'camera_zoom' in data:
                if not isIR:
                    #10배줌 카메라 기준
                    camera_zoom=int(data['camera_zoom'])-2384
                else:
                    #IR 카메라 기준
                    camera_zoom=int(data['camera_zoom'])
                camera_zoom= int(round(camera_zoom/ 16384 * 10))
                self.label_data_cam_zoom.setText(f"{camera_zoom}")
            
            # 다이얼로그 제목 업데이트
            device_name = data.get('missiondevice_serial_number', 'Unknown Device')
            self.setWindowTitle(f"Camera Data - {device_name}")
                
            # print(f"다이얼로그 데이터 업데이트 완료: {device_name}")
            
        except Exception as e:
            print(f"다이얼로그 데이터 업데이트 오류: {e}")

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    dialog = CameraMdDataDialog()
    dialog.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()