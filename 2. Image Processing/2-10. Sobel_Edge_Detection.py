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
edge_threshold = 0.1
img_select = 3

while True:
    # 회색 이미지 불러오기
    img = cv.imread(img_list[img_select], cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # 양방향 Sobel로 모서리 추출
    # [0, 1] 안에서 해당값 정규화 (1020 = 255*(1+2+1)에서 파생됨)
    dx   = cv.Sobel(img, cv.CV_64F, 1, 0) / 1020 # x방향 Sobel
    dy   = cv.Sobel(img, cv.CV_64F, 0, 1) / 1020 # y방향 Sobel
    mag  = np.sqrt(dx*dx + dy*dy) / np.sqrt(2)   # Sobel 규모
    ori  = np.arctan2(dy, dx)                    # Sobel 객체
    edge = mag > edge_threshold # Alternative) cv.threshold(), cv.adaptiveThreshold()

    # 컬러 이미지 준비
    ori[ori < 0] = ori[ori < 0] + 2*np.pi        # [-np.pi, np.pi)를 [0, 2*np.pi)로 변환
    ori_hsv = np.dstack((ori / (2*np.pi) * 180,  # HSV color - 색조
                        np.full_like(ori, 255), # HSV color - 채도 channel
                        mag * 255))             # HSV color - 명도 channel
    ori_bgr = cv.cvtColor(ori_hsv.astype(np.uint8), cv.COLOR_HSV2BGR)

    # 컬러 원본, Sobel X/Y, 규모, edge 이미지 준비
    img_bgr  = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    dx_bgr   = cv.cvtColor(abs(dx * 255).astype(np.uint8), cv.COLOR_GRAY2BGR)
    dy_bgr   = cv.cvtColor(abs(dy * 255).astype(np.uint8), cv.COLOR_GRAY2BGR)
    mag_bgr  = cv.cvtColor((mag * 255).astype(np.uint8),   cv.COLOR_GRAY2BGR)
    edge_bgr = cv.cvtColor((edge * 255).astype(np.uint8),  cv.COLOR_GRAY2BGR)

    # 모든 이미지 보여주기
    drawText(img_bgr, 'Original')
    drawText(dx_bgr,  'SobelX')
    drawText(dy_bgr,  'SobelY')
    drawText(mag_bgr, 'Magnitude')
    drawText(ori_bgr, 'Orientation')
    drawText(edge_bgr, f'EdgeThreshold: {edge_threshold:.2f}')
    merge = np.vstack((np.hstack((img_bgr, dx_bgr, dy_bgr)),
                    np.hstack((edge_bgr, mag_bgr, ori_bgr))))
    cv.imshow('Sobel Edge', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        edge_threshold = min(edge_threshold + 0.02, 1)
    elif key == ord('-') or key == ord('_'):
        edge_threshold = max(edge_threshold - 0.02, 0)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
