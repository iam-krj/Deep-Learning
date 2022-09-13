import cv2
import imutils
img = cv2.imread("krj.jpg")
resizeImg = imutils.resize(img, width =200)
cv2.imwrite("Hello.jpg", resizeImg)
