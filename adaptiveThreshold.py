import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', 'y-ing-.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.medianBlur(img_gray, 27)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
