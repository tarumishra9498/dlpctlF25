from PySide6.QtCore import QMutexLocker, QThread, Signal, Slot
import cv2 as cv
import time

from frame_analysis import frame_analysis


class VideoReadThread(QThread):
    FrameUpdate = Signal(object)

    def __init__(
        self,
        path,
        settings,
        settings_mutex,
        circles,
        circles_mutex,
        frame_start,
        frame_pos_mutex,
    ):
        super().__init__()
        self.path = path
        self.settings = settings
        self.circles = circles
        self.settings_mutex = settings_mutex
        self.circles_mutex = circles_mutex
        self.running = True
        self.frame_start = frame_start
        self.frame_pos_mutex = frame_pos_mutex
        self.paused = False

    def run(self):
        cap = cv.VideoCapture(self.path)

        if not cap.isOpened():
            print("could not open video file; check the path & codec support")
            return

        cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)
        fps = cap.get(cv.CAP_PROP_FPS)
        frame_delay = 1 / fps

        while self.running:
            if self.paused:
                continue

            with QMutexLocker(self.settings_mutex):
                local_settings = dict(self.settings)
            with QMutexLocker(self.circles_mutex):
                local_circles = list(self.circles)

            ret, frame = cap.read()
            if ret:
                updated_frame, updated_circles, updated_frame_pos = frame_analysis(
                    frame,
                    local_settings,
                    local_circles,
                    cap.get(cv.CAP_PROP_POS_FRAMES),
                )
                self.FrameUpdate.emit(updated_frame)
                time.sleep(frame_delay)
                self.update_circles(updated_circles)
                # self.update_frame_pos(updated_frame_pos)
            else:
                break

        cap.release()

    def update_circles(self, circles):
        with QMutexLocker(self.circles_mutex):
            self.circles.clear()
            self.circles = circles

    @Slot(bool)
    def on_pause(self, do_pause):
        self.paused = do_pause

    def stop(self):
        self.running = False
        self.wait()
