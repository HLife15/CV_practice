import cv2 as cv
import numpy as np

# 이미지 불러오기
img_list = [
    'C:\\Users\\USER\\Desktop\\kleague.png',
    'C:\\Users\\USER\\Desktop\\example.png',
    'C:\\Users\\USER\\Desktop\\botkaku.png',
    'C:\\Users\\USER\\Desktop\\fxxk.png',
    'C:\\Users\\USER\\Desktop\\profile.png',
    'C:\\Users\\USER\\Desktop\\profile4.png',
]
img_select = 0

while True:
    # 이미지 불러오기
    img = cv.imread(img_list[img_select])
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # 색조, 채도, 명도 채널에 각각 히스토그램 균등화 작업
    img_hist1 = np.dstack((cv.equalizeHist(img[:,:,0]),
                           cv.equalizeHist(img[:,:,1]),
                           cv.equalizeHist(img[:,:,2])))

    # YCbCr의 휘도(luminance channel, 밝은 정도)에만 히스토그램 균등화 작업
    img_cvt = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
    img_hist2 = np.dstack((cv.equalizeHist(img_cvt[:,:,0]),
                           img_cvt[:,:,1],
                           img_cvt[:,:,2]))
    img_hist2 = cv.cvtColor(img_hist2, cv.COLOR_YCrCb2BGR)

    # 모든 이미지 보여주기
    merge = np.hstack((img, img_hist1, img_hist2))
    cv.imshow('Color Histogram Equalization: Image | Each Channel | Luminance Channel', merge)
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
