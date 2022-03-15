import cv2

img = cv2.imread("../assets/star.jpg", -1)


cv2.imshow("asdf", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
