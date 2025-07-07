from PySide6.QtCore import QThread, Slot
import cv2 as cv

class VideoReadThread(QThread):
    def __init__(self, path):
        super().__init__()
        self.path = path
    def run(self):
        cap = cv.VideoCapture(self.path)
        while cap.get(cv.CAP_PROP_POS_FRAMES) != cap.get(cv.CAP_PROP_FRAME_COUNT):
            ret, frame = cap.read()
            

    def stop(self):
        self.quit()
        self.wait()
    
