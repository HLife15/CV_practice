import numpy as np
import cv2 as cv

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

# 회색 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# control parameters 초기 설정
value_range = [20, 200] # 최솟값, 최댓값

while True:
    # 밝기/대비 적용
    img_tran = 255 / (value_range[1] - value_range[0]) * (img.astype(np.int32) - value_range[0])
    img_tran = img_tran.astype(np.uint8) # Apply saturation

    # 이미지 히스토그램 추출
    hist = conv_hist2img(get_histogram(img))
    hist_tran = conv_hist2img(get_histogram(img_tran))

    # Mark the intensity range, 'value_range'
    if value_range[0] >= 0 and value_range[0] <= 255:
        mark = hist[:, value_range[0]] == 255
        hist[mark, value_range[0]] = 200
    if value_range[1] >= 0 and value_range[1] <= 255:
        mark = hist[:, value_range[1]] == 255
        hist[mark, value_range[1]] = 100

    # 모든 이미지 보여주기
    row0 = np.hstack((img, img_tran))
    row1 = np.hstack((hist, hist_tran))
    row1 = cv.resize(row1, (row0.shape[1], 255))
    merge = np.vstack((row0, row1))
    cv.imshow('Contrast Stretching: Original | Stretching', merge)

    # Process the key event
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        value_range[0] += 1
    elif key == ord('-') or key == ord('_'):
        value_range[0] -= 1
    elif key == ord(']') or key == ord('}'):
        value_range[1] += 1
    elif key == ord('[') or key == ord('{'):
        value_range[1] -= 1

cv.destroyAllWindows()
