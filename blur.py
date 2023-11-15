import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', 'k on Twitter.jpg'))

k_size = 7
blur = cv2.blur(img, (k_size, k_size))
gaussBlur = cv2.GaussianBlur(img, (k_size, k_size), 3)
medianBlur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.imshow('Gauss', gaussBlur)
cv2.imshow('median', medianBlur)
cv2.waitKey(0)
