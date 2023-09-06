import cv2 as cv
import numpy as np

def empty(a):
    pass

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

cv.namedWindow("trackbar")
cv.resizeWindow("trackbar", 640, 240)
cv.createTrackbar("Huemin", "trackbar", 90, 179, empty)
cv.createTrackbar("Huemax", "trackbar", 150, 179, empty)
cv.createTrackbar("Satmin", "trackbar", 50, 255, empty)
cv.createTrackbar("Satmax", "trackbar", 128, 255, empty)
cv.createTrackbar("Valmin", "trackbar", 50, 255, empty)
cv.createTrackbar("Valmax", "trackbar", 255, 255, empty)

while True:
    success, img = cap.read()
    if not success:
        break

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Huemin", "trackbar")
    h_max = cv.getTrackbarPos("Huemax", "trackbar")
    s_min = cv.getTrackbarPos("Satmin", "trackbar")
    s_max = cv.getTrackbarPos("Satmax", "trackbar")
    v_min = cv.getTrackbarPos("Valmin", "trackbar")
    v_max = cv.getTrackbarPos("Valmax", "trackbar")
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    mask = cv.inRange(hsv, lower, upper)
    result = cv.bitwise_and(img, img, mask=mask)

    cv.imshow("orgi", img)
    cv.imshow("mask", mask)
    cv.imshow("result", result)
    
    key = cv.waitKey(10)
    if key == 27:  # Exit when the 'Esc' key is pressed
        break

cap.release()
cv.destroyAllWindows()
