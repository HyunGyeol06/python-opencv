import cv2
import numpy as np

img = cv2.imread(r"C:\Users\user\Downloads\s1-4.png", cv2.IMREAD_COLOR)

h, w, _ = img.shape

ret_d, th_d = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(th_d, cv2.MORPH_CLOSE, kernel)

hole = cv2.subtract(opening, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

ret, img_thresh = cv2.threshold(hole, 230, 255, 0)

contours, hierachy = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contours = cv2.drawContours(img_thresh.copy(), contours, -1, (255, 255, 255), 2)

result = cv2.putText(img_contours, str(len(contours)), (int(w/2), int(h/2)), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

cv2.imwrite("result.png", result)

cv2.imshow("ORI", img)
cv2.imshow("Contours", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
