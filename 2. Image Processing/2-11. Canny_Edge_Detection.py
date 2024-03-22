import numpy as np
import cv2 as cv

def drawText(img, text, org=(10, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.6, color=(0, 0, 0), colorBoundary=(255, 255, 255)):
    cv.putText(img, text, org, fontFace, fontScale, colorBoundary, thickness=2)
    cv.putText(img, text, org, fontFace, fontScale, color)

img_list = [
    'C:\\Users\\USER\\Desktop\\kleague.png',
    'C:\\Users\\USER\\Desktop\\example.png',
    'C:\\Users\\USER\\Desktop\\botkaku.png',
    'C:\\Users\\USER\\Desktop\\fxxk.png',
    'C:\\Users\\USER\\Desktop\\profile.png',
    'C:\\Users\\USER\\Desktop\\profile4.png',
]

# 컨트롤 파라미터 초기화
threshold1 = 500
threshold2 = 1200
aperture_size = 5
img_select = -1

while True:
    # 회색 이미지 불러오기
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # Canny Edge 이미지 추출
    edge = cv.Canny(img, threshold1, threshold2, apertureSize=aperture_size)

    # 모든 이미지 보여주기
    info = f'Thresh1: {threshold1}, Thresh2: {threshold2}, KernelSize: {aperture_size}'
    cv.putText(edge, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(edge, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img, edge))
    cv.imshow('Canny Edge: Original | Result', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        threshold1 += 2
    elif key == ord('-') or key == ord('_'):
        threshold1 -= 2
    elif key == ord(']') or key == ord('}'):
        threshold2 += 2
    elif key == ord('[') or key == ord('{'):
        threshold2 -= 2
    elif key == ord('>') or key == ord('.'):
        aperture_size = min(aperture_size + 2, 7)
    elif key == ord('<') or key == ord(','):
        aperture_size = max(aperture_size - 2, 3)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
