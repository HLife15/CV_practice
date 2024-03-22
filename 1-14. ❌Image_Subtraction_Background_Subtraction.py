# 오류 투성이

import numpy as np
import cv2 as cv

# 영상 불러오기
video = cv.VideoCapture('C:\\Users\\USER\\Desktop\\SYVideo.wmv')
assert video.isOpened(), 'Cannot read the given video'

# 컨트롤 파라미터 초기화
blur_ksize = (9, 9)
blur_sigma = 3
diff_threshold = 50
bg_update_rate = 0.05
fg_update_rate = 0.001
zoom_level = 0.8

# 배경 이미지 불러오기
img_back = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png')
assert img_back is not None, 'Cannot read the initial background image'
img_back = cv.GaussianBlur(img_back, blur_ksize, blur_sigma).astype(np.float64)

box = lambda ksize: np.ones((ksize, ksize), dtype=np.uint8)
while True:
    # 영상에서 이미지 추출
    valid, img = video.read()
    if not valid:
        break

    # 현재 이미지와 배경 이미지의 차이 찾기
    img_blur = cv.GaussianBlur(img, blur_ksize, blur_sigma)
    img_diff = img_blur - img_back

    # 임계값 적용
    img_norm = np.linalg.norm(img_diff, axis=2)
    img_bin = np.zeros_like(img_norm, dtype=np.uint8)
    img_bin[img_norm > diff_threshold] = 255

    # 모폴로지 연산 적용
    img_mask = img_bin.copy()
    img_mask = cv.erode(img_mask, box(3))               # 작은 노이즈 차단
    img_mask = cv.dilate(img_mask, box(5))              # 손상된 부분 연결
    img_mask = cv.dilate(img_mask, box(3))              # 손상된 부분 연결
    fg = img_mask == 255                                # 전경 마스크 유지
    img_mask = cv.erode(img_mask, box(3), iterations=2) # 두꺼운 마스크를 얇게

    # 배경 이미지 업데이트
    # Alternative) cv.createBackgroundSubtractorMOG2(), cv.bgsegm
    bg = ~fg
    img_back[bg] = (bg_update_rate * img_blur[bg] + (1 - bg_update_rate) * img_back[bg]) # With the higher weight
    img_back[fg] = (fg_update_rate * img_blur[fg] + (1 - fg_update_rate) * img_back[fg]) # With the lower weight

    # 전경 이미지 추출
    img_fore = np.zeros_like(img)
    img_fore[fg] = img[fg]

    # 모든 이미지 보여주기
    merge = np.vstack((np.hstack((img, img_back.astype(np.uint8))),
                       np.hstack((cv.cvtColor(img_mask, cv.COLOR_GRAY2BGR), img_fore))))
    merge = cv.resize(merge, None, None, zoom_level, zoom_level)
    cv.imshow('Change Detection: Original | Background | Foreground Mask | Foreground', merge)

    # Process the key event
    key = cv.waitKey(1)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27: # ESC
        break

cv.destroyAllWindows()
