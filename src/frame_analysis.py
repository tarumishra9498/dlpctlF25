import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def frame_analysis(frame, settings, circles, frame_pos):
    t0 = 0
    scale_height = .55
    scale_width = .55
    return_frame = None
    frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
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
            
            # checks number of points in countour (approx) and circularity (good if close to 1)
            if len(approx) > 4 and circularity > 0.7:
                
                # x = round(x)
                # y = round(y)
                center = (int(x), int(y))
                r = round(r, 2)
                cv.circle(return_frame, center, int(r), (255, 0, 255), 1)
                cv.circle(return_frame, center, 2, (0, 255, 0), 1)

                if len(contours) == 0:
                    print('no countours found')
                    break
                    
                # on first frame populate circles
                elif len(circles) == 0:
                    circles.append([int(x), int(y), [(frame_pos, round(r, 2))]])
                    
                # on all other frames, find matches
                else:
                    if settings["tracking_on"]:
                        circles_np = np.array(circles, dtype=object)
                        subtracted_x = np.abs(circles_np[:, 0] - np.full(len(circles_np[:, 0]), x))
                        subtracted_y = np.abs(circles_np[:, 1] - np.full(len(circles_np[:, 1]), y))
                        
                        closest_idx_x = np.where(subtracted_x < settings["min_pos_err"])
                        closest_idx_y = np.where(subtracted_y < settings["min_pos_err"])
                        closest_idx = np.intersect1d(closest_idx_x, closest_idx_y)
                        
                        # no match found, need to create a new circle list
                        if closest_idx.size == 0:
                            circles.append([round(x), round(y), [(frame_pos, round(r, 2))]])

                        # match found, update bucket
                        else:
                            # print(f"closest index: {closest_idx}")
                            circles[closest_idx[0]][2].append((frame_pos, r))
    return return_frame, circles, frame_pos

# def plotting(circles):
#     x_coords = [pair[0] for pair in circles[0][2]]
#     y_coords = [pair[1] for pair in circles[0][2]]
#     plt.plot(x_coords, y_coords, 'o')
#     plt.title("Radius per Frame of Single Circle")
#     plt.xlabel("Frame")
#     plt.ylabel("Radius (pixels)")
#     plt.show()