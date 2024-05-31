import cv2
import numpy as np

# read original image
original_image = cv2.imread("image.jpg")
window_name = "window"

# color space COLOR_BGR2GRAY (gray image)
image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imshow(window_name, image)

# color space COLOR_BGR2HSV
image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
cv2.imshow(window_name, image)

cv2.waitKey(0)
