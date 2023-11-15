import os

import cv2

# read image
image_path = os.path.join('Data', 'Football woman team.png')
img = cv2.imread(image_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
cv2.imshow('gray', img_gray)
cv2.imshow('rgb', img_rgb)
cv2.imshow('rgb', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
