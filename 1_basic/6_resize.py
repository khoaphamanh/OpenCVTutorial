import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Original", img)

factors = [2, 4, 10]


for f in factors:
    downscale = cv2.resize(
        img, dsize=None, fx=1 / f, fy=1 / f, interpolation=cv2.INTER_NEAREST
    )
    reconstruct = cv2.resize(
        downscale, dsize=None, fx=f, fy=f, interpolation=cv2.INTER_NEAREST
    )
    cv2.imshow("Abgetastet mit Faktor {}".format(1 / f), reconstruct)

cv2.waitKey(0)
