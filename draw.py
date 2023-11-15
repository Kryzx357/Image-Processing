import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', 'hd.jpg'))
img2 = img

print(img.shape)

# line
# cv2.line(img, (150, 500), (50, 650), (0, 0, 255), 3)
cv2.arrowedLine(img2, (50, 650), (150, 500), (0, 0, 255), 3, cv2.LINE_AA)

# rectangle
cv2.rectangle(img2, (280, 300), (450, 600), (0, 0, 255), 5, cv2.LINE_AA)

# circle
cv2.circle(img2, (200, 310), 35, (0, 0, 255), 7, cv2.LINE_AA)

# text
cv2.putText(img2, 'NOT CLICKBAIT', (100, 250), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 7, cv2.LINE_AA)
cv2.putText(img2, 'NOT CLICKBAIT', (100, 250), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img2, 'OMG!!!', (150, 650), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 0), 13, cv2.LINE_AA)
cv2.putText(img2, 'OMG!!!', (150, 650), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 255, 255), 4, cv2.LINE_AA)

cv2.imwrite(os.path.join('.', 'Data', 'hdMEME.jpg'), img2)

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.waitKey(0)
