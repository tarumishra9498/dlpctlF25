import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import os
from PySide6.QtGui import QImage

def qimage_to_cv(qimg):
    # qimage to bgr
    qimg = qimg.convertToFormat(QImage.Format.Format_RGBA8888)
    width = qimg.width()
    height = qimg.height()
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
    return cv.cvtColor(arr, cv.COLOR_RGBA2BGR)


def cv_to_qimage(img):
    # bgr/grayscale to qimage
    if img.ndim == 2:
        fmt = QImage.Format.Format_Grayscale8
        h, w = img.shape
        ptr = img.data
        bytes_per_line = w
        return QImage(ptr, w, h, bytes_per_line, fmt)


def frame_analysis(q_image, blur, adapt_area, adapt_c, min_area, circles, frame_pos, blur_on, thresh_on, contour_on, tracking_on):

    frame = qimage_to_cv(q_image)

    t0 = 0
    scale_height = .55
    scale_width = .55
    
    frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
    h, w = frame.shape[:2]

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (blur, blur), 0) if blur_on else None
    gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, adapt_area, adapt_c)
    contours, _ = cv.findContours(gray, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:

        # Approximate the contour to a polygon
        perimeter = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.03 * perimeter, True)

        # Get the area of the (potentially irregular) contour
        area = cv.contourArea(contour)
        
        # filters out small circles
        if area < min_area:
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
            cv.circle(frame, center, int(r), (255, 0, 255), 2)
            cv.circle(frame, center, 2, (0, 255, 0), 1)
            
            # on first frame populate circles
            if frame_pos == 1:
                circles.append([x, y, [frame_pos, round(r, 2)]])
            
            # on all other frames, find matches
            else:
                circles_np = np.array(circles, dtype=object)
                subtracted_x = np.abs(circles_np[:, 0] - np.full(len(circles_np[:, 0]), x))
                subtracted_y = np.abs(circles_np[:, 1] - np.full(len(circles_np[:, 1]), y))
                
                err = 5
                closest_idx_x = np.where(subtracted_x < err)
                closest_idx_y = np.where(subtracted_y < err)
                closest_idx = np.intersect1d(closest_idx_x, closest_idx_y)
                
                # no match found, need to create a new circle list
                if closest_idx.size == 0:
                    # print("match not found")
                    circles.append([round(x), round(y), [frame_pos, round(r, 2)]])

                # match found, update bucket
                else:
                    # print(f"closest index: {closest_idx}")
                    circles[closest_idx[0]][2].append(frame_pos, r)
    
    frame = cv_to_qimage(frame)

    return frame, circles