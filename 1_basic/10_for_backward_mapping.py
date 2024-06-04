import numpy as np
import cv2

""" Einlesen des Bildes """
img = cv2.imread("normal.jpg")
print("img shape:", img.shape)
rows, cols, channels = img.shape

# do with frame work
t_1 = np.float32(
    [
        [
            np.cos(np.pi / 4),
            np.sin(np.pi / 4),
            0,
        ],  # 0: translation 0 pixel in x richtung
        [
            -np.sin(np.pi / 4),
            np.cos(np.pi / 4),
            0,
        ],  # 0: translation 0 pixel in y richtung
    ]
)
dst = cv2.warpAffine(img, t_1, (cols, rows))
cv2.imshow("img_opencv", dst)

# do it from scratch
c1, c2, c3, c4 = (
    np.cos(np.pi / 4),
    np.sin(np.pi / 4),
    -np.sin(np.pi / 4),
    np.cos(np.pi / 4),
)
c_y, c_x = rows / 2, cols / 2


def new_pos(x, y):
    T = np.array([[c1, c2], [c3, c4]])
    c = np.array([c_x, c_y])
    pos = np.array([x, y]) - c
    new = (
        np.matmul(
            T,
            pos,
        )
        + c
    )
    return round(new[0]), round(new[1])


x = 4
y = 5

test = new_pos(x, y)
print("test:", test)


def old_pos(x, y):
    T = np.array([[c1, c2], [c3, c4]])
    T_inv = np.linalg.inv(T)
    c = np.array([c_x, c_y])
    pos = np.array([x, y]) - c
    new = (
        np.matmul(
            T_inv,
            pos,
        )
        + c
    )

    return round(new[0]), round(new[1])


test = old_pos(x, y)
print("test:", test)


def forward_mapping(img):
    new_img = np.zeros_like(img)
    for c in range(cols):
        for r in range(rows):
            new_c, new_r = new_pos(c, r)
            if new_c not in range(0, cols) or new_r not in range(0, rows):
                continue
            new_img[new_r, new_c] = img[r, c]
    return new_img


def backward_mapping(img):
    new_img = np.zeros_like(img)
    for c in range(cols):
        for r in range(rows):
            old_c, old_r = old_pos(c, r)
            if old_c not in range(0, cols) or old_r not in range(0, rows):
                continue
            new_img[r, c] = img[old_r, old_c]
    return new_img


cv2.waitKey(0)

new_img = forward_mapping(img)
print("new_img shape:", new_img.shape)
cv2.imshow("new_img_forward", new_img)

new_img = backward_mapping(img)
cv2.imshow("new_img_backward", new_img)

cv2.waitKey(0)
