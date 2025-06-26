import cv2 as cv
import numpy as np
import time
import os

# circles = dict()
# radii = dict()

# capture video
# video = cv.VideoCapture(os.path.join(os.path.dirname(__file__), '../static/sample_bubble_video.mp4'))
video = cv.VideoCapture(os.path.join(os.path.dirname(__file__), '../static/sample_bubble_video_unstable.mp4'))

start_time = time.perf_counter()
ret, frame = video.read()

# scale first frame to start video writing
scale_height = .55
scale_width = .55
frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
h, w = frame.shape[:2]

# start writing video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter("output.avi", fourcc, 30.0, (w, h))

def nothing(val):
    pass

cv.namedWindow("Hough Circle Image")
cv.createTrackbar("thresh_val", "Hough Circle Image", 90, 255, nothing)
cv.createTrackbar("max_val", "Hough Circle Image",0, 255, nothing)
cv.createTrackbar("med_blur", "Hough Circle Image", 13, 100, nothing)
cv.createTrackbar("param1","Hough Circle Image",73, 300, nothing)
cv.createTrackbar("param2","Hough Circle Image",21, 100, nothing)
cv.createTrackbar("min_r","Hough Circle Image",6, 50, nothing)
cv.createTrackbar("max_r","Hough Circle Image",50, 100, nothing)
cv.createTrackbar("minDist","Hough Circle Image",20, 100, nothing)

# # sample_bubble_video
# frame_start = 225
# frame_end = 410

# sample_bubble_video_unstable
frame_start = 0
frame_end = 700

# sample bubble video = start at 225, end at 410

video.set(cv.CAP_PROP_POS_FRAMES, frame_start)

while True:
    ret, frame = video.read()

    # trackbar positions
    thresh_val = cv.getTrackbarPos("thresh_val", "Hough Circle Image")
    max_val = cv.getTrackbarPos("max_val", "Hough Circle Image")
    med_blur = cv.getTrackbarPos("med_blur", "Hough Circle Image")
    if med_blur % 2 == 0:
        med_blur += 1

    p1 = cv.getTrackbarPos("param1","Hough Circle Image")
    if not(p1):
        p1 += 1

    p2 = cv.getTrackbarPos("param2","Hough Circle Image")
    min_dist = cv.getTrackbarPos("minDist","Hough Circle Image")
    min_r = cv.getTrackbarPos("min_r","Hough Circle Image")
    max_r = cv.getTrackbarPos("max_r","Hough Circle Image")

    # restart timer
    if video.get(cv.CAP_PROP_POS_FRAMES) == frame_end:
        video.set(cv.CAP_PROP_POS_FRAMES, frame_start)
        end_time = time.perf_counter()
        print(f"time elapsed: {round((end_time - start_time), 3)}")
        start_time = time.perf_counter()
        print(f"thresh:{thresh_val}, max_val:{max_val}, med_blur:{med_blur}")
        print(f"p1:{p1}, p2:{p2}, min_r:{min_r}, max_r:{max_r}, minDist:{min_dist}")

    # skip “black” frames
    h, w = frame.shape[:2]
    if not np.array_equal(frame[h//2, w//2], [0,0,0]):
        
        # resize and recalc frame shape
        frame = cv.resize(frame, (0, 0), fx=scale_width, fy=scale_height)
        h, w = frame.shape[:2]
    

        # crop to top-left quarter
        # frame = frame[1 : h//2, 1 : w//2]

        # filters
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, med_blur)
        ret, gray = cv.threshold(gray, thresh_val, max_val, cv.THRESH_TRUNC)
        
        frame_circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, minDist=min_dist,
                                param1=p1, param2= p2,
                                minRadius= min_r, maxRadius=max_r)

        # draw cirle detections
        if frame_circles is not None:
            for x, y, r in np.uint16(np.around(frame_circles[0])):
                cv.circle(frame, (x,y), r, (255,0,255), 2)
                cv.circle(frame, (x,y), 2, (0,255,0), 2)

        out.write(frame)
        cv.imshow("Hough Circle Image", frame)
        cv.imshow("Filtered image", gray)

    # break on esc
    if cv.waitKey(1) & 0xFF == 27:
        break

# for frame in circles:
#     print(np.size((circles[frame])))
#     for x, y, r in circles[frame][0]:
#         x = round(x)
#         y = round(y)

#         if (x, y) not in radii.keys():
#             radii[(x, y)] = r

# print(radii)

out.release() 
cv.destroyAllWindows()