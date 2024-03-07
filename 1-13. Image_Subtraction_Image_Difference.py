import numpy as np
import cv2 as cv

video = cv.VideoCapture('C:\\Users\\USER\\Desktop\\SYVideo.wmv')

if video.isOpened():
    img_prev = None
    while True:
        # 비디오에서 이미지 추출
        valid, img = video.read()
        if not valid:
            break

        # 달라진 이미지 추출
        if img_prev is None:
            img_prev = img.copy()
            continue
        img_diff = np.abs(img.astype(np.int32) - img_prev).astype(np.uint8)
        img_prev = img.copy()
            
        # 모든 이미지 보여주기
        merge = np.hstack((img, img_diff))
        cv.imshow('Image Difference: Original | Difference', merge)

        # 키 이벤트 설정
        key = cv.waitKey(1)
        if key == ord(' '):
            key = cv.waitKey()
        if key == 27:
            break

    cv.destroyAllWindows()

# 배경은 날아가고 움직이는 것의 외곽만 남김
