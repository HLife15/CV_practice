import numpy as np
import cv2 as cv

img_gray = np.full((480, 640), 255, dtype=np.uint8) # 640*480 크기의 흰 바탕화면 (0[Black] ~ 255[White])
img_gray[140:240, 220:420] = 0 # y좌표 140~240, x좌표 220~420 까지 검은 직사각형 그림
img_gray[240:340, 220:420] = 127 # y좌표 240~340, x좌표 220~420 까지 회색 직사각형 그림

img_color = np.zeros((480, 640, 3), dtype=np.uint8) # 640*480 크기의 검은 바탕화면 (channel = 3 [Color])
img_color[:] = 255 # 바탕화면 흰색으로
img_color[140:240, 220:420, :] = (0, 0, 255) # y좌표 140~240, x좌표 220~420 까지 빨간 직사각형 그림 (Blue, Green, Red)
img_color[240:340, 220:420, :] = (255, 0, 0) # y좌표 240~340, x좌표 220~420 까지 파란 직사각형 그림

cv.imshow('Gray Image', img_gray) # 'Gray Image' 창에서 img_gray 출력
cv.imshow('Color Image', img_color) # 'Color Image' 창에서 img_color 출력
cv.waitKey() # 아무 키나 누를 때까지 대기
# cv.destroyAllWindows() # Spider IDE 일 때만 필수
