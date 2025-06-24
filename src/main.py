from PySide6.QtCore import QTimer
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from ui.ui_dlpctl import Ui_MainWindow

from camera import Camera
from image import ImageSeq
from dlp import DLP


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DLP Control")

        # TODO: Make it possible to reconnect in UI without restarting app
        self.dlp = DLP()

        # TODO: Make it possible to reconnect in UI without restarting app
        self.camera = Camera()


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
