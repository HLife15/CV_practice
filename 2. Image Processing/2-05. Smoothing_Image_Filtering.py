import numpy as np
import cv2 as cv

# 커널 정의
kernel_table = [
    {'name': 'Box 3x3',         'kernel': np.ones((3, 3)) / 9},   # Alternative: cv.boxFilter(), cv.blur()
    {'name': 'Gaussian 3x3',    'kernel': np.array([[1, 2, 1],    # Alternative: cv.GaussianBlur()
                                                    [2, 4, 2],
                                                    [1, 2, 1]]) / 16},
    {'name': 'Box 5x5',         'kernel': np.ones((5, 5)) / 25},
    {'name': 'Gaussian 5x5',    'kernel': np.array([[1,  4,  6,  4, 1],
                                                    [4, 16, 24, 16, 4],
                                                    [6, 24, 36, 24, 6],
                                                    [4, 16, 24, 16, 4],
                                                    [1,  4,  6,  4, 1]]) / 256},
]

# 이미지 리스트 불러오기
img_list = [
    'C:\\Users\\USER\\Desktop\\kleague.png',
    'C:\\Users\\USER\\Desktop\\example.png',
    'C:\\Users\\USER\\Desktop\\botkaku.png',
    'C:\\Users\\USER\\Desktop\\fxxk.png',
    'C:\\Users\\USER\\Desktop\\profile.png',
    'C:\\Users\\USER\\Desktop\\profile4.png']

# 컨트롤 파라미터 초기화
kernel_select = 0
img_select = 0

while True:
    # 회색 이미지로 불러오기
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)

    # 주어진 커널로 이미지에 합성곱 적용
    name, kernel = kernel_table[kernel_select].values() # (짧은) 별명 짓기
    result = cv.filter2D(img, -1, kernel) # -1 : output datatype (-1이면 input과 datatype 동일)

    # 이미지와 커널 적용된 이미지 보여주기
    merge = np.hstack((img, result))
    cv.imshow('Image Filtering: Original | Filtered', merge)

    # 키 설정
    key =cv.waitKey()
    if key == 27:
        break
    elif key == ord('+') or key == ord('='):
        kernel_select = (kernel_select + 1) % len(kernel_table)
    elif key == ord('-') or key == ord('_'):
        kernel_select = (kernel_select + 1) % len(kernel_table)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)
