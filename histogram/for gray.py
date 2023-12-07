import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread(r"C:\Users\user\Pictures\Screenshots\iam.png")

# 이미지의 높이와 너비 가져오기
height, width, _ = image.shape

# 빈 그레이 이미지 생성
gray_image = np.zeros((height, width), dtype=np.uint8)

# 원본 이미지의 모든 픽셀을 반복하며 그레이 스케일로 변환
for y in range(height):
    for x in range(width):
        # 원본 이미지에서 픽셀의 B, G, R 값을 가져와서 그레이 값 계산
        blue, green, red = image[y, x]
        gray_value = int(0.2989 * red + 0.5870 * green + 0.1140 * blue)

        # 그레이 이미지에 그레이 픽셀 설정
        gray_image[y, x] = gray_value

# 그레이 이미지 저장
cv2.imwrite('그레이이미지.png', gray_image)

# 그레이 이미지 표시
cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()