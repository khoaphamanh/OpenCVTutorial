import numpy as np
import cv2

# given a gray image
I_in = [
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
    [100, 100, 100, 100, 100],
    [200, 200, 100, 200, 200],
    [200, 200, 100, 200, 200],
]

I_in = np.asarray(I_in, dtype="uint8")
print("I_in:\n", I_in)
cv2.imshow(
    "Original image",
    cv2.resize(I_in, (500, 500), interpolation=cv2.INTER_NEAREST),
)

ddepth = -1  # result image have same data type with
ddepth = cv2.CV_64F  # result image have data type float 64

# hochpass filter
hochpass = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
print("hochpass:", hochpass)
result_filter = cv2.filter2D(
    src=I_in, ddepth=ddepth, kernel=hochpass, borderType=cv2.BORDER_REPLICATE
)
print("result_filter:\n", result_filter)
cv2.imshow(
    "Apply hochpass filter",
    cv2.resize(result_filter, (500, 500), interpolation=cv2.INTER_NEAREST),
)

# kanten filter
kanten = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
print("kanten:", kanten)
result_filter = cv2.filter2D(
    src=I_in, ddepth=ddepth, kernel=kanten, borderType=cv2.BORDER_REPLICATE
)
print("result_filter:\n", result_filter)
cv2.imshow(
    "Apply kanten filter",
    cv2.resize(result_filter, (500, 500), interpolation=cv2.INTER_NEAREST),
)

# median filter
result_filter = cv2.medianBlur(np.abs(I_in).astype(np.float32), 3)
print("result_filter", result_filter)
cv2.imshow(
    "Apply median filter",
    cv2.resize(result_filter, (500, 500), interpolation=cv2.INTER_NEAREST),
)

cv2.waitKey(0)
