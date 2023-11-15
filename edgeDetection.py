import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'Data', 'on Twitter.jpg'))

img_Edge = cv2.Canny(img, 200, 400)

img_Edge_d = cv2.dilate(img_Edge, np.ones((3, 3), dtype=np.int8))
img_Edge_e = cv2.erode(img_Edge_d, np.ones((2, 2), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('Edge', img_Edge)
cv2.imshow('dia', img_Edge_d)
cv2.imshow('ero', img_Edge_e)
cv2.waitKey(0)
