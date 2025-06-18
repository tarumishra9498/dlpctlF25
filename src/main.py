from ALP4 import ALP4
import numpy as np
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from ui.ui_dlpctl import Ui_MainWindow

from image import ImageSeq


def rect_rotation_center(dmd: ALP4, framerate: int):
    """
    This function draws a rotating rectangle at `framerate` on the `dmd`

    Args:
        dmd: The DLP device/connection
        framerate: Framerate of animation, should not exceed 1000
    """
    # In milliseconds
    frametime = 1_000_000 / framerate

    dmd.SeqAlloc()
    dmd.SetTiming(pictureTime=frametime)

    frame_count = 358
    rect_image_seq = ImageSeq(200, 100, frame_count)

    blank_rect = np.zeros([rect_image_seq.width, rect_image_seq.height])

    rect_image_seq.image_data = [blank_rect]
    print(rect_image_seq.image_data)

    dmd.Run()
    input("Press Enter when done viewing animation")


class MainWindow(QMainWindow, Ui_MainWindow):
    dlp: ALP4 | None = None

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DLP Control")

        self.dlp = ALP4(version="4.1")
        self.dlp.Initialize()

    def __del__(self) -> None:
        if self.dlp:
            self.dlp.Halt()
            self.dlp.Free()


# TODO: Actually test this code on a Windows device
if __name__ == "__main__":
    app = None
    if not QtWidgets.QApplication.instance():
        QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()

    window = MainWindow()

    window.show()
    if app:
        app.exec()
