import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class BubbleKalman:
    def __init__(self, x, y, r2, r1, dt, q_process_noise=1e-1, r_measurement_noise=1e-2):
        self.kf = cv.KalmanFilter(2, 1)
        self.kf.transitionMatrix = np.array([[1, dt], [0, 1]], dtype=np.float32)
        self.kf.measurementMatrix = np.array([[1, 0]], dtype=np.float32)
        self.kf.processNoiseCov = q_process_noise * np.eye(2, dtype=np.float32)
        self.kf.measurementNoiseCov = np.array([[r_measurement_noise]], dtype=np.float32)
        # self.kf.statePost = np.array([[r2], [(r2-r1)/dt]], dtype=np.float32)
        self.kf.statePost = np.array([[r2], [dt]], dtype=np.float32)
        self.kf.errorCovPost = np.eye(2, dtype=np.float32)
        self.center = (x, y)

    def correct(self, measurement):
        self.kf.correct(measurement)

    def predict(self):
        return self.kf.predict()

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

def frame_analysis(frame, settings, circles, selected_circles, kalman_filters, frame_pos, frame_start):
    return_frame = None
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    if settings["blur_on"]:
        gray = cv.GaussianBlur(gray, (settings["blur"], settings["blur"]), 0) 
    if settings["thresh_on"]:
        gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, settings["adapt_area"], settings["adapt_c"])
    if settings["filters_on"]: 
        return_frame = gray
    else:
        return_frame = frame
    
    print(f"iteration: {settings["video_iteration"]}, frame: {frame_pos}")

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
            circle_area = np.pi * (r ** 2)

            if circle_area > 0:
                circularity = area/circle_area
            else:
                circularity = 0

            if settings["selection_on"]:
                # add hovering
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

                if len(contours) == 0:
                    print('no countours found')
                    break

                # first frame, populate circles
                elif int(frame_pos) == frame_start or (settings["selection_on"] and len(circles) == 0):
                    try:
                        if settings["tracking_on"]:
                            circles.append([int(x), int(y), [[frame_pos, r]]])
                            kalman_filters[len(circles) - 1] = None
                            detected_idxs.append(len(circles) - 1)

                    except Exception as e:
                        print(f"first frame error: {e}")

                # on all other frames, find matches
                else:
                    if settings["tracking_on"]:
                        try:
                            circles_np = np.array(circles, dtype=object)
                            closest_idx = closest_idx_finder(circles_np, x, y, settings["min_pos_err"])

                            # no match found, need to create a new circle list
                            if closest_idx.size == 0:
                                circles.append([round(x), round(y), [[frame_pos, r]]])
                                kalman_filters[len(circles) - 1] = None
                                detected_idxs.append(len(circles) - 1)

                            # match found, update bucket
                            else:
                                # FIX FIX FIFX
                                circles[closest_idx[0]][2].append([frame_pos, r])
                                if kalman_filters[closest_idx[0]] is None:
                                    r2 = circles[closest_idx[0]][2][-1][1]
                                    r1 = circles[closest_idx[0]][2][-2][1]
                                    kalman_filters[closest_idx[0]] = BubbleKalman(x, y, r2, r1, 1/settings["fps"])
                                    pred = kalman_filters[closest_idx[0]].predict()
                                    kalman_filters[closest_idx[0]].correct(np.array([[r]], dtype=np.float32))
                                else:
                                    pred = kalman_filters[closest_idx[0]].predict()
                                    kalman_filters[closest_idx[0]].correct(np.array([[r]], dtype=np.float32))
                                detected_idxs.append(closest_idx[0])

                        except Exception as e:
                            print(f"tracking error: {e}")
    
        # find circles that haven't been detected with contour detection
        found_idxs = np.zeros(len(circles), dtype=bool)
        found_idxs[detected_idxs] = True
        missing_idxs = np.where(found_idxs == False)[0]
        if missing_idxs.size > 0:
            for i in missing_idxs:
                if len(circles[i][2]) > 2 and kalman_filters[i] is not None:
                    prediction = kalman_filters[i].predict()[0][0]
                    print(f"prediction {prediction}, index {i}")
                    if len(circles[i][2][-1]) != 3 and len(circles[i][2][-2]) != 3 and prediction > 0:
                        circles[i][2].append([frame_pos, round(float(prediction), 2), "estimate"])
                        center = (circles[i][0], circles[i][1])
                        cv.circle(return_frame, center, int(prediction), (173, 216, 230), 2)
                        cv.circle(return_frame, center, 2, (0, 255, 0), 1)
        
                
    cv.putText(return_frame, f"FPS: {int(settings["fps"])}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
    return return_frame, circles, kalman_filters

def plotting(circles):
    x_coords = [pair[0] for pair in circles[0][2]]
    y_coords = [pair[1] for pair in circles[0][2]]
    plt.plot(x_coords, y_coords, 'o')
    plt.title("Radius per Frame of Single Circle")
    plt.xlabel("Frame")
    plt.ylabel("Radius (pixels)")
    plt.show()