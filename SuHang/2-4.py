import cv2
import numpy as np
from matplotlib import pyplot as plt


def hist(h, w, img):
    histogram = np.zeros((256))

    for y in range(h):
        for x in range(w):
            i = img[y, x]
            histogram[i] = histogram[i] + 1

    return histogram


def hist_eq(img1):
    img = img1.copy()
    a = np.zeros((256,), dtype=np.float16)

    height, width = img.shape

    for i in range(width):
        for j in range(height):
            g = img[j, i]
            a[g] = a[g] + 1

    tmp = 3 / (height * width)
    b = np.zeros((256,), dtype=np.float16)

    for i in range(256):
        for j in range(i + 1):
            b[i] += a[j] * tmp
        b[i] = round(b[i] * 255)

    b = b.astype(np.uint8)

    for i in range(width):
        for j in range(height):
            g = img[j, i]
            img[j, i] = b[g]
    return img


img = cv2.imread(r"C:\Users\user\Downloads\s2-4.png", 0)
eqhist = hist_eq(img)

h1, w1 = img.shape
h2, w2 = eqhist.shape

hist_ori = hist(h1, w1, img)
hist_eq = hist(h2, w2, eqhist)

cv2.imwrite("./hist-eq.png", eqhist)

fig = plt.figure()

plt.subplot(221), plt.imshow(img, 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(eqhist, 'gray')
plt.title('Histogram Equlization'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.plot(hist_ori), plt.xlim([0, 256])
plt.subplot(224), plt.plot(hist_eq), plt.xlim([0, 256])

plt.show()
