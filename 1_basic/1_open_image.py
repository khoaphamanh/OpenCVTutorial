import cv2

# read the picture
I = cv2.imread("image.jpg")

m, n, k = I.shape
print("m:", m)
print("n:", n)
print("k:", k)

# display the picture
cv2.imshow("Fenstername", I)
cv2.waitKey(0)

# save the picture
cv2.imwrite("newname.jpg", I)

# to quit the run, press f5/run
