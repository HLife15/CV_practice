import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png')

if img is not None:
    # Negative 이미지
    img_nega = cv.bitwise_not(img) # img_nega = 255 - img

    # 수직 반전 이미지 (0 : 상하, 1 : 좌우)
    img_flip = cv.flip(img, 0) # img_flip = img[::-1,:,:]

    # 모든 이미지 보여주기
    merge = cv.hconcat((img, img_nega, img_flip)) # merge = np.hstack((img, img_nega, img_flip))
    cv.imshow('Image Editing: Original | Negative | Flip', merge)
    cv.waitKey()
    cv.destroyAllWindows()
