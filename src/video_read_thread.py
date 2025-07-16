from PySide6.QtCore import QMutexLocker, QThread, Signal, Slot
import cv2 as cv
import time
import numpy as np

from frame_analysis import frame_analysis


class VideoReadThread(QThread):
    FrameUpdate = Signal(object)

    def __init__ (
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
        self.local_kalman_filters = []
        self.paused = False
        self.display_fps = 30.0


    def run(self):
        cap = cv.VideoCapture(self.path)
        if not cap.isOpened():
            print("could not open video file; check the path & codec support")
            return
        cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)


        tick_freq = cv.getTickFrequency()
        fps_tick = 0
        last_tick = 0
        display_time = 1.0 / self.display_fps
        frame_time = 1.0 / cap.get(cv.CAP_PROP_FPS)

        while self.running:
            while self.paused and self.running:
                time.sleep(0.01)

            start_tick = cv.getTickCount()
            ret, frame = cap.read()
            if not ret:
                break
                with QMutexLocker(self.circles_mutex):
                    self.circles.clear()
                self.local_kalman_filters.clear()
                cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)
                ret, frame = cap.read()
                continue

            current_tick = cv.getTickCount()
            if fps_tick == 0:
                fps_tick = current_tick
            if last_tick == 0:
                last_tick = current_tick
            delta = current_tick - last_tick
            fps = tick_freq / delta if delta > 0 else 0.0
            last_tick = current_tick

            if (current_tick - fps_tick) / tick_freq >= display_time:
                fps_tick = current_tick

                with QMutexLocker(self.settings_mutex):
                    local_settings = dict(self.settings)
                    selections_copy = list(self.settings["selected_circles"])
                local_settings["selected_circles"] = selections_copy
                with QMutexLocker(self.circles_mutex):
                    local_circles = list(self.circles)

                local_settings["fps"] = fps
                try:
                    updated_frame, updated_circles, updated_kfs, updated_frame_pos = frame_analysis(
                        frame,
                        local_settings,
                        local_circles,
                        self.local_kalman_filters,
                        cap.get(cv.CAP_PROP_POS_FRAMES),
                    )
                except Exception as e:
                    print(e)
                    continue

                self.FrameUpdate.emit(updated_frame)
                self.update_circles(updated_circles)
                self.local_kalman_filters = updated_kfs

            proc_ticks = cv.getTickCount() - start_tick
            proc_secs  = proc_ticks / tick_freq
            time.sleep(max(frame_time - proc_secs, 0))
        
        cap.release()

    def update_circles(self, circles):
        with QMutexLocker(self.circles_mutex):
            self.circles.clear()
            self.circles.extend(circles)

    @Slot(bool)
    def on_pause(self, do_pause):
        self.paused = do_pause

    def stop(self):
        self.running = False
