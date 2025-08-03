import sys
from functools import partial

from PySide6 import QtWidgets
from PySide6.QtCore import QMutex, QMutexLocker, Qt, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import (
    QFileDialog,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
)

import cv2 as cv
import numpy as np

from pyvisa import ResourceManager
from pyvisa.resources import USBInstrument

from function_generator import FunctionGenerator
from ui.ui_dlpctl import Ui_MainWindow

from camera_thread import CameraThread
from video_write_thread import VideoWriteThread
from dlp_thread import DlpThread
from video_read_thread import VideoReadThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("DLP Control")

        self.blur = 7
        self.adapt_area = 61
        self.adapt_c = 13
        self.min_area = 70
        self.circularity = 0.7
        self.min_pos_err = 5

        self.source = None
        self.analysis_on = False
        self.filters_on = False
        self.blur_on = True
        self.thresh_on = True
        self.contour_on = True
        self.tracking_on = True
        self.selection_on = False
        self.pid_on = False

        self.camera_data = []

        self.camera_data_mutex = QMutex()
        self.settings_mutex = QMutex()
        self.circles_mutex = QMutex()
        self.selected_circles_mutex = QMutex()
        self.frame_pos_mutex = QMutex()
        self.paused_mutex = QMutex()

        self.settings = {
            "source": self.source,
            "analysis_on": self.analysis_on,
            "filters_on": self.filters_on,
            "blur": self.blur,
            "adapt_area": self.adapt_area,
            "adapt_c": self.adapt_c,
            "min_area": self.min_area,
            "circularity": self.circularity,
            "min_pos_err": self.min_pos_err,
            "blur_on": self.blur_on,
            "thresh_on": self.thresh_on,
            "contour_on": self.contour_on,
            "tracking_on": self.tracking_on,
            "selection_on": self.selection_on,
            "pid_on": self.pid_on,
            "video_frame_h": 0,
            "video_frame_w": 0,
            "pixmap_h": 0,
            "pixmap_w": 0,
            "fps": 0,
            "video_iteration": 0,
            "freq" : 0,
            "waveform" : None,
            "vpp" : 0,
            "vdc" : 0,
        }

        self.frame_pos = 0
        self.circles = {}
        self.selected_circles = []
        self.opened_files = []

        self.camera: CameraThread = CameraThread()
        self.pushButton.clicked.connect(self.connect_camera)
        self.pushButton.clicked.connect(self.read_video)

        self.video_writer: VideoWriteThread = VideoWriteThread()

        self.dlp: DlpThread = DlpThread()
        self.pushButton_2.clicked.connect(self.connect_dlp)

        self.exposure_slider.sliderReleased.connect(self.exposure_slider_changed)
        self.exposure_spinbox.valueChanged.connect(self.exposure_slider.setValue)

        self.function_generator: FunctionGenerator = FunctionGenerator()
        self.waveform_combobox.activated.connect(self.update_waveform)

        self.freq_slider.valueChanged.connect(self.freq_spinbox.setValue)
        self.freq_slider.valueChanged.connect(self.update_freq)
        self.freq_spinbox.valueChanged.connect(self.freq_slider.setValue)
        self.freq_spinbox.valueChanged.connect(self.update_freq)

        self.amp_slider.valueChanged.connect(partial(self.update_voltage, "vpp", "slider"))
        self.amp_spinbox.valueChanged.connect(partial(self.update_voltage, "vpp", "spinbox"))

        self.offset_voltage_slider.valueChanged.connect(partial(self.update_voltage, "vdc", "slider"))
        self.offset_voltage_spinbox.valueChanged.connect(partial(self.update_voltage, "vdc", "spinbox"))


        self.rm = ResourceManager()
        self.refresh_devices.clicked.connect(self.refresh_devices_clicked)
        # key: resource name, value: (idn, list_item, list_widget)
        self.visa_insts: dict[
            str, tuple[str, QListWidgetItem | None, QPushButton | None]
        ] = {}

        self.load_bitmask.setEnabled(False)
        self.load_bitmask.pressed.connect(self.on_load_bitmask)
        self.capture.setEnabled(False)
        self.capture.pressed.connect(self.on_capture)

        self.analysis_button.setChecked(self.analysis_on)
        self.analysis_button.clicked.connect(self.checked_analysis)

        self.show_filters.setChecked(self.filters_on)
        self.show_filters.clicked.connect(self.checked_filters)

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

        self.circularity_spinbox.setValue(self.circularity)
        self.circularity_spinbox.valueChanged.connect(self.update_circularity)

        self.tracking_min_error_spinbox.setValue(self.min_pos_err)
        self.tracking_min_error_spinbox.valueChanged.connect(self.update_min_pos_err)

        self.blur_checkbox.setChecked(self.blur_on)
        self.thresh_checkbox.setChecked(self.thresh_on)
        self.contour_checkbox.setChecked(self.contour_on)
        self.tracking_checkbox.setChecked(self.tracking_on)
        self.selection_checkbox.setChecked(self.selection_on)
        self.pid_checkbox.setChecked(self.pid_on)

        self.blur_checkbox.stateChanged.connect(self.checked_blur)
        self.thresh_checkbox.stateChanged.connect(self.checked_thresh)
        self.contour_checkbox.stateChanged.connect(self.checked_contour)
        self.tracking_checkbox.stateChanged.connect(self.checked_tracking)
        self.selection_checkbox.stateChanged.connect(self.checked_selection)
        self.pid_checkbox.stateChanged.connect(self.checked_pid)

        self.clear_all.pressed.connect(self.clear_all_bubbles)

        self.actionOpen.triggered.connect(self.on_open)
        self.ReadThread = VideoReadThread(
            None, None, None, None, None, None, None, None, None, None, None, None
        )
        self.play.clicked.connect(lambda: self.ReadThread.on_pause(False))
        self.pause.clicked.connect(lambda: self.ReadThread.on_pause(True))
        self.replay.clicked.connect(lambda: self.on_replay(True))

        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)
        self.video_frame.setMouseTracking(True)
        self.video_frame.clicked.connect(self.on_video_click)
        self.video_frame.moved.connect(self.on_mouse_move)

    def on_camera_frame(self, data):
        self.ReadThread.update_camera_frame(data)

    def refresh_devices_clicked(self):
        # Clear out visa instruments from list
        for inst in self.visa_insts.values():
            li = inst[1]  # list item
            lw = inst[2]  # list widget
            if li and lw:
                row = self.device_list.row(li)
                self.device_list.takeItem(row)
                del li
                lw.close()

        print("Refreshing device list")
        resources = self.rm.list_resources()
        for i, resource in enumerate(resources):
            try:
                with self.rm.open_resource(resource) as instrument:
                    print(f"instrument {i} detected of type {type(instrument)}")
                    if isinstance(instrument, USBInstrument):
                        idn = instrument.query("*IDN?").strip()
                        list_item = QListWidgetItem(self.device_list)
                        list_button = QPushButton(f"{instrument.model_name}")

                        self.visa_insts[resource] = (idn, list_item, list_button)
                        self.device_list.addItem(list_item)
                        self.device_list.setItemWidget(list_item, list_button)

                        if "Waveform Generator" in instrument.model_name:
                            list_button.clicked.connect(
                                partial(self.connect_function_generator_clicked, resource)
                            )
            except Exception as e:
                print(e)
                self.visa_insts[resource] = ("VISA Device (No IDN)", None, None)
        print(f"VISA devices detected: {self.visa_insts}")

    def exposure_slider_changed(self):
        self.camera.set_exposure(self.exposure_slider.value())
        self.exposure_spinbox.setValue(self.exposure_slider.value())

    def connect_function_generator_clicked(self, idn: str):
        self.function_generator.select_instrument(self.rm, idn)
    

    def update_waveform(self):
        commands = {
            "Sine" : "SIN",
            "Square" : "SQU",
            "Ramp" : "RAMP",
            "Pulse" : "PULS",
            "Noise" : "NOIS"
         
        }
        command_str = self.waveform_combobox.currentText()
        if command_str in commands:
            self.function_generator.set_function(commands[command_str])
            self.update_settings("waveform", commands[command_str])

    def update_freq(self, val):
        units = {
            "MHz" : 1e6,
            "kHz" : 1e3,
            "Hz" : 1,
            "mHz" : 1e-3,
            "uHz" : 1e-6
        }

        val *= units[self.freq_combo_box.currentText()]
        if val < 100 * 1e-6:
            print("Frequency too low, min frequency: 100 uHz")
        if val > 10 * 1e6:
            print("Frequency too high, max frequency: 10 MHz")
        else:
            self.function_generator.set_frequency(int(val))

        self.update_settings("freq", int(val))

    # def update_voltage(self, voltage_type: str, source: str, val: float):
    #     units = {
    #         "Vpp" : 1,
    #         "Vdc" : 1,
    #         "mVpp" : 1e-3,
    #         "mVdc" : 1e-3
    #     }
        
    #     if source == "spinbox":
    #         if voltage_type == "vpp":
    #             val *= units[self.amp_combo_box.currentText()]
    #             print(val)
    #             self.function_generator.set_voltage(val, "vpp")
    #             self.update_settings("vpp", val)
    #             self.amp_slider.setValue(int(val))
    #         else:
    #             val *= units[self.offset_voltage_combo_box.currentText()]
    #             print(val)
    #             self.function_generator.set_voltage(val, "vdc")
    #             self.update_settings("vdc", val)
    #             self.offset_voltage_slider.setValue(int(val))
    #     else:
    #         if voltage_type == "vpp":
    #             self.function_generator.set_voltage(val, "vpp")
    #             self.update_settings("vpp", val)
    #             self.amp_spinbox.setValue(int(val))
    #         else:
    #             self.function_generator.set_voltage(val, "vdc")
    #             self.update_settings("vdc", val)
    #             self.offset_voltage_spinbox.setValue(int(val))

    def update_voltage(self, voltage_type: str, source: str, val: float):
        units = {
            "Vpp": 1,
            "Vdc": 1,
            "mVpp": 1e-3,
            "mVdc": 1e-3,
        }

        cfg = {
            "vpp": {
                "unit_widget": self.amp_combo_box,
                "slider": self.amp_slider,
                "spinbox": self.amp_spinbox,
            },
            "vdc": {
                "unit_widget": self.offset_voltage_combo_box,
                "slider": self.offset_voltage_slider,
                "spinbox": self.offset_voltage_spinbox,
            },
        }[voltage_type]

        if source == "spinbox":
            cfg["slider"].setValue(int(val))
        else:
            cfg["spinbox"].setValue(int(val))
        
        factor = units[cfg["unit_widget"].currentText()]
        val = val * factor

        self.function_generator.set_voltage(val, voltage_type)
        self.update_settings(voltage_type, val)

    def connect_camera(self):
        if not self.camera.basler:
            if self.camera.open():
                self.camera.start()
                self.capture.setEnabled(True)
                self.pushButton.setStyleSheet("color: green;")
                self.camera.frame_out.connect(self.video_writer.save_frame)
                self.camera.display_out.connect(self.update_display)
                self.camera.display_out.connect(self.on_camera_frame)
                self.update_settings("source", "camera")
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

        bitmask = cv.imread(filename, cv.IMREAD_GRAYSCALE)

        self.dlp.img = bitmask
        self.dlp.run()

    def on_open(self):
        self.update_settings("source", "video")
        self.read_video()

    def update_display(self, data):
        q_img = None

        # reading from file
        if isinstance(data, np.ndarray):
            rgb = cv.cvtColor(data, cv.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            q_img = QImage(rgb.data, w, h, ch * w, QImage.Format.Format_RGB888)

        # reading from camera
        # this should be deleted since video_read_thread will always output a numpy array
        else:
            frame, current_fps, exposure, recording_state = data
            h, w = frame.shape
            channels = 1
            q_img = QImage(
                frame.data, w, h, channels * w, QImage.Format.Format_Grayscale8
            )
        pixmap = QPixmap.fromImage(q_img).scaled(
            self.video_frame.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.video_frame.setPixmap(pixmap)
        self.update_settings("pixmap_w", pixmap.width())
        self.update_settings("pixmap_h", pixmap.height())

    def on_replay(self, val):
        if val:
            if self.ReadThread and self.ReadThread.isRunning():
                self.ReadThread.stop()
                self.ReadThread.wait()  # try removing these calls

            with QMutexLocker(self.circles_mutex):
                self.circles.clear()

            self.ReadThread = VideoReadThread(
                self.opened_files[-1],
                self.camera_data,
                self.camera_data_mutex,
                self.settings,
                self.settings_mutex,
                self.circles,
                self.circles_mutex,
                self.selected_circles,
                self.selected_circles_mutex,
                self.frame_pos,
                self.frame_pos_mutex,
                self.function_generator
            )
            self.ReadThread.FrameUpdate.connect(self.update_display)
            # look into this

            # self.ReadThread.FrameUpdate.connect(self.video_writer.save_frame)
            self.ReadThread.start()

    def update_min_pos_err(self, val):
        self.update_settings("min_pos_err", val)

    def clear_all_bubbles(self):
        with QMutexLocker(self.selected_circles_mutex):
            self.selected_circles.clear()

    def read_video(self):
        file = None
        if self.settings["source"] == "video":
            file_dialog = QFileDialog(self)
            file_dialog.setWindowTitle("Open File")
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            file_dialog.setViewMode(QFileDialog.ViewMode.Detail)

            if file_dialog.exec():
                files = file_dialog.selectedFiles()
                self.opened_files.append(files[0])
                file = self.opened_files[-1]
            self.update_settings("source", "video")
            self.video_frame.setText("Video Opened")

        if self.ReadThread is not None and self.ReadThread.isRunning():
            self.ReadThread.stop()
            self.ReadThread.wait()

        print("video thread activated")
        self.ReadThread = VideoReadThread(
            file,
            self.camera_data,
            self.camera_data_mutex,
            self.settings,
            self.settings_mutex,
            self.circles,
            self.circles_mutex,
            self.selected_circles,
            self.selected_circles_mutex,
            self.frame_pos,
            self.frame_pos_mutex,
            self.function_generator
        )

        self.ReadThread.FrameUpdate.connect(self.update_display)
        self.ReadThread.start()

    def showEvent(self, event):
        self.update_settings("video_frame_w", self.video_frame.width())
        self.update_settings("video_frame_h", self.video_frame.height())

    def closeEvent(self, event):
        self.camera.stop_recording()
        self.camera.close()
        self.camera.stop()
        self.camera.wait(1000)
        self.video_writer.stop()
        self.video_writer.wait()
        self.dlp.stop()
        self.dlp.wait()

        if self.ReadThread:
            self.ReadThread.stop()
            self.ReadThread.wait()
        super().closeEvent(event)

    def on_video_click(self, x, y):
        x -= (self.settings["video_frame_w"] - self.settings["pixmap_w"]) // 2
        y -= (self.settings["video_frame_h"] - self.settings["pixmap_h"]) // 2
        with QMutexLocker(self.selected_circles_mutex):
            if self.selected_circles_mutex == [False]:
                self.selected_circles = []
            self.selected_circles.append([x, y])

    def on_mouse_move(self, x, y):
        x -= (self.settings["video_frame_w"] - self.settings["pixmap_w"]) // 2
        y -= (self.settings["video_frame_h"] - self.settings["pixmap_h"]) // 2
        self.mouse_pos.setText(f"Frame Position (x, y): {x}, {y}")

    def update_settings(self, name, value):
        with QMutexLocker(self.settings_mutex):
            self.settings[name] = value

    def checked_analysis(self):
        self.update_settings("analysis_on", self.analysis_button.isChecked())
        if self.analysis_button.isChecked():
            self.analysis_button.setText("Analysis On")
        else:
            self.analysis_button.setText("Analysis Off")

    def checked_filters(self):
        self.update_settings("filters_on", self.show_filters.isChecked())

    def checked_blur(self):
        self.update_settings("blur_on", self.blur_checkbox.isChecked())

    def checked_thresh(self):
        self.update_settings("thresh_on", self.thresh_checkbox.isChecked())

    def checked_contour(self):
        self.update_settings("contour_on", self.contour_checkbox.isChecked())

    def checked_tracking(self):
        self.update_settings("tracking_on", self.tracking_checkbox.isChecked())

    def checked_selection(self):
        self.update_settings("selection_on", self.selection_checkbox.isChecked())
        update = self.selection_checkbox.isChecked()
        if update:
            update = []
        else:
            update = [False]
        self.update_settings("selected_circles", update)

    def checked_pid(self):
        self.update_settings("pid_on", self.pid_checkbox.isChecked())

    def update_blur(self, val):
        if val % 2 == 0:
            val += 1
        self.update_settings("blur", val)

    def update_adapt_area(self, val):
        if val % 2 == 0:
            val += 1
        self.update_settings("adapt_area", val)

    def update_adapt_c(self, val):
        self.update_settings("adapt_c", val)

    def update_min_area(self, val):
        self.update_settings("min_area", val)

    def update_circularity(self, val):
        self.update_settings("circularity", val)


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
