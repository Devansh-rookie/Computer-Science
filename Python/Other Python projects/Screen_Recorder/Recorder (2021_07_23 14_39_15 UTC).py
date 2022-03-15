import pyautogui
import cv2
import numpy as np
import utils

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*"XVID")


filename = f'Recording {utils.addition(0)}.avi'

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Recording")
cv2. resizeWindow("Recording", 480, 270)

while True:

    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    if cv2.waitKey(1) == ord("`"):
        break

out.release()
cv2.destroyAllWindows()

