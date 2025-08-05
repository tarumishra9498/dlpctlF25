from PySide6.QtCore import QMutexLocker, QThread, Signal, Slot
import cv2 as cv
import time
import numpy as np
import traceback
import serial

import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt

from frame_analysis import frame_analysis


class VideoReadThread(QThread):
    FrameUpdate = Signal(object)
    PIDcmds = Signal(object)

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
        fgen, 
        serial
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
        self.fgen = fgen
        self.serial = serial
        self.paused = False
        self.display_fps = 30.0
        self.bubble_counter_start = 1
        self.radii = []
        self.control_vals = []

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
            if video_iteration == 2:
                print('breaking')
                break

            if self.settings["analysis_on"] == False:
                print('stopping')
                self.running = False
            while self.paused and self.running:
                time.sleep(0.01)

        
            start_tick = cv.getTickCount()
            
            with QMutexLocker(self.settings_mutex):
                local_settings = self.settings.copy()

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
                    h, w = frame.shape[:2]

                    self.out = cv.VideoWriter(
                        "filtered_output.mp4", 
                        cv.VideoWriter.fourcc(*'mp4v'),
                        30,
                        (w, h),
                        isColor=True,          
                    )
                    if not self.out.isOpened():
                        raise RuntimeError("Could not open VideoWriter for AVI output")

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

                if local_settings["pid_on"] and len(updated_circles) > 0:
                    self.radii.append([updated_circles[1].history[-1][0], updated_circles[1].history[-1][-1]])
                    self.control_vals.append([updated_circles[1].history[-1][0], updated_circles[1].pid.control_signal])                   
                   
                    on_time, off_time = updated_circles[1].pid.pwm_cycle

                    cmd_sent = time.time() * 1000
                    self.send_command(self.serial, updated_circles[1].pid.cycle_time, on_time)
                    response = None
                    while response != "DONE":
                        response = self.serial.readline().decode().strip()
                    cmd_received = round(time.time() * 1000)

                    time_elapsed = cmd_received - cmd_sent - updated_circles[1].pid.cycle_time
                    # print(f"latency: {time_elapsed}")

                if updated_frame.ndim == 2:      
                    write_frame = cv.cvtColor(updated_frame, cv.COLOR_GRAY2BGR)
                else:
                    write_frame = updated_frame
                try:
                    self.out.write(write_frame)
                    self.FrameUpdate.emit(write_frame)
                except Exception as e:
                    print(e)

                with QMutexLocker(self.circles_mutex):
                    self.circles.clear()
                    self.circles.update(updated_circles)

            except Exception as e:
                print(f"Frame analysis failed: {e}")
                traceback.print_exc()
                break
            
            frame_analysis_iteration += 1
            proc_ticks = cv.getTickCount() - start_tick
            proc_secs = proc_ticks / tick_freq
            time.sleep(max(display_time - proc_secs, 0))

        if cap:
            cap.release()

        if self.out:
            self.out.release()
        
        if local_settings["pid_on"]:
            fig, ax = plt.subplots()
            xs_r, ys_r = zip(*self.radii)
            xs_c, ys_c = zip(*self.control_vals)

            ax.scatter(xs_r, ys_r, c='blue', s = 5, label='Radii')
            ax.scatter(xs_c, ys_c, c='red', s = 5, label='Control')
            ax.grid()
            ax.legend()  
            plt.title("Control and Radius vs Time")
            fig.savefig("control_vs_radius.png", dpi=300, bbox_inches='tight')
            plt.close(fig)

    @Slot(bool)
    def on_pause(self, do_pause):
        self.paused = do_pause
    
    def update_camera_frame(self, data):
        with QMutexLocker(self.camera_data_mutex):
            self.camera_data = data
            # print(f"data in readthread {self.camera_data}")

    def stop(self):
        self.running = False

    def send_command(self, serial, cycle_time, on_time):
        command = f"{int(cycle_time)} {int(on_time)}\n"
        # print(command)
        serial.write(command.encode()) 
        