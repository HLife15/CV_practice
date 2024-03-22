import numpy as np
import cv2 as cv

img1 = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png')
img2 = cv.imread('C:\\Users\\USER\\Desktop\\example.png')

if img1 is not None and img2 is not None:
    alpha = 0.5

    while True:
        blend = (alpha * img1 + (1 - alpha) * img2).astype(np.uint8)

        # 모든 이미지 보여주기
        info = f'Alpha: {alpha:.1f}'
        cv.putText(blend, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
        cv.putText(blend, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
        merge = np.hstack((img1, img2, blend))
        cv.imshow('Image Blending: Image1 | Image2 | Blended', merge)

        # 키 이벤트 설정
        key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('+') or key == ord('='):
            alpha = min(alpha + 0.1, 1)
        elif key == ord('-') or key == ord('_'):
            alpha = max(alpha - 0.1, 0)

    cv.destroyAllWindows()
