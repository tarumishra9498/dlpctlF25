from PySide6.QtCore import QMutexLocker, QThread, Signal
import cv2 as cv
import time

from frame_analysis import frame_analysis

class VideoReadThread(QThread):
    FrameUpdate = Signal(object)

    def __init__(self, path, settings, settings_mutex, circles, circles_mutex):
        super().__init__()
        self.path = path
        self.settings = settings
        self.circles = circles
        self.settings_mutex = settings_mutex
        self.circles_mutex = circles_mutex
        self.running = True

    def run(self):
        cap = cv.VideoCapture(self.path)
        fps = cap.get(cv.CAP_PROP_FPS)
        frame_delay = 1 / fps

        if not cap.isOpened():
            print("could not open video file; check the path & codec support")
            return

        while self.running:
            with QMutexLocker(self.settings_mutex):
                local_settings = dict(self.settings)
            with QMutexLocker(self.circles_mutex):
                local_circles = list(self.circles)

            ret, frame = cap.read()
            frame_pos = 1
            
            if ret:
                updated_frame, updated_circles = frame_analysis(frame, local_settings, local_circles, frame_pos)
                self.FrameUpdate.emit(updated_frame)
                time.sleep(frame_delay)
                self.update_circles(updated_circles)

            else:
                break
            frame_pos += 1
        print(self.circles)
        cap.release()
    
    def update_circles(self, circles):
        with QMutexLocker(self.circles_mutex):
            self.circles.clear()
            self.circles.append(circles)

    def stop(self):
        self.running = False
        self.wait()
