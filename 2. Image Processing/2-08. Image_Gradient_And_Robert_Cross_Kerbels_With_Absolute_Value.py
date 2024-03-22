import numpy as np
import cv2 as cv

def drawText(img, text, org=(10, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.6, color=(0, 0, 0), colorBoundary=(255, 255, 255)):
    cv.putText(img, text, org, fontFace, fontScale, colorBoundary, thickness=2)
    cv.putText(img, text, org, fontFace, fontScale, color)

# 커널 정의
kernel_table = [
    {'name': 'Gradient X',      'kernel': np.array([[-1,  1]])},
    {'name': 'Robert DownRight','kernel': np.array([[-1,  0],
                                                    [ 0,  1]])},
    {'name': 'Gradient Y',      'kernel': np.array([[-1], [1]])},
    {'name': 'Robert UpRight',  'kernel': np.array([[ 0,  1],
                                                    [-1,  0]])},
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
    result = cv.filter2D(img, cv.CV_64F, kernel) # -1 : output datatype (dtype: np.float64)
    result = cv.convertScaleAbs(result) # 절댓값 씌운 후 착색과 함께 np.float64를 np.uint8로 바꿔줌

    # 이미지와 커널 적용된 이미지 보여주기
    drawText(result, f'{name}')
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
