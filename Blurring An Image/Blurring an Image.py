import cv2
img = cv2.imread("krj.jpg")

gaussianBlurImg = cv2.GaussianBlur(img, (21,21),0)
cv2.imwrite("GaussianImage.jpg", gaussianBlurImg)
