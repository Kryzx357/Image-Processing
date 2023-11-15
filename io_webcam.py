import cv2

cap = cv2.VideoCapture(1)

while True:
    rate, frame = cap.read()

    frame = cv2.putText(frame, 'OMG!!!', (350, 100), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 0), 13, cv2.LINE_AA)
    frame = cv2.putText(frame, 'OMG!!!', (350, 100), cv2.FONT_HERSHEY_DUPLEX, 1.5, (255, 255, 255), 4, cv2.LINE_AA)

    cv2.imshow('web_cam', frame)

    '''Press Q key for exit'''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
