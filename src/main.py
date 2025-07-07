import sys

from PySide6 import QtWidgets
from PySide6.QtGui import QImage, QImageReader, QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QCheckBox,
    QDoubleSpinBox,
    QSpinBox,
)

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

        self.load_bitmask.setEnabled(False)
        self.load_bitmask.pressed.connect(self.on_load_bitmask)
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

        self.blur_slider.setValue(self.blur)
        self.blur_spinbox.setValue(self.blur)
        self.blur_slider.valueChanged.connect(self.update_blur)
        self.blur_slider.valueChanged.connect(self.blur_spinbox.setValue)
        self.blur_spinbox.valueChanged.connect(self.update_blur)
        self.blur_spinbox.valueChanged.connect(self.blur_slider.setValue)

        self.thresh_area_slider.setValue(self.adapt_area)
        self.thresh_area_spinbox.setValue(self.adapt_area)
        self.thresh_area_slider.valueChanged.connect(self.update_adapt_area)
        self.thresh_area_slider.valueChanged.connect(self.thresh_area_spinbox.setValue)
        self.thresh_area_spinbox.valueChanged.connect(self.update_adapt_area)
        self.thresh_area_spinbox.valueChanged.connect(self.thresh_area_slider.setValue)

        self.thresh_const_slider.setValue(self.adapt_c)
        self.thresh_const_spinbox.setValue(self.adapt_c)
        self.thresh_const_slider.valueChanged.connect(self.update_adapt_c)
        self.thresh_const_slider.valueChanged.connect(
            self.thresh_const_spinbox.setValue
        )
        self.thresh_const_spinbox.valueChanged.connect(self.update_adapt_c)
        self.thresh_const_spinbox.valueChanged.connect(
            self.thresh_const_slider.setValue
        )

        self.contour_slider.setValue(self.min_area)
        self.contour_spinbox.setValue(self.min_area)
        self.contour_slider.valueChanged.connect(self.update_min_area)
        self.contour_slider.valueChanged.connect(self.contour_spinbox.setValue)
        self.contour_spinbox.valueChanged.connect(self.update_min_area)
        self.contour_spinbox.valueChanged.connect(self.contour_slider.setValue)

        self.circularity_slider.setValue(int(self.circularity))
        self.circularity_spinbox.setValue(self.circularity)
        self.circularity_slider.valueChanged.connect(self.update_circularity)
        self.circularity_slider.valueChanged.connect(self.circularity_spinbox.setValue)
        self.circularity_spinbox.valueChanged.connect(self.update_circularity)
        self.circularity_spinbox.valueChanged.connect(self.circularity_slider.setValue)

        self.circularity_slider.setValue(int(self.min_pos_err))
        self.tracking_min_error_spinbox.setValue(self.min_pos_err)
        self.circularity_slider.valueChanged.connect(self.update_min_pos_err)
        self.circularity_slider.valueChanged.connect(
            self.tracking_min_error_spinbox.setValue
        )
        self.tracking_min_error_spinbox.valueChanged.connect(self.update_min_pos_err)
        self.tracking_min_error_spinbox.valueChanged.connect(
            self.circularity_slider.setValue
        )

        self.blur_checkbox.setChecked(True)
        self.thresh_checkbox.setChecked(True)
        self.contour_checkbox.setChecked(True)
        self.tracking_checkbox.setChecked(True)
        self.blur_checkbox.stateChanged.connect(self.checked_blur)
        self.thresh_checkbox.stateChanged.connect(self.checked_thresh)
        self.contour_checkbox.stateChanged.connect(self.checked_contour)
        self.tracking_checkbox.stateChanged.connect(self.checked_tracking)

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
        filename = QFileDialog.getOpenFileName(
            self.load_bitmask,
            "Open bitmask",
            "",
            ("Image Files (*.png *.jpg *.bmp"),
        )[0]

        bitmask = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        w = bitmask.shape[0]
        h = bitmask.shape[1]
        arr = bitmask.ravel().reshape(w, h, 1)

        self.dlp.push(arr)
        self.dlp.run()

    def update_display(self, data):
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
        if self.blur_checkbox.isChecked():
            self.blur_on = True
        else:
            self.blur_on = False

    def checked_thresh(self):
        if self.thresh_checkbox.isChecked():
            self.thresh_on = True
        else:
            self.thresh_on = False

    def checked_contour(self):
        if self.contour_checkbox.isChecked():
            self.contours_on = True
        else:
            self.contours_on = False

    def checked_tracking(self):
        if self.tracking_checkbox.isChecked():
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

    def closeEvent(self, _):
        self.camera.stop_recording()
        self.video_writer.stop()


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
