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
        camera_data,
        camera_data_mutex,
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
        self.camera_data = []
        self.camera_data_mutex = camera_data_mutex
        self.settings = settings
        self.circles = circles
        self.settings_mutex = settings_mutex
        self.circles_mutex = circles_mutex
        self.selected_circles = selected_circles
        self.selected_circles_mutex = selected_circles_mutex
        self.running = False
        self.frame_start = frame_start
        self.frame_pos_mutex = frame_pos_mutex
        self.paused = False
        self.display_fps = 30.0
        self.bubble_counter_start = 1

    def run(self):
        while not(self.running):
            if self.settings["analysis_on"]:
                self.running = True
            time.sleep(0.1)

        frame_analysis_iteration = 1
        video_iteration = 1
        first_frame_shown = False
        tick_freq = cv.getTickFrequency()
        fps_tick = 0
        last_tick = 0
        display_time = 1.0 / self.display_fps
        cap = None
        frame_pos = 0

        with QMutexLocker(self.circles_mutex):
            self.circles.clear()
        
        with QMutexLocker(self.selected_circles_mutex):
            self.selected_circles.clear()
          
        if self.settings["source"] == "video":
            cap = cv.VideoCapture(self.path)
            if not cap.isOpened():
                print("Could not open video file; check the path & codec support")
                return
            cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)
        
        while self.running:
            while self.paused and self.running:
                time.sleep(0.01)

            start_tick = cv.getTickCount()
            
            # if the video is the source, read the frame
            if self.settings["source"] == "video" and cap:
                ret, frame = cap.read()
                if not ret:
                    with QMutexLocker(self.circles_mutex):
                        self.circles.clear()
                    self.bubble_counter_start = 1
                    cap.set(cv.CAP_PROP_POS_FRAMES, self.frame_start)
                    time.sleep(.01)
                    video_iteration += 1
                    frame_analysis_iteration += 1
                    continue
                    
                if frame_analysis_iteration == 1:
                    self.frame_start = cap.get(cv.CAP_PROP_POS_FRAMES)
                frame_pos = cap.get(cv.CAP_PROP_POS_FRAMES)
            
            # if the camera is the source, get the camera frame
            elif self.settings["source"] == "camera":
                frame, camera_fps, exposure, recording_state = self.camera_data
                # don't change frame_start
                frame_pos += 1
                print("camera frame grabbed")

            else:
                print("Source not found")
                break

            # none of these depend on the frame source
            current_tick = cv.getTickCount()
            if fps_tick == 0:
                fps_tick = current_tick
            if last_tick == 0:
                last_tick = current_tick
            delta = current_tick - last_tick
            fps = tick_freq / delta if delta > 0 else 0.0
            last_tick = current_tick
            fps_tick = current_tick


            with QMutexLocker(self.settings_mutex):
                local_settings = self.settings.copy()
            local_settings["video_iteration"] = video_iteration

            if self.settings["source"] == "video":
                local_settings["fps"] = fps
            else:
                local_settings["fps"] = camera_fps

            with QMutexLocker(self.circles_mutex):
                local_circles = self.circles.copy()
            with QMutexLocker(self.selected_circles_mutex):
                local_selected_circles = self.selected_circles.copy()

            try:
                updated_frame, updated_circles = frame_analysis(
                    frame,
                    local_settings,
                    local_circles,
                    local_selected_circles,
                    frame_pos,
                    self.frame_start,
                    self.bubble_counter_start
                )

                self.FrameUpdate.emit(updated_frame)
                with QMutexLocker(self.circles_mutex):
                    self.circles.clear()
                    self.circles.update(updated_circles)

            except Exception as e:
                print(f"Frame analysis failed: {e}")
                break

            frame_analysis_iteration += 1
            proc_ticks = cv.getTickCount() - start_tick
            proc_secs = proc_ticks / tick_freq
            time.sleep(max(display_time - proc_secs, 0))

        if cap:
            cap.release()

    @Slot(bool)
    def on_pause(self, do_pause):
        self.paused = do_pause
    
    def update_camera_frame(self, data):
        with QMutexLocker(self.camera_data_mutex):
            self.camera_data = data
            # print(f"data in readthread {self.camera_data}")

    def stop(self):
        self.running = False
