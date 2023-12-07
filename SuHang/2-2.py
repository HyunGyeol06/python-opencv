import cv2
import numpy as np

img = cv2.imread(r"C:\Users\user\Pictures\Screenshots\xdfghjk.png", cv2.IMREAD_COLOR)

h, w, _ = img.shape

gray_img = np.zeros((h, w), dtype=np.uint8)

for y in range(0, h):
    for x in range(0, w):
        if not (int(w * (1 / 2)) < x < int(w * (3 / 4)) and int(h * (1 / 2)) < y < int(h * (3 / 4))):
            b, g, r = img[y, x]
            gray_value = int(r + g + b) / 3
            gray_img[y, x] = gray_value

cv2.imwrite("gray_img.png", gray_img)

cv2.imshow("Original", img)
cv2.imshow('Gray', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
