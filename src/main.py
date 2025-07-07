import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QImageReader, QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow, QCheckBox, QDoubleSpinBox, QSpinBox

import cv2

import numpy as np

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

        self.capture.setEnabled(False)
        self.capture.pressed.connect(self.on_capture)

        self.blur = 5
        self.adapt_area = 60
        self.adapt_c = 13
        self.min_area = 25 
        self.circularity = 0.7
        self.min_pos_err = 5 

        self.blur_on = True
        self.thresh_on = True
        self.contours_on = True
        self.tracking_on = True

        self.horizontalSlider_7.setValue(self.blur)
        self.spinBox.setValue(self.blur)
        self.horizontalSlider_7.valueChanged.connect(self.update_blur)
        self.horizontalSlider_7.valueChanged.connect(self.spinBox.setValue)
        self.spinBox.valueChanged.connect(self.update_blur)
        self.spinBox.valueChanged.connect(self.horizontalSlider_7.setValue)

        self.horizontalSlider_2.setValue(self.adapt_area)
        self.spinBox_2.setValue(self.adapt_area)
        self.horizontalSlider_2.valueChanged.connect(self.update_adapt_area)
        self.horizontalSlider_2.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox_2.valueChanged.connect(self.update_adapt_area)
        self.spinBox_2.valueChanged.connect(self.horizontalSlider_2.setValue)

        self.horizontalSlider_3.setValue(self.adapt_c)
        self.spinBox_3.setValue(self.adapt_c)
        self.horizontalSlider_3.valueChanged.connect(self.update_adapt_c)
        self.horizontalSlider_3.valueChanged.connect(self.spinBox_3.setValue)
        self.spinBox_3.valueChanged.connect(self.update_adapt_c)
        self.spinBox_3.valueChanged.connect(self.horizontalSlider_3.setValue)

        self.horizontalSlider_4.setValue(self.min_area)
        self.spinBox_4.setValue(self.min_area)
        self.horizontalSlider_4.valueChanged.connect(self.update_min_area)
        self.horizontalSlider_4.valueChanged.connect(self.spinBox_4.setValue)
        self.spinBox_4.valueChanged.connect(self.update_min_area)
        self.spinBox_4.valueChanged.connect(self.horizontalSlider_4.setValue)

        self.horizontalSlider_5.setValue(int(self.circularity))
        self.doubleSpinBox.setValue(self.circularity)
        self.horizontalSlider_5.valueChanged.connect(self.update_circularity)
        self.horizontalSlider_5.valueChanged.connect(self.doubleSpinBox.setValue)
        self.doubleSpinBox.valueChanged.connect(self.update_circularity)
        self.doubleSpinBox.valueChanged.connect(self.horizontalSlider_5.setValue)

        self.horizontalSlider_6.setValue(int(self.min_pos_err))
        self.doubleSpinBox_2.setValue(self.min_pos_err)
        self.horizontalSlider_6.valueChanged.connect(self.update_min_pos_err)
        self.horizontalSlider_6.valueChanged.connect(self.doubleSpinBox_2.setValue)
        self.doubleSpinBox_2.valueChanged.connect(self.update_min_pos_err)
        self.doubleSpinBox_2.valueChanged.connect(self.horizontalSlider_6.setValue)

        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        self.checkBox.stateChanged.connect(self.checked_blur)
        self.checkBox_2.stateChanged.connect(self.checked_thresh)
        self.checkBox_3.stateChanged.connect(self.checked_contour)
        self.checkBox_4.stateChanged.connect(self.checked_tracking)

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
            else:
                self.pushButton_2.setStyleSheet("")

    def on_capture(self):
        if not self.camera.recording:
            self.capture.setStyleSheet("color: green;")
            self.camera.start_recording()
        else:
            self.camera.stop_recording()
            self.capture.setStyleSheet("")
            print("stopping capture, saved to output.mp4")

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

    def checked_blur(self):
        if self.checkBox.isChecked():
            self.blur_on = True
        else:
            self.blur_on = False

    def checked_thresh(self):
        if self.checkBox_2.isChecked():
            self.thresh_on = True
        else:
            self.thresh_on = False
    
    def checked_contour(self):
        if self.checkBox_3.isChecked():
            self.contours_on = True
        else:
            self.contours_on = False
    
    def checked_tracking(self):
        if self.checkBox_4.isChecked():
            self.tracking_on = True
        else:
            self.tracking_on = False

    def update_blur(self, val):
        if val % 2 == 0:
            val += 1
        self.blur = val

    def update_adapt_area(self, val):
        if val % 2 == 0:
            val += 1
        self.adapt_area = val

    def update_adapt_c(self, val):
        self.adapt_c = val

    def update_min_area(self, val):
        self.min_area = val

    def update_circularity(self, val):
        val = val / 100.0
        self.circularity = val
        print(val)

    def update_min_pos_err(self, val):
        self.min_pos_err = val

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



