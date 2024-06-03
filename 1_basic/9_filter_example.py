import numpy as np
import cv2

# detech the midle line of the image
I_in = cv2.imread("edge_01.png")
cv2.imshow("Original image", I_in)

# step 0: convert to 1 chanel
I_in = cv2.cvtColor(I_in, cv2.COLOR_BGR2GRAY)
cv2.imshow("Step 0 image", I_in)

# step 1: median filter
I_in = cv2.medianBlur(I_in, 9)
cv2.imshow("Step 1 image", I_in)

# step 2: Kantenfilter
kanten_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
I_in = cv2.filter2D(I_in, cv2.CV_64F, kanten_filter, borderType=cv2.BORDER_REPLICATE)
cv2.imshow("Step 2 image", I_in)

# step 3: Glätten/ Tiefpass filter mit Box filter
tiefpass = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9
I_in = cv2.filter2D(I_in, cv2.CV_64F, tiefpass, borderType=cv2.BORDER_REPLICATE)
I_in = I_in / np.max(I_in)
cv2.imshow("Step 3 image", I_in)

cv2.waitKey(0)
