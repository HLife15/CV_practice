import numpy as np
import cv2 as cv

# 캔버스 준비 (640*480 크기의 흰색으로 칠해진 컬러채널)
canvas = np.full((480, 640, 3), 255, dtype=np.uint8)

# 선 그리기 // cv.line(캔버스, 시작점, 끝점, 선 색, 선 굵기)
# 텍스트 입력 // cv.putText(캔버스, 표시할 텍스트, 시작점, 폰트, 글씨 크기, 글씨 색)
cv.line(canvas, (10, 10), (640-10, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (640-10, 10), (10, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (320, 10), (320, 480-10), color=(200, 200, 200), thickness=2)
cv.line(canvas, (10, 240), (640-10, 240), color=(200, 200, 200), thickness=2)
cv.putText(canvas, 'Line', (10, 20), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0))

# 원 그리기 // cv.circle(캔버스, 중심점, 반지름, 선 색, 선 굵기)
center = (100, 240)
cv.circle(canvas, center, radius=60, color=(0, 0, 255), thickness=5)
cv.putText(canvas, 'Circle', center, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 0))

# 사각형 그리기 // cv.rectangle(캔버스, top-left 좌표, bottom-right 좌표, 선 색, 선 굵기 [-1일 땐 내부 선 색으로 채움])
pt1, pt2 = (320-60, 240-50), (320+60, 240+50)
cv.rectangle(canvas, pt1, pt2, color=(0, 255, 0), thickness=-1)
cv.putText(canvas, 'Rectangle', pt1, cv.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255))

# 삼각형 (점을 지나는 연속 선) 그리기 // cv.polyline(캔버스, 좌표 배열, True [처음 좌표와 마지막 좌표 잇는 선 그림], 선 색, 선 굵기)
pts = np.array([(540, 240-50), (540-55, 240+50), (540+55, 240+50)])
cv.polylines(canvas, [pts], True, color=(255, 0, 0), thickness=5)
cv.putText(canvas, 'Polylines', pts[0].flatten(), cv.FONT_HERSHEY_DUPLEX, 0.5, (0, 200, 200))

# 캔버스 보여주기
cv.imshow('Shape Drawing', canvas)
cv.waitKey()
cv.destroyAllWindows()
