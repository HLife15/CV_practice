import cv2 as cv
import numpy as np

# 이미지 흑백으로 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)

if img is not None:
    # 기본 설정
    contrast = 1.6
    contrast_step = 0.1
    brightness = -40
    brightness_step = 1

    while True:
        img_tran = contrast * img + brightness
        img_tran[img_tran < 0] = 0
        img_tran[img_tran > 255] = 255
        img_tran = img_tran.astype(np.uint8)

        merge = cv.hconcat((img, img_tran))
        cv.imshow('Image Editing: Original | BO', merge)
        
        key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('+') or key == ord('='):
            contrast += contrast_step
        elif key == ord('-') or key == ord('_'):
            contrast -= contrast_step
        elif key == ord(']') or key == ord('}'):
            brightness += brightness_step
        elif key == ord('[') or key == ord('{'):
            brightness -= brightness_step

    cv.destroyAllWindows()    
