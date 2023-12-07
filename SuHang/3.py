import cv2
import numpy as np
import math

img = cv2.imread(r"C:\Users\user\Pictures\Screenshots\iam.png", cv2.IMREAD_COLOR)
rows, cols = img.shape[:2]
print(str(cols)+", "+str(rows))

point1_ori = [math.ceil(cols * (1 / 4)), math.ceil(rows * (1 / 4))]
point2_ori = [math.ceil(cols * (3 / 4)), math.ceil(rows * (1 / 4))]
point3_ori = [math.ceil(cols * (1 / 4)), math.ceil(rows * (3 / 4))]
print(str(point1_ori)+", "+str(point2_ori)+", "+str(point3_ori))

point1_aff = [math.ceil(cols * (1 / 4)), math.ceil(rows * (3 / 8))]
point2_aff = [math.ceil(cols * (3 / 4)), math.ceil(rows * (1 / 8))]
point3_aff = [math.ceil(cols * (1 / 4)), math.ceil(rows * (7 / 8))]
print(str(point1_aff)+", "+str(point2_aff)+", "+str(point3_aff))

pts1 = np.float32([point1_ori, point2_ori, point3_ori])
pts2 = np.float32([point1_aff, point2_aff, point3_aff])

cv2.circle(img, point1_ori, 10, (255, 0, 0), -1) #red
cv2.circle(img, point2_ori, 10, (0, 255, 0), -1) #green
cv2.circle(img, point3_ori, 10, (0, 0, 255), -1) #blue

M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Ori", img)
cv2.imshow("Aff", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()