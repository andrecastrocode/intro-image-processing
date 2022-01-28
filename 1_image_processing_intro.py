#hello world

import cv2

img = cv2.imread("resources/opencv.png")
msg = "hello world"
cv2.imshow(msg, img)

cv2.waitKey()
cv2.destroyAllWindows() 