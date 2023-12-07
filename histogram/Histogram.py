import cv2
import numpy as np
from matplotlib import pyplot as plt


img1 = cv2.imread(r"C:\Users\user\Pictures\Screenshots\iam.png")
img2 = cv2.imread(r"C:\Users\user\Pictures\Screenshots\cat.png")

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

fig = plt.figure()

hist1 = cv2.calcHist([img1_gray], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2_gray], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img1), plt.title('Image_A'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img2), plt.title('Image_B'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.plot(hist1), plt.xlim([0, 256])
plt.subplot(224), plt.plot(hist2), plt.xlim([0, 256])

plt.show()