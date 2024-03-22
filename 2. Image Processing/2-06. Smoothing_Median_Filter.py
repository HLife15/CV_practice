import numpy as np
import cv2 as cv

# 이미지 리스트 불러오기
img_list = [
    'C:\\Users\\USER\\Desktop\\kleague.png',
    'C:\\Users\\USER\\Desktop\\example.png',
    'C:\\Users\\USER\\Desktop\\botkaku.png',
    'C:\\Users\\USER\\Desktop\\fxxk.png',
    'C:\\Users\\USER\\Desktop\\profile.png',
    'C:\\Users\\USER\\Desktop\\profile4.png']

# 컨트롤 파라미터 초기화
kernel_size = 5
img_select = -1

while True:
    # 회색 이미지로 불러오기
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)

    # 중간값 필터 적용
    result = cv.medianBlur(img, kernel_size)

    # 모든 이미지 보여주기
    merge = np.hstack((img, result))
    cv.imshow('Medial Filtering: Original | Result', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27:
        break
    elif key == ord('+') or key == ord('='):
        kernel_size += 2
    elif key == ord('-') or key == ord('_'):
        kernel_size = max(kernel_size - 2, 3)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)
