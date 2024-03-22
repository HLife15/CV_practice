import numpy as np
import cv2 as cv

# 도수분포표 만들기
def get_histogram(gray_img):
    hist = np.zeros((256), dtype=np.uint32)
    for val in range(0, 256):
        hist[val] = sum(sum(gray_img == val))
    return hist

# 도수분포표 그리기
def conv_hist2img(hist):
    img = np.full((256, 256), 255, dtype=np.uint8)
    max_freq = max(hist)
    for val in range(len(hist)):
        normalized_freq = int(hist[val] / max_freq * 255)
        img[0:normalized_freq, val] = 0
    return img[::-1,:]

if __name__ == '__main__':
    img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)
    assert img is not None, 'Cannot read the given image'

    # 히스토그램 추출
    hist = get_histogram(img)
    print(f'* The number of bins : {len(hist)}')
    print(f'* The maximum frequency : {max(hist)}')
    print(f'* The minimum frequency : {min(hist)}')

    # 이미지와 히스토그램 보여주기
    img_hist = conv_hist2img(hist)
    img_hist = cv.resize(img_hist, (len(img[0]), len(img_hist)))
    merge = np.vstack((img, img_hist))
    cv.imshow('Histogram : Image | Histogram', merge)
    cv.waitKey()
    cv.destroyAllWindows()
