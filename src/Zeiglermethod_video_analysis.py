import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time
from time import perf_counter
import os
from scipy.signal import find_peaks  # <-- added for peak detection


class BubbleKalman(cv.KalmanFilter):
    def __init__(self, center, dt, process_noise=1e-2, measurement_noise=1e-1):
        super().__init__(2,1)
        self.transitionMatrix = np.array([[1, dt],[0, 1]], dtype=np.float32)
        self.measurementMatrix = np.array([[1, 0]], dtype=np.float32)
        self.processNoiseCov = process_noise * np.eye(2, dtype=np.float32)
        self.measurementNoiseCov = np.array([[measurement_noise]], dtype=np.float32)
        self.statePost = np.zeros((2, 1), dtype=np.float32)
        self.errorCovPost = np.eye(2, dtype=np.float32)
        self.center = center


kf = BubbleKalman((100, 100), 10)
kf.correct(np.array([[12.3]], dtype=np.float32))
kf.correct(np.array([[10]], dtype=np.float32))
kf.correct(np.array([[9]], dtype=np.float32))

print("TEST3")
circles = list()
kalman_filters = list()
video = cv.VideoCapture(os.path.join(os.path.dirname(__file__), '250930_6vpp_neg3_400nm_001.mp4'))

frame_start = 225
frame_end = 1000

fps = video.get(cv.CAP_PROP_FPS)
ret, frame = video.read()
t0 = 0
scale_height = .55
scale_width = .55

frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
h, w = frame.shape[:2]

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("output.avi", fourcc, fps, (w, h))

video.set(cv.CAP_PROP_POS_FRAMES, frame_start)

def nothing(val):
    pass

cv.namedWindow("Circle Detection")
cv.createTrackbar("thresh_val", "Circle Detection", 79, 255, nothing)
cv.createTrackbar("max_val", "Circle Detection",70, 255, nothing)
cv.createTrackbar("blur", "Circle Detection", 5, 100, nothing)
cv.createTrackbar("adapt_area", "Circle Detection", 60, 100, nothing)
cv.createTrackbar("adapt_c", "Circle Detection", 13, 100, nothing)
cv.createTrackbar("min_area", "Circle Detection", 25, 1000, nothing)

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Trackbar positions
    thresh_val = cv.getTrackbarPos("thresh_val", "Circle Detection")
    max_val = cv.getTrackbarPos("max_val", "Circle Detection")
    blur = cv.getTrackbarPos("blur", "Circle Detection")
    if blur % 2 == 0:
        blur += 1
    adapt_area = cv.getTrackbarPos("adapt_area", "Circle Detection")
    if adapt_area % 2 == 0:
        adapt_area += 1
    adapt_c = cv.getTrackbarPos("adapt_c", "Circle Detection")
    min_area = cv.getTrackbarPos("min_area", "Circle Detection")

    if video.get(cv.CAP_PROP_POS_FRAMES) == frame_end:
        break

    detected_idxs = list()

    h, w = frame.shape[:2]
    if not np.array_equal(frame[h//2, w//2], [0,0,0]):

        frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
        h, w = frame.shape[:2]

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.GaussianBlur(gray, (blur, blur), 0)
        gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                    cv.THRESH_BINARY_INV, adapt_area, adapt_c)

        contours, _ = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            perimeter = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.03 * perimeter, True)
            area = cv.contourArea(contour)
            if area < min_area:
                continue

            (x, y), r = cv.minEnclosingCircle(contour)
            circle_area = np.pi * (r ** 2)
            circularity = area/circle_area if circle_area > 0 else 0

            if len(approx) > 4 and circularity > 0.7:
                center = (int(x), int(y))
                r = round(r, 2)
                cv.circle(frame, center, int(r), (255, 0, 255), 2)
                cv.circle(frame, center, 2, (0, 255, 0), 1)

                if video.get(cv.CAP_PROP_POS_FRAMES) == frame_start + 1:
                    circles.append([x, y, [(video.get(cv.CAP_PROP_POS_FRAMES), r)]])
                    detected_idxs.append(len(circles) - 1)
                    kalman_filters.append(BubbleKalman(x, y, r))
                    kalman_filters[-1].correct(np.array([[r]], dtype=np.float32))
                else:
                    circles_np = np.array(circles, dtype=object)
                    subtracted_x = np.abs(circles_np[:, 0] - np.full(len(circles_np[:, 0]), x))
                    subtracted_y = np.abs(circles_np[:, 1] - np.full(len(circles_np[:, 1]), y))
                    err = 5
                    closest_idx_x = np.where(subtracted_x < err)
                    closest_idx_y = np.where(subtracted_y < err)
                    closest_idx = np.intersect1d(closest_idx_x, closest_idx_y)

                    if closest_idx.size == 0:
                        circles.append([round(x), round(y), [(video.get(cv.CAP_PROP_POS_FRAMES), r)]])
                        kalman_filters.append(BubbleKalman(x, y, r))
                        kalman_filters[-1].correct(np.array([[r]], dtype=np.float32))
                        detected_idxs.append(len(circles) - 1)
                    else:
                        circles[closest_idx[0]][2].append((video.get(cv.CAP_PROP_POS_FRAMES), r))
                        detected_idxs.append(closest_idx[0])
                        kalman_filters[closest_idx[0]].correct(np.array([[r]], dtype=np.float32))

        found_idxs = np.zeros(len(circles), dtype=bool)
        found_idxs[detected_idxs] = True
        missing_idxs = np.where(found_idxs == False)[0]
        if missing_idxs.size > 0:
            for i in missing_idxs:
                prediction = kalman_filters[i].predict()[0][0]
                circles[i][2].append((video.get(cv.CAP_PROP_POS_FRAMES), round(float(prediction), 2), "estimated"))

        real_fps = 1/(perf_counter()-t0)
        cv.putText(frame, f"FPS: {int(real_fps)}", (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        t0 = perf_counter()

        out.write(frame)
        cv.imshow("Circle Detection", frame)
        cv.imshow("Filtered image", gray)

    if cv.waitKey(1) & 0xFF == 27:
        break

out.release()
cv.destroyAllWindows()

# -----------------------------
# Post-processing: radius vs frame and peak detection
# -----------------------------
bubble_idx = 0  # choose which bubble to analyze
frames = [pair[0] for pair in circles[bubble_idx][2]]
radii = [pair[1] for pair in circles[bubble_idx][2]]

# Find peaks
peaks, _ = find_peaks(radii, height=0)
peak_frames = [frames[p] for p in peaks]
peak_radii = [radii[p] for p in peaks]

print("Peak frames:", peak_frames)
print("Peak radii:", peak_radii)

# Estimate oscillation period (Pu) in frames
if len(peak_frames) > 1:
    Pu = np.mean(np.diff(peak_frames))
    print(f"Estimated oscillation period (Pu in frames): {Pu}")
else:
    print("Not enough peaks detected to estimate Pu.")

# Plot radius with peaks
plt.plot(frames, radii, label='Radius')
plt.plot(peak_frames, peak_radii, 'rx', label='Peaks')
plt.title("Bubble Radius per Frame with Peaks")
plt.xlabel("Frame")
plt.ylabel("Radius (pixels)")
plt.legend()
plt.show()

# -----------------------------
# Simulated PID Control & Plot
# -----------------------------
# Assume you want to control the bubble radius to reach a desired setpoint

setpoint = np.mean(radii) + 2  # target radius slightly above average
Kp = 0.7
Ki = 0.00
Kd = 0.0

control_signal = []
error_list = []
simulated_radius = []

pv = radii[0]  # start simulation from first measured radius
integral = 0
prev_error = 0
dt = 1 / fps if fps > 0 else 1  # approximate time per frame

for i in range(len(frames)):
    error = setpoint - pv
    integral += error * dt
    derivative = (error - prev_error) / dt
    u = Kp * error + Ki * integral + Kd * derivative  # control signal (PWM-like)
    pv += 0.1 * u  # simplified system response model — radius increases with u

    control_signal.append(u)
    simulated_radius.append(pv)
    error_list.append(error)
    prev_error = error

# Normalize control signal for plotting together
u_scaled = np.array(control_signal)
u_scaled = (u_scaled - np.min(u_scaled)) / (np.max(u_scaled) - np.min(u_scaled)) * (max(radii) - min(radii)) + min(radii)

# -----------------------------
# Plot radius + control signal
# -----------------------------
plt.figure(figsize=(10,6))
plt.plot(frames, radii, label='Measured Radius (pixels)', color='blue')
plt.plot(frames, simulated_radius, '--', label='Simulated PID Radius', color='orange')
plt.plot(frames, u_scaled, label='Control Signal (scaled)', color='red', alpha=0.6)
plt.xlabel("Frame")
plt.ylabel("Radius / Control Signal")
plt.title("Bubble Radius and PID Control Signal Over Frames")
plt.legend()
plt.grid(True)
plt.show()

