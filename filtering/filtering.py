import cv2.cv2 as cv2
import numpy as np


def noting(x):
    pass


def filtering():
    img = cv2.imread(r"C:\Users\user\Pictures\Screenshots\iam.png", cv2.IMREAD_COLOR)
    cv2.namedWindow("Filtering")
    cv2.createTrackbar("K", 'Filtering', 1, 20, noting)

    while(1):
        if cv2.waitKey(1) & 0xFF == 27:
            break
        k = cv2.getTrackbarPos('K', 'Filtering')
        if k == 0:
            k = 1
        kernel = np.ones((k, k), np.float32)/ (k*2)
        dst = cv2.filter2D(img, -1, kernel)
        cv2.imshow('JetsonNano_Filtering', dst)

    cv2.destroyAllWindows()

filtering()