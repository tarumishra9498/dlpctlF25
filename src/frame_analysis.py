import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time 


class Circle:
    def __init__(self, x, y, r1):
        self.center = (x, y)
        self.history = []
        self.kalman = None
        self.pid = None

    def add_circle(self, frame_pos, x, y, r):
        self.history.append([frame_pos, int(x), int(y), round(r, 2)])


class CircleKalman:
    def __init__(self, x, y, r, dt, q_process_noise=1e-1, r_measurement_noise=1e-2):
        self.kf = cv.KalmanFilter(2, 1)
        self.kf.transitionMatrix = np.array([[1, dt], [0, 1]], dtype=np.float32)
        self.kf.measurementMatrix = np.array([[1, 0]], dtype=np.float32)
        self.kf.processNoiseCov = q_process_noise * np.eye(2, dtype=np.float32)
        self.kf.measurementNoiseCov = np.array(
            [[r_measurement_noise]], dtype=np.float32
        )
        self.kf.statePost = np.array([[r], [dt]], dtype=np.float32)
        self.kf.errorCovPost = np.eye(2, dtype=np.float32)
        self.center = (x, y)

    def correct(self, measurement):
        self.kf.correct(measurement)

    def predict(self):
        return self.kf.predict()


class CirclePID:
    def __init__(self, x, y, setpoint, init_r, dt):
        self.x = x
        self.y = y
        self.setpoint = setpoint
        self.pv = init_r
        self.kp = 0.6
        self.ki = 0.3
        self.kd = 0.1
        self.error = 0
        self.prev_error = 0
        self.integral = 0
        self.derivative = 0
        self.control_signal = 0
        self.cycle_time = 80
        self.pwm_cycle = [40, 40]
        self.max_ratio = 50

    def update(self, measurement, dt):
        try:
            self.pv = measurement

            if self.pv > 100:
                self.control_signal = 0
            else:
                self.error = self.setpoint - self.pv
                self.integral += self.error * dt
                self.derivative = (
                    (self.error - self.prev_error) / dt if dt > 0 else 0.0
                )
                
                self.control_signal = self.kp * self.error + self.ki * self.integral + self.kd * self.derivative

            self.prev_error = self.error
            
            u = max(0.0, min(self.control_signal, self.max_ratio))
            on_time = (u / self.max_ratio ) * self.cycle_time
            off_time = self.cycle_time - on_time

            self.pwm_cycle = [round(on_time, 2), round(off_time, 2)]

        except Exception as e:
            pass
            # print(f"pid error: {e}")

def closest_idx_finder(array2d, x, y, tolerance):
    if len(array2d) == 0:
        return np.array([])
    else:
        try:
            subtracted_x = np.abs(array2d[:, 0] - np.full(len(array2d[:, 0]), x))
            subtracted_y = np.abs(array2d[:, 1] - np.full(len(array2d[:, 1]), y))
            closest_idx_x = np.where(subtracted_x < tolerance)
            closest_idx_y = np.where(subtracted_y < tolerance)
            closest_idx = np.intersect1d(closest_idx_x, closest_idx_y)
            return closest_idx
        except Exception as e:
            print(f"closest index finder {e}")
            return np.array([])

def frame_analysis(
    frame, settings, circles, selected_circles, frame_pos, frame_start, bubble_counter
):
    return_frame = None
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if settings["blur_on"]:
        gray = cv.GaussianBlur(gray, (settings["blur"], settings["blur"]), 0)
    if settings["thresh_on"]:
        gray = cv.adaptiveThreshold(
            gray,
            255,
            cv.ADAPTIVE_THRESH_MEAN_C,
            cv.THRESH_BINARY_INV,
            settings["adapt_area"],
            settings["adapt_c"],
        )
    if settings["filters_on"]:
        return_frame = gray
    else:
        return_frame = frame

    # print(f"iteration: {settings["video_iteration"]}, frame: {frame_pos}")

    if settings["contour_on"] and settings["thresh_on"] and settings["blur_on"]:
        contours, _ = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        detected_idxs = list()
        for contour in contours:
            perimeter = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.03 * perimeter, True)
            area = cv.contourArea(contour)

            if area < settings["min_area"]:
                continue

            # Calculate circularity, ratio of the contour area to the smallest enclosing circle area
            (x, y), r = cv.minEnclosingCircle(contour)
            circle_area = np.pi * (r**2)

            if circle_area > 0:
                circularity = area / circle_area
            else:
                circularity = 0

            if settings["selection_on"]:
                h, w = frame.shape[:2]
                if len(selected_circles) > 0:
                    selections_np = np.array(selected_circles, dtype=np.float32)
                    scale_h = h / settings["pixmap_h"]
                    scale_w = w / settings["pixmap_w"]
                    selections_np[:, 0] *= scale_w
                    selections_np[:, 1] *= scale_h
                    closest_idx = closest_idx_finder(selections_np, x, y, r)

                    # if circle is selected twice, don't show it
                    if closest_idx.size % 2 == 0:
                        continue

                # no selections, dont display anything
                else:
                    continue

            # checks number of points in countour (approx) and circularity (good if close to 1)
            if len(approx) > 4 and circularity > 0.7:
                x = round(x, 2)
                y = round(y, 2)
                center = (int(x), int(y))
                r = round(r, 2)
                cv.circle(return_frame, center, int(r), (173, 216, 230), 2)
                cv.circle(return_frame, center, 2, (0, 255, 0), 1)
                if settings["fps"] > 0:
                    dt = 1 / settings["fps"]
                else:
                    dt = None

                if len(contours) == 0:
                    print("no countours found")
                    break

                # first frame, populate circles
                elif int(frame_pos) == frame_start or (
                    settings["selection_on"] and len(circles) == 0
                ):
                    try:
                        if settings["tracking_on"]:
                            circles[bubble_counter] = Circle(x, y, r)
                            circles[bubble_counter].add_circle(frame_pos, x, y, r)
                            detected_idxs.append(bubble_counter)
                            if settings["pid_on"]:
                                # change setpoint
                                circles[bubble_counter].pid = CirclePID(x, y, 100, r, dt)
                                circles[bubble_counter].pid.update(r, dt)
                            bubble_counter += 1

                    except Exception as e:
                        print(f"first frame error: {e}")

                else:
                    if settings["tracking_on"]:
                        try:
                            keys = list(circles.keys())
                            centers_np = np.array(
                                [circles[k].center for k in keys], dtype=np.float32
                            )
                            idx = closest_idx_finder(
                                centers_np, x, y, settings["min_pos_err"]
                            )  # index of the key in the centers list, which is not always the key value

                            # no match found, need to create a new circle list
                            if idx.size == 0:
                                circles[bubble_counter] = Circle(x, y, r)
                                circles[bubble_counter].add_circle(frame_pos, x, y, r)
                                if settings["pid_on"]:
                                    # change setpoint
                                    circles[bubble_counter].pid = CirclePID(x, y, 0, r, dt)
                                    circles[bubble_counter].pid.update(r, dt)
                                detected_idxs.append(bubble_counter)
                                bubble_counter += 1

                            # match found
                            else:
                                closest_idx = keys[idx[0]]
                                circles[closest_idx].add_circle(frame_pos, x, y, r)
                                if circles[closest_idx].kalman is None:
                                    circles[closest_idx].kalman = CircleKalman(
                                        x, y, r, dt
                                    )
                                    pred = circles[closest_idx].kalman.predict()
                                    circles[closest_idx].kalman.correct(
                                        np.array([[r]], dtype=np.float32)
                                    )
                                else:
                                    pred = circles[closest_idx].kalman.predict()
                                    circles[closest_idx].kalman.correct(
                                        np.array([[r]], dtype=np.float32)
                                    )
                                if settings["pid_on"]:
                                    circles[closest_idx].pid.update(r, dt)
                                detected_idxs.append(closest_idx)

                        except Exception as e:
                            print(f"tracking error: {e}")

        # find circles that haven't been detected with contour detection
        found_idxs = np.zeros(len(circles) + 1, dtype=bool)
        found_idxs[detected_idxs] = True
        missing_idxs = np.where(found_idxs == False)[0]
        if missing_idxs.size > 0:
            for i in missing_idxs:
                if (
                    i != 0
                    and len(circles[i].history) > 2
                    and circles[i].kalman is not None
                ):
                    prediction = circles[i].kalman.predict()[0][0]
                    if (
                        len(circles[i].history[-1]) != 4
                        and len(circles[i].history[-2]) != 4
                        and prediction > 0
                    ):
                        circles[i].history.append[
                            frame_pos,
                            circles[i].center(0),
                            circles[i].center(1),
                            prediction,
                            "estimate",
                        ]
                        cv.circle(
                            return_frame,
                            circles[i].center,
                            int(prediction),
                            (173, 216, 230),
                            2,
                        )
                        cv.circle(return_frame, circles[i].center, 2, (0, 255, 0), 1)

    cv.putText(
        return_frame,
        f"FPS: {int(settings['fps'])}",
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv.LINE_AA,
    )
    return return_frame, circles

