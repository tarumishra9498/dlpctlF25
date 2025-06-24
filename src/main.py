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

        self.dlp: DLP | None
        self.camera: Camera | None

        # TODO: Make it possible to reconnect in UI without restarting app

        try:
            self.dlp = DLP()
        except DlpctlException as e:
            print(e)
            self.dlp = None

        try:
            self.camera = Camera()
        except DlpctlException as e:
            print(e)
            self.camera = None


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
