import os

import cv2

# read image
image_path = os.path.join('.', 'Data', 'hicham_kaidi.jpg')

img = cv2.imread(image_path)

# write image

cv2.imwrite(os.path.join('.', 'Data', 'img_out.jpg'), img)

# visualize image

cv2.imshow('frame', img)
cv2.waitKey(0)
