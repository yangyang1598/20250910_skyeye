import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ui.ui_popup_patrol_dialog import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog

class PopupPatrolDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
def main():
    app = QApplication(sys.argv)
    dialog = PopupPatrolDialog()
    dialog.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()