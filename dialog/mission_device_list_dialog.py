import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_mission_device_list_dialog import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog

class MissionDeviceListDialog(QDialog, Ui_Dialog):
    def __init__(self,data):
        super().__init__()
        self.data=data
        self.names=None

        self.setupUi(self)
        self.populate_device_list()
        
    def populate_device_list(self):
        """미션 디바이스 목록을 리스트 위젯에 추가"""
        self.names = [item['name'] for item in self.data]
        if self.names:
            self.combo_mission_device_list.clear()
            for name in self.names:
                self.combo_mission_device_list.addItem(name)
    def accept(self):
        """OK 클릭 시 선택한 항목의 missiondevice_serial_number를 DEVICE_NAME에 설정"""
        try:
            selected_name = self.combo_mission_device_list.currentText().strip()
            item = next((it for it in self.data if it.get('name') == selected_name), None)
            if not item:
                print("⚠️ 선택 항목을 찾을 수 없습니다.")
                return super().accept()

            serial = item.get('missiondevice_serial_number')
            if serial:
                import protocol as protocol_module
                protocol_module.DEVICE_NAME = serial
                print(f"✅ DEVICE_NAME 변경: {serial}")
            else:
                print("⚠️ 선택 항목에 missiondevice_serial_number가 없습니다.")
        except Exception as e:
            print(f"❌ DEVICE_NAME 설정 중 오류: {e}")
        return super().accept()
def main():
    app = QApplication(sys.argv)
    dialog = MissionDeviceListDialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()