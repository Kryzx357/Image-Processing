import cv2
from PIL import Image

from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
green = [0, 255, 0]  # yellow in BGR colorspace
red = [3, 73, 252]  # yellow in BGR colorspace
cap = cv2.VideoCapture(1)

while True:
    rate, frame = cap.read()

    hsv_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=green)

    mask = cv2.inRange(hsv_Image, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('web_cam', frame)

    '''Press Q key for exit'''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
