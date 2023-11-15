# crop
import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', '_seven-img-6310-20230405-132657.jpg'))

resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
print(img.shape)

# height, width
cropped_img = resized_img[:, 0:480]

cv2.imshow('img', img)
cv2.imshow('crop', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
