import numpy as np
import cv2

KERNEL_SIZE = 20

# load image
filepath = "text_%s.jpg"
images = list()
for i in [1, 2, 3]:
    img = cv2.imread(filepath % i)
    img = cv2.resize(img, (500, 500))
    images.append(img)


def balance(img):
    # kernel with value 1/ ( kernel*kernel)
    kernel = np.ones(shape=(KERNEL_SIZE, KERNEL_SIZE)) / (KERNEL_SIZE * KERNEL_SIZE)

    # apply conv2d on image, -1 is same depth as orignal image (in this case)
    # filter2D do use Padding to keep tracking the boder of the image
    # result img will have same size with
    blur_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    # print("blur_img shape:", blur_img.shape)

    # calculate quotien
    img = img / blur_img
    # print("img shape:", img.shape)

    # calculate I new
    img = 255 * (img - np.min(img)) / (np.max(img) - np.min(img))
    img = img.astype(np.uint8)

    return img


for i, img in enumerate(images):
    balance_img = balance(img=img)
    cv2.imshow("original image {}".format(i), img)
    cv2.imshow("balance image {}".format(i), balance_img)

cv2.waitKey(0)
