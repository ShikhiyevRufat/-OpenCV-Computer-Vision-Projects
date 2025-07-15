import cv2
import numpy as np


PREVIEW = 0
BLUR = 1
CANNY = 2
video_read = PREVIEW
result = None

cap = cv2.VideoCapture(0)
win_name = "Work with cam"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    rate, frame = cap.read()

    if  video_read == PREVIEW:
        result = frame
    elif video_read == BLUR:
        result = cv2.blur(frame, (13,13))
    elif video_read == CANNY:
        result = cv2.Canny(frame, 80, 150)


    cv2.imshow(win_name, result)
    
    if cv2.waitKey(1) == ord("a"):
        video_read = PREVIEW
    elif cv2.waitKey(1) == ord("s"):
        video_read = BLUR
    elif cv2.waitKey(1) == ord("d"):
        video_read = CANNY

cap.release()
cv2.destroyAllWindows(win_name)