# 실행은 되는데 영상은 재생 안되고 터미널에 Frame이 100씩 늘어나는 것만 표시됨 (이미지 저장도 X)

import numpy as np
import cv2 as cv

# 영상 불러오기
video = cv.VideoCapture('C:\\Users\\USER\\Desktop\\SYVideo.wmv')
assert video.isOpened(), 'Cannot read the given video'

frame_count = 0
img_back = None
while True:
    # 영상에서 이미지 추출
    valid, img = video.read()
    if not valid:
        break
    frame_count += 1

    # 과정 보여주기
    if frame_count % 100 == 0:
        print(f'Frame: {frame_count}')

    # 이미지와 평균 이미지 (배경화면) 더함
    # cv.createBackgroundSubtractorMOG2(), cv::bgsegm
    if img_back is None:
        img_back = np.zeros_like(img, dtype=np.float64)
    img_back += img.astype(np.float64)
img_back = img_back / frame_count
img_back = img_back.astype(np.uint8)

# 평균 이미지를 저장하고 보여주기
cv.imwrite('C:\\Users\\USER\\Desktop\\SYVideo.png', img_back)
cv.imshow('Background Extraction', img_back)
cv.waitKey()
cv.destroyAllWindows()
