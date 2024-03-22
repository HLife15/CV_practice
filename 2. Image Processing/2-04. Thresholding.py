import numpy as np
import cv2 as cv

def drawText(img, text, org=(10, 25), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.6, color=(0, 0, 0), colorBoundary=(255, 255, 255)):
    cv.putText(img, text, org, fontFace, fontScale, colorBoundary, thickness=2)
    cv.putText(img, text, org, fontFace, fontScale, color)

# 회색 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'
img_threshold_type = cv.THRESH_BINARY_INV # 검은색에 가까운 색을 픽셀로 인식

# 컨트롤 파라미터 초기화
threshold = 127
adaptive_type = cv.ADAPTIVE_THRESH_MEAN_C
adaptive_blocksize = 99
adaptive_C = 4

while True:
    # 이미지에 Thresholding 적용
    _, binary_user = cv.threshold(img, threshold, 255, img_threshold_type)
    threshold_otsu, binary_otsu = cv.threshold(img, threshold, 255, img_threshold_type | cv.THRESH_OTSU)
    binary_adaptive = cv.adaptiveThreshold(img, 255, adaptive_type, img_threshold_type, adaptive_blocksize, adaptive_C)

    # 이미지와 Threshold 결과 보여주기
    drawText(binary_user, f'Threshold: {threshold}')
    drawText(binary_otsu, f'Otsu Threshold: {threshold_otsu}')
    adaptive_type_text = 'M' if adaptive_type == cv.ADAPTIVE_THRESH_MEAN_C else 'G'
    drawText(binary_adaptive, f'Type: {adaptive_type_text}, BlockSize: {adaptive_blocksize}, C: {adaptive_C}')
    merge = np.vstack((np.hstack((img, binary_user)), np.hstack((binary_otsu, binary_adaptive))))
    cv.imshow('Thresholding : Original | User | Otsu | Adaptive', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27:
        break
    elif key == ord('+') or key == ord('='):
        threshold += 1
    elif key == ord('-') or key == ord('_'):
        threshold -= 1
    elif key == ord('\t'):
        if adaptive_type == cv.ADAPTIVE_THRESH_MEAN_C:
            adaptive_type = cv.ADAPTIVE_THRESH_GAUSSIAN_C
        else:
            adaptive_type = cv.ADAPTIVE_THRESH_MEAN_C
    elif key == ord(']') or key == ord('}'):
        adaptive_blocksize += 2
    elif key == ord('[') or key == ord('{'):
        adaptive_blocksize = max(adaptive_blocksize - 2, 3)
    elif key == ord('>') or key == ord('.'):
        adaptive_C += 1
    elif key == ord('<') or key == ord(','):
        adaptive_C -= 1  

cv.destroyAllWindows()
