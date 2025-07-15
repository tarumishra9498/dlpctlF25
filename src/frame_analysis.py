import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class BubbleKalman(cv.KalmanFilter):
    def __init__(self, center, dt, process_noise=1e-2, measurement_noise=1e-1):
        super().__init__(2,1)
        self.transitionMatrix = np.array([[1, dt],[0, 1]], dtype=np.float32) # F
        self.measurementMatrix = np.array([[1, 0]], dtype=np.float32) # H
        self.processNoiseCov = process_noise * np.eye(2, dtype=np.float32) # Q
        self.measurementNoiseCov = np.array([[measurement_noise]], dtype=np.float32) # R
        self.statePost = np.zeros((2, 1), dtype=np.float32) # initial state estimate
        self.errorCovPost = np.eye(2, dtype=np.float32) # initial state covariance
        self.center = center

def closest_idx_finder(array2d, x, y, tolerance):
    subtracted_x = np.abs(array2d[:, 0] - np.full(len(array2d[:, 0]), x))
    subtracted_y = np.abs(array2d[:, 1] - np.full(len(array2d[:, 1]), y))
    closest_idx_x = np.where(subtracted_x < tolerance)
    closest_idx_y = np.where(subtracted_y < tolerance)
    closest_idx = np.intersect1d(closest_idx_x, closest_idx_y)
    return closest_idx

def frame_analysis(frame, settings, circles, kalman_filters, frame_pos):
    t0 = 0
    # scale_height = .75
    # scale_width = .75
    return_frame = None
    # frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    if settings["blur_on"]:
        gray = cv.GaussianBlur(gray, (settings["blur"], settings["blur"]), 0)
    
    if settings["thresh_on"]:
        gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, settings["adapt_area"], settings["adapt_c"])

    if settings["filters_on"]: 
        return_frame = gray
    else:
        return_frame = frame

    if settings["contour_on"] and settings["thresh_on"] and settings["blur_on"]:
        contours, _ = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        detected_idxs = list()
        for contour in contours:

            # Approximate the contour to a polygon
            perimeter = cv.arcLength(contour, True)
            approx = cv.approxPolyDP(contour, 0.03 * perimeter, True)

            # Get the area of the (potentially irregular) contour
            area = cv.contourArea(contour)
            
            # filters out small circles
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
                # checks whether contour is selected based on radius and center point
                selections_np = np.array(settings["selected_circles"], dtype=np.float32)
                h, w = frame.shape[:2]

                if len(settings["selected_circles"]) > 0:
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
                
                # x = round(x)
                # y = round(y)
                center = (int(x), int(y))
                r = round(r, 2)
                cv.circle(return_frame, center, int(r), (173, 216, 230), 2)
                cv.circle(return_frame, center, 2, (0, 255, 0), 1)

                if len(contours) == 0:
                    print('no countours found')
                    break
                    
                # first frame, populate circles
                elif len(circles) == 0:
                    circles.append([int(x), int(y), [(frame_pos, round(r, 2))]])
                    kalman_filters.append(BubbleKalman(x, y, round(r, 2)))
                    kalman_filters[-1].correct(np.array([[r]], dtype=np.float32))
                    detected_idxs.append(len(circles) - 1)

                # on all other frames, find matches
                else:
                    if settings["tracking_on"]:
                        circles_np = np.array(circles, dtype=object)                        
                        closest_idx = closest_idx_finder(circles_np, x, y, settings["min_pos_err"])

                        # no match found, need to create a new circle list
                        if closest_idx.size == 0:
                            circles.append([round(x), round(y), [(frame_pos, round(r, 2))]])
                            kalman_filters.append(BubbleKalman(x, y, round(r, 2)))
                            kalman_filters[-1].correct(np.array([[r]], dtype=np.float32))
                            detected_idxs.append(len(circles) - 1)

                        # match found, update bucket
                        else:
                            circles[closest_idx[0]][2].append((frame_pos, r))
                            kalman_filters[closest_idx[0]].correct(np.array([[r]], dtype=np.float32))
                            detected_idxs.append(closest_idx[0])

        # find circles that haven't been detected with contour detection
        found_idxs = np.zeros(len(circles), dtype=bool)
        found_idxs[detected_idxs] = True
        missing_idxs = np.where(found_idxs == False)[0]
        if missing_idxs.size > 0:
            for i in missing_idxs:
                prediction = kalman_filters[i].predict()[0][0]
                # will never do two back to back predictions or an empty prediction
                if len(circles[i][2][-1]) != 3 and prediction > 0:
                    circles[i][2].append((frame_pos, round(float(prediction)), "estimated"))
                    center = (circles[i][0], circles[i][1])
                    cv.circle(return_frame, center, int(prediction), (173, 216, 230), 2)
                    cv.circle(return_frame, center, 2, (0, 255, 0), 1)

    return return_frame, circles, kalman_filters, frame_pos

# def plotting(circles):
#     x_coords = [pair[0] for pair in circles[0][2]]
#     y_coords = [pair[1] for pair in circles[0][2]]
#     plt.plot(x_coords, y_coords, 'o')
#     plt.title("Radius per Frame of Single Circle")
#     plt.xlabel("Frame")
#     plt.ylabel("Radius (pixels)")
#     plt.show()