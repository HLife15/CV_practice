import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png')
assert img is not None, 'Cannot read the given image'

# BGR 이미지를 HSV 이미지로 변환
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 색조, 채도, 명도 보여주기
img_hue = np.dstack((img_hsv[:,:,0],
                     np.full_like(img_hsv[:,:,0], 255),
                     np.full_like(img_hsv[:,:,0], 255)))
img_hue = cv.cvtColor(img_hue, cv.COLOR_HSV2BGR)
img_sat = np.dstack((img_hsv[:,:,1], ) * 3)
img_val = np.dstack((img_hsv[:,:,2], ) * 3)
merge = np.hstack((img, img_hue, img_sat, img_val))
cv.imshow('Color Conversion: Image | Hue | Saturation | Value', merge)
cv.waitKey()
cv.destroyAllWindows()
