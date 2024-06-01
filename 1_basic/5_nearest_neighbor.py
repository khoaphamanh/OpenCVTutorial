import numpy as np
import cv2

# choose the method
method = "opencv"  # "from_scratch"

# read the image
img = cv2.imread("image.jpg")
h, w, c = img.shape

# scales to resize the image smaller
scales = [4, 8, 13.5]
images = []

for s in scales:
    new_h, new_w = int(h / s), int(w / s)
    new_image = np.zeros(shape=(new_h, new_w, c), dtype=img.dtype)
    print("new_image shape:", new_image.shape)

    if method == "opencv":
        new_image = cv2.resize(img, (new_w, new_h))

    elif method == "from_scratch":

        for y in range(new_h):
            for x in range(new_w):
                x_from_original = int(x * s)
                y_from_original = int(y * s)
                new_image[y, x] = img[y_from_original, x_from_original]

    images.append(new_image)

# show image
cv2.imshow("original", img)
print(img.shape)
for idx, image in enumerate(images):
    scale = scales[idx]
    image = cv2.resize(image, (w, h))
    print("image shape:", image.shape)
    cv2.imshow("{}".format(scale), image)
cv2.waitKey(0)
