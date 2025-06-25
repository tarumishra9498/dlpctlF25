from PySide6.QtCore import QTimer
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from ui.ui_dlpctl import Ui_MainWindow

from camera import Camera

if sys.platform == "win32":
    from dlp import DLP
else:
    from dlp import MockDLP as DLP

from exception import DlpctlException


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DLP Control")

        self.camera: Camera | None
        self.pushButton.clicked.connect(self.connect_camera)

        self.dlp: DLP | None
        self.pushButton_2.clicked.connect(self.connect_dlp)

    def connect_camera(self):
        try:
            self.camera = Camera()
        except DlpctlException as e:
            self.camera = None
            print(e)

    def connect_dlp(self):
        try:
            self.dlp = DLP()
        except DlpctlException as e:
            print(e)
            self.dlp = None


if __name__ == "__main__":
    app = None
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    window = MainWindow()

    window.show()
    if app:
        app.exec()
