from PySide6.QtCore import QMutexLocker, QThread, Signal, Slot
import cv2 as cv
import time
import numpy as np
import copy

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
        selected_circles,
        selected_circles_mutex,
        frame_start,
        frame_pos_mutex,
    ):
        super().__init__()
        self.path = path
        self.settings = settings
        self.circles = circles
        self.settings_mutex = settings_mutex
        self.circles_mutex = circles_mutex
        self.selected_circles = selected_circles
        self.selected_circles_mutex = selected_circles_mutex
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

        frame_analysis_iteration = 1
        video_iteration = 1
        first_frame_shown = False
        tick_freq = cv.getTickFrequency()
        fps_tick = 0
        last_tick = 0
        display_time = 1.0 / self.display_fps
        frame_time = 1.0 / cap.get(cv.CAP_PROP_FPS)

        with QMutexLocker(self.circles_mutex):
            self.circles.clear()
        
        with QMutexLocker(self.selected_circles_mutex):
            self.selected_circles.clear()
        
        while self.running:
            while self.paused and self.running:
                time.sleep(0.01)
            start_tick = cv.getTickCount()
            ret, frame = cap.read()
            if not ret:

                with QMutexLocker(self.circles_mutex):
                    self.circles.clear()
                self.local_kalman_filters.clear()
                with QMutexLocker(self.settings_mutex):
                    local_settings = self.settings.copy()
                
                cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)
                time.sleep(.01)
                video_iteration += 1
                frame_analysis_iteration += 1
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
                    local_settings = self.settings.copy()
                local_settings["video_iteration"] = video_iteration

                with QMutexLocker(self.circles_mutex):
                    local_circles = self.circles.copy()

                with QMutexLocker(self.selected_circles_mutex):
                    local_selected_circles = self.selected_circles.copy()

                local_settings["fps"] = fps

                if frame_analysis_iteration == 1:
                    self.frame_start = cap.get(cv.CAP_PROP_POS_FRAMES)
                    # print(f"starting frame {self.frame_start}")

                try:
                    updated_frame, updated_circles, updated_kfs, = frame_analysis(
                        frame,
                        local_settings,
                        local_circles,
                        local_selected_circles,
                        self.local_kalman_filters,
                        cap.get(cv.CAP_PROP_POS_FRAMES),
                        self.frame_start,
                    )

                    # print("Frame analysis succeeded")

                    self.FrameUpdate.emit(updated_frame)

                    # print("Frame emit succeeded")

                    self.update_circles(updated_circles)
                    self.local_kalman_filters = updated_kfs
                    
                    
                except Exception as e:
                    print(f"Frame analysis failed: {e}")
                    break
                
                frame_analysis_iteration += 1

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
