import cv2
import numpy as np
from matplotlib import pyplot as plt


def histogram():
    img1 = cv2.imread(r"C:\Users\user\Pictures\Screenshots\iam.png")
    img2 = cv2.imread(r"C:\Users\user\Pictures\Screenshots\cat.png")
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    h1, w1 = img1_gray.shape
    h2, w2 = img2_gray.shape

    def cvt(i):
        b, g, r = cv2.split(i)
        i = cv2.merge([r, g, b])
        return i

    img1 = cvt(img1)
    img2 = cvt(img2)

    fig = plt.figure()

    hist1_test = np.zeros((256))
    hist2_test = np.zeros((256))

    for y in range(h1):
        for x in range(w1):
            i = img1_gray[y, x]
            hist1_test[i] = hist1_test[i] + 1

    for y in range(h2):
        for x in range(w2):
            j = img2_gray[y, x]
            hist2_test[j] = hist2_test[j] + 1

    hist1 = cv2.calcHist([img1_gray], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([img2_gray], [0], None, [256], [0, 256])
    plt.subplot(231), plt.imshow(img1), plt.title('Image_A'), plt.xticks([]), plt.yticks([])
    plt.subplot(232), plt.imshow(img2), plt.title('Image_B'), plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.plot(hist1), plt.xlim([0, 256])
    plt.subplot(234), plt.plot(hist2), plt.xlim([0, 256])

    plt.subplot(235), plt.plot(hist1_test), plt.xlim([0, 256])
    plt.subplot(236), plt.plot(hist2_test), plt.xlim([0, 256])

    plt.show()


histogram()
