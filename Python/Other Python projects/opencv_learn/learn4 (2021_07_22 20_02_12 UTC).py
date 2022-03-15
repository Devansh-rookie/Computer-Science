import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    line = cv2.line(frame, (0, 0), (width, height), (0,0,0), 10)

    line2 = cv2.line(line, (0, height), (width, 0), (0,255,0), 5)

    cv2.imshow("Frame", line)

    if cv2.waitKey(16) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
