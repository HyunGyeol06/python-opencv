import cv2
import numpy as np
from matplotlib import pyplot as plt


def expand2square(image1, background_color=(255, 0, 0)):
    image = image1.copy()
    width, height = image.shape[::-1]

    if width == height:
        return image
    elif width > height:
        dif = width - height
        image = cv2.copyMakeBorder(image, dif // 2, dif // 2, 0, 0, cv2.BORDER_REPLICATE, background_color)
        return image
    else:
        dif = height - width
        image = cv2.copyMakeBorder(image, 0, 0, dif // 2, dif // 2, cv2.BORDER_REPLICATE, background_color)
        return image


img = cv2.imread(r"C:\Users\user\Downloads\s1-5.png", 0)
template = cv2.imread(r"C:\Users\user\Downloads\s1-5_template.png", 0)
# img = expand2square(img)
# template = expand2square(template)
w, h = template.shape[::-1]

method = cv2.TM_CCOEFF_NORMED
res = cv2.matchTemplate(img, template, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
res = expand2square(res)

if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
    top_left = min_loc
else:
    top_left = max_loc

ret_d, th_d = cv2.threshold(res, 0.2, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
th_img = cv2.morphologyEx(th_d, cv2.MORPH_OPEN, kernel)
th_img = th_img.astype(np.uint8)
th_img = expand2square(th_img)
th_img = cv2.resize(th_img, (400, 580))

contours, _ = cv2.findContours(th_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = img.copy()
img_contours = cv2.drawContours(img_contours, contours, -1, (51, 102, 255), 4)

pts1 = np.float32([[85, 50], [350, 50], [30, 580], [280, 580]])
pts2 = np.float32([[10, 10], [1000, 10], [10, 1000], [1000, 1000]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (1010, 1010))


cv2.imwrite("./pers.png", dst)

fig = plt.figure()
plt.subplot(131), plt.title('ori'), plt.imshow(img, cmap='gray'), plt.yticks([]), plt.xticks([])
plt.subplot(132), plt.title('template matching'), plt.imshow(th_d, cmap='gray'), plt.yticks([]), plt.xticks([])
#plt.subplot(223), plt.title('Threshold'), plt.imshow(img_contours, cmap='gray'), plt.yticks([]), plt.xticks([])
plt.subplot(133), plt.title('Perspective'), plt.imshow(dst, cmap='gray'), plt.yticks([]), plt.xticks([])
plt.show()
