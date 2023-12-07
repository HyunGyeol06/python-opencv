import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\user\Downloads\s2-3.png", cv2.IMREAD_COLOR)

img_blue, _, __ = cv2.split(img)
h1, w1 = img_blue.shape


hist1_test = np.zeros((256))

for y in range(h1):
    for x in range(w1):
        i = img_blue[y, x]
        hist1_test[i] = hist1_test[i] + 1

cv2.imwrite("img_blue.png", img_blue)

plt.plot(hist1_test), plt.xlim([0, 256])
plt.show()
