import cv2 as cv
import numpy as np
import time
from time import perf_counter
import os


circles = list()

video = cv.VideoCapture(os.path.join(os.path.dirname(__file__), '../static/sample_bubble_video.mp4'))
# video = cv.VideoCapture(os.path.join(os.path.dirname(__file__), '../static/sample_bubble_video_unstable.mp4'))

fps = video.get(cv.CAP_PROP_FPS)
ret, frame = video.read()
t0 = 0
scale_height = .55
scale_width = .55

# scale first frame to start video writing
frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
h, w = frame.shape[:2]

# start writing video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("output.avi", fourcc, fps, (w, h))

#sample_bubble_video
frame_start = 225
frame_end = 410

# # # sample_bubble_video_unstable
# frame_start = 0
# frame_end = 700

video.set(cv.CAP_PROP_POS_FRAMES, frame_start)

def nothing(val):
    pass

cv.namedWindow("Circle Detection")
cv.createTrackbar("thresh_val", "Circle Detection", 79, 255, nothing)
cv.createTrackbar("max_val", "Circle Detection",0, 255, nothing)
cv.createTrackbar("blur", "Circle Detection", 9, 100, nothing)
cv.createTrackbar("adapt_area", "Circle Detection", 55, 100, nothing)
cv.createTrackbar("adapt_c", "Circle Detection", 13, 100, nothing)
cv.createTrackbar("min_area", "Circle Detection", 25, 1000, nothing)

while video.isOpened():
    ret, frame = video.read()

    # trackbar positions
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

    # restart video
    if video.get(cv.CAP_PROP_POS_FRAMES) == frame_end:
        break
        print(f"blur:{blur}")
        print(f"adapt_area:{adapt_area}")
        print(f"adapt_c:{adapt_c}")
        print(f"min_area:{min_area}")
        video.set(cv.CAP_PROP_POS_FRAMES, frame_start)

    # skip “black” frames
    h, w = frame.shape[:2]
    if not np.array_equal(frame[h//2, w//2], [0,0,0]):

        # resize and recalc frame shape
        frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
        h, w = frame.shape[:2]

        # contouring filters
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # gray = cv.GaussianBlur(gray, (blur, blur), 0)
        gray = cv.medianBlur(gray, blur)
        gray = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, adapt_area, adapt_c)
        # ret, gray = cv.threshold(gray, thresh_val, max_val, cv.THRESH_BINARY)
        gray = cv.bitwise_not(gray)

        # countour detection
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
                
                x = round(x)
                y = round(y)
                r = round(r, 2)
                cv.circle(frame, (x, y), int(r), (255, 0, 255), 1)
                cv.circle(frame, (x, y), 2, (0, 255, 0), 1)
                
                # on first frame populate circles
                if video.get(cv.CAP_PROP_POS_FRAMES) == frame_start + 1:
                    circles.append([x, y, [(video.get(cv.CAP_PROP_POS_FRAMES), round(r, 2))]])
                
                # on all other frames, find matches
                else:
                    circles_np = np.array(circles, dtype=object)
                    subtracted = np.abs(circles_np[:, 0] - np.full(len(circles_np[:, 0]), x))

                    # closest_idx = [array(), []]
                    err = 1
                    closest_idx = np.where(subtracted < err)
                    
                    # no match found, need to create a new circle list
                    if len(closest_idx[0]) == 0:
                        circles.append([x, y, [(video.get(cv.CAP_PROP_POS_FRAMES), round(r, 2))]])

                    # match found, update bucket
                    else:
                        circles[closest_idx[0][0]][2].append((video.get(cv.CAP_PROP_POS_FRAMES), r))
        
        # calculate fps
        real_fps = 1/(perf_counter()-t0)
        fps_text = f"FPS: {int(real_fps)}"
        cv.putText(frame, fps_text, (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv.LINE_AA)
        t0 = perf_counter()

        out.write(frame)
        cv.imshow("Circle Detection", frame)
        cv.imshow("Filtered image", gray)

    # break on esc
    if cv.waitKey(1) & 0xFF == 27:
        break

out.release() 
cv.destroyAllWindows()

print(f"circles: {circles[0]}")