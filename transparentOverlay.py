import os
import cv2
import numpy as np


img = cv2.imread(os.path.join('.', 'Data', 'batman.jpg'))
img2 = cv2.imread(os.path.join('.', 'Data', 'symbol.jpg'))
overlay = img2.copy()

alpha = 0.4

kernel = np.ones((3, 3), np.uint8)
hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

lower_hsv = np.array([0, 64, 114])
upper_hsv = np.array([360, 255, 255])

Mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
Mask = cv2.erode(Mask, kernel, iterations=3)
Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
Mask = cv2.dilate(Mask, kernel, iterations=1)

maskColor = Mask.copy()
maskColor = cv2.cvtColor(maskColor, cv2.COLOR_GRAY2BGR)
maskColor[:, :, 2] = np.zeros([maskColor.shape[0], maskColor.shape[1]])
maskColor[:, :, 1] = np.zeros([maskColor.shape[0], maskColor.shape[1]])

print(maskColor.shape)
# Mask = cv2.bitwise_not(Mask)

image_new = cv2.addWeighted(overlay, alpha, maskColor, 1 - alpha, 0)

# cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('Mask', Mask)
cv2.imshow('MaskC', maskColor)
cv2.imshow('Overlay', image_new)

cv2.waitKey(0)
cv2.destroyAllWindows()
