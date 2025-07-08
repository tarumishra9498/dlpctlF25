from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
import cv2 as cv
import time

class VideoReadThread(QThread):
    FrameUpdate = Signal(object)

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.running = True

    def run(self):
        cap = cv.VideoCapture(self.path)
        fps = cap.get(cv.CAP_PROP_FPS)
        print(fps)
        frame_delay = 1 / fps

        while self.running:
            ret, frame = cap.read()
            if ret:
                self.FrameUpdate.emit(frame)
                time.sleep(frame_delay)
            else:
                break

    def stop(self):
        self.running = False
        self.wait()
