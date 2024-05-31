import cv2

# read the picture
I = cv2.imread("image.jpg")

m, n, k = I.shape
print("m:", m)
print("n:", n)
print("k:", k)

# display the picture
fenster_name = "Fenstername"
cv2.imshow(fenster_name, I)
cv2.waitKey(0)

# save the picture
new_name = "newname.jpg"
cv2.imwrite(new_name, I)

# to quit the run, press f5/run
