import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow

from image import ImageSeq
from ui.ui_dlpctl import Ui_MainWindow

from camera_thread import CameraThread
from video_write_thread import VideoWriteThread

from dlp_thread import DlpThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DLP Control")

        self.camera: CameraThread = CameraThread()
        self.pushButton.clicked.connect(self.connect_camera)

        self.video_writer: VideoWriteThread = VideoWriteThread()

        self.dlp: DlpThread = DlpThread()
        self.pushButton_2.clicked.connect(self.connect_dlp)

        self.bitmask: ImageSeq | None = None
        self.load_bitmask.setEnabled(False)
        self.load_bitmask.pressed.connect(self.on_load_bitmask)

        self.capture.setEnabled(False)
        self.capture.pressed.connect(self.on_capture)

    def connect_camera(self):
        if not self.camera.basler:
            if self.camera.open():
                self.camera.start()
                self.capture.setEnabled(True)
                self.pushButton.setStyleSheet("color: green;")
                self.camera.frame_out.connect(self.video_writer.save_frame)
                self.camera.display_out.connect(self.update_display)
            else:
                self.capture.setEnabled(False)
                self.pushButton.setStyleSheet("")
                print("Could not connect to camera")
        else:
            self.camera.stop_recording()
            self.camera.stop_grabbing()
            self.camera.close()
            self.capture.setEnabled(False)
            self.pushButton.setStyleSheet("")

    def connect_dlp(self):
        if not self.dlp.connected:
            if self.dlp.open():
                self.pushButton_2.setStyleSheet("color: green;")
                self.load_bitmask.setEnabled(True)
            else:
                self.pushButton_2.setStyleSheet("")
                self.load_bitmask.setEnabled(False)

    def on_capture(self):
        if not self.camera.recording:
            self.capture.setStyleSheet("color: green;")
            self.camera.start_recording()
        else:
            self.camera.stop_recording()
            self.capture.setStyleSheet("")
            print("stopping capture, saved to output.mp4")

    def on_load_bitmask(self):
        if self.bitmask is None:
            print("opening file picker")
            filename = QFileDialog.getOpenFileName(
                self.load_bitmask,
                "Open bitmask",
                "",
                ("Image Files (*.png *.jpg *.bmp"),
            )[0]
            print(filename)

    def closeEvent(self, _):
        self.camera.stop_recording()
        self.video_writer.stop()

    def update_display(self, data):
        print("updating display")
        if self.camera:
            frame, current_fps, exposure, recording_state = data
            h, w = frame.shape
            channels = 1
            q_img = QImage(
                frame.data, w, h, channels * w, QImage.Format.Format_Grayscale8
            )
            pixmap = QPixmap.fromImage(q_img)
            self.video_frame.setPixmap(pixmap)


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
