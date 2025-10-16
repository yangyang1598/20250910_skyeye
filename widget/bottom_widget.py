import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_bottom_widget import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy

class BottomWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    
    # 위젯 생성 및 표시
    widget = BottomWidget()
    widget.show()
    
    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
