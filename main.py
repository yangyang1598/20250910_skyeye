import sys, os
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEngineSettings

class MapApp(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        path = os.path.abspath("map.html")  # 현재 실행 디렉토리에서 map.html 절대경로
        self.load(QUrl.fromLocalFile(path))
        self.loadFinished.connect(self.on_load_finished)
        self.show()

    def on_load_finished(self, ok):
        if ok:
            print("✅ HTML 로딩 완료!")
        else:
            print("❌ HTML 로딩 실패")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    sys.exit(app.exec())