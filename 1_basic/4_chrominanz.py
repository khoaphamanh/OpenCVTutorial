import cv2
import numpy as np

# read original image
original_image = cv2.imread("image.jpg")
window_name = "window"

pixel_sum = np.sum(
    original_image, keepdims=True, axis=2
)  # pixel_sum shape: (720, 1280, 1)

# normalize the pixel value p_r / (p_r + p_g + p_b), p_g / (p_r + p_g + p_b), p_b / (p_r + p_g + p_b)
image = original_image / pixel_sum

# show the image
cv2.imshow(window_name, image)

cv2.waitKey(0)
