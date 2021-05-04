import numpy as np
import cv2

cap = cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
face=cv2.CascadeClassifier("face.xml")


while True:
    ret, frame = cap.read()

# Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = face.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in f:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the resulting frame

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




