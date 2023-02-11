import numpy as np
import cv2 as cv
# https://github.com/opencv/opencv/issues/14590
# https://www.jetbrains.com/help/pycharm/stubs.html
# numpy is a binding dependency
# py -m pip install numpy
# py -m pip install opencv-python

# noinspection PyUnresolvedReferences
camera = cv.VideoCapture(0)
if not camera.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()
