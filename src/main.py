from PySide6.QtCore import QTimer
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from ui.ui_dlpctl import Ui_MainWindow

from camera import Camera
from image import ImageSeq
from dlp import DLP
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
            print("Camera successfully connected")
        except DlpctlException:
            self.camera = None
            print("Could not connect to Camera")

    def connect_dlp(self):
        try:
            self.dlp = DLP()
            print("DLP successfully connected")
        except DlpctlException:
            print("Could not connect to DLP")
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
