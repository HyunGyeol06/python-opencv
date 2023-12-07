import copy

import cv2
import numpy as np
import matplotlib.pyplot as plt


def fourier():
    img = cv2.imread(r"C:\Users\user\Downloads\s2-5.png", cv2.IMREAD_GRAYSCALE)

    f = np.fft.fft2(img)
    shift = np.fft.fftshift(f)
    spect = 20*np.log(np.abs(shift))
    spect_filtered = copy.deepcopy(spect)

    spect_filtered[200:250, 200:250] = 0
    spect_filtered[350:400, 200:250] = 0
    spect_filtered[200:250, 350:420] = 0
    spect_filtered[350:420, 350:420] = 0
    spect_filtered[280:320, 350:] = 0
    spect_filtered[280:320, :250] = 0
    spect_filtered[350:, 280:320] = 0
    spect_filtered[:250, 280:320] = 0

    shift[200:250, 200:250] = 0
    shift[350:400, 200:250] = 0
    shift[200:250, 350:420] = 0
    shift[350:420, 350:420] = 0
    shift[280:320, 350:] = 0
    shift[280:320, :250] = 0
    shift[350:, 280:320] = 0
    shift[:250, 280:320] = 0

    f_ishift = np.fft.ifftshift(shift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    cv2.imwrite("./filtered_img.png", img_back)

    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title("ori"), plt.xticks([]), plt.yticks([])

    plt.subplot(222), plt.imshow(spect, cmap='gray')
    plt.title("spect"), plt.xticks([]), plt.yticks([])

    plt.subplot(223), plt.imshow(spect_filtered, cmap='gray')
    plt.title("spect_filtered"), plt.xticks([]), plt.yticks([])

    plt.subplot(224), plt.imshow(img_back, cmap='gray')
    plt.title("img_filtered"), plt.xticks([]), plt.yticks([])

    plt.show()



fourier()
