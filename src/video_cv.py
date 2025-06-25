import cv2 as cv
import numpy as np
from hough_params import HOUGH_PARAMS

# import scalebar as sb
import time

circles = dict()
radii = dict()


video = cv.VideoCapture("static/sample_bubble_video.mp4")
# video = cv.VideoCapture('ecoli.mp4')
# while video.get(cv.CAP_PROP_POS_FRAMES) != (video.get(cv.CAP_PROP_FRAME_COUNT) - 1):


start_time = time.perf_counter()

ret, frame = video.read()
frame = cv.resize(frame, (0, 0), fx=0.75, fy=0.75)
h, w = frame.shape[:2]
fourcc = cv.VideoWriter.fourcc(*"mp4v")
out = cv.VideoWriter("output.mp4", fourcc, 30.0, (w, h))

video.set(cv.CAP_PROP_POS_FRAMES, 0)

while video.get(cv.CAP_PROP_POS_FRAMES) != 410:
    ret, frame = video.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # skip “black” frames
    if not np.array_equal(frame[h // 2, w // 2], [0, 0, 0]):
        # resize and recalc shape

        frame = cv.resize(frame, (0, 0), fx=0.75, fy=0.75)
        h, w = frame.shape[:2]
        # crop to top-left quarter
        # frame = frame[1 : h//2, 1 : w//2]

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray, HOUGH_PARAMS["med_blur"])

        # detect circles
        frame_circles = cv.HoughCircles(
            gray,
            cv.HOUGH_GRADIENT,
            1,
            minDist=HOUGH_PARAMS["min_dist"],
            param1=HOUGH_PARAMS["p1"],
            param2=HOUGH_PARAMS["p2"],
            minRadius=HOUGH_PARAMS["minR"],
            maxRadius=HOUGH_PARAMS["maxR"],
        )

        # draw detections
        if frame_circles is not None:
            for x, y, r in np.uint16(np.around(frame_circles[0])):
                cv.circle(frame, (x, y), r, (255, 0, 255), 2)
                cv.circle(frame, (x, y), 2, (0, 255, 0), 2)

        out.write(frame)

        # show
        cv.imshow("hough circle frame", frame)

    # break on '1'
    key = cv.waitKey(1)
    if key == ord("1"):
        break

end_time = time.perf_counter()
print(f"time elapsed: {end_time - start_time}")

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
