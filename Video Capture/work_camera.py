import cv2


win = cv2.VideoCapture(0)
win_name = "First Camera"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

while cv2.waitKey(1) !=27:
    has_frame, frame = win.read()
    if not has_frame:
        break

    cv2.imshow(win_name, frame)

win.release()
cv2.destroyAllWindows(win_name)