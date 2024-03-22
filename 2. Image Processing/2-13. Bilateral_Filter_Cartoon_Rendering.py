import numpy as np
import cv2 as cv

# 이미지 리스트 불러오기
img_list = [
    'C:\\Users\\USER\\Desktop\\kleague.png',
    'C:\\Users\\USER\\Desktop\\example.png',
    'C:\\Users\\USER\\Desktop\\botkaku.png',
    'C:\\Users\\USER\\Desktop\\fxxk.png',
    'C:\\Users\\USER\\Desktop\\profile.png',
    'C:\\Users\\USER\\Desktop\\profile4.png']

# 컨트롤 파라미터 초기화
kernel_size = 9
sigma_color = 150
sigma_space = 2.4
n_iterations = 1
img_select = 0

while True:
    # 이미지 불러오기
    img = cv.imread(img_list[img_select])
    assert img is not None, 'Cannot read the given image, ' + img_list[img_select]

    # 양방향 필터를 반복적으로 적용
    result = img.copy()
    for itr in range(n_iterations):
        result = cv.bilateralFilter(result, kernel_size, sigma_color, sigma_space)

    # 모든 이미지 보여주기
    info = f'KSize: {kernel_size}, SColor: {sigma_color}, SSpace: {sigma_space:.1f}, NIter: {n_iterations}'
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 255, thickness=2)
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, 0)
    merge = np.hstack((img, result))
    cv.imshow('Bilateral Filter: Original | Result', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        kernel_size = kernel_size + 2
    elif key == ord('-') or key == ord('_'):
        kernel_size = max(kernel_size - 2, -1)
    elif key == ord(']') or key == ord('}'):
        sigma_color += 2
    elif key == ord('[') or key == ord('{'):
        sigma_color -= 2
    elif key == ord('>') or key == ord('.'):
        sigma_space += 0.1
    elif key == ord('<') or key == ord(','):
        sigma_space -= 0.1
    elif key == ord(')') or key == ord('0'):
        n_iterations += 1
    elif key == ord('(') or key == ord('9'):
        n_iterations = max(n_iterations - 1, 1)
    elif key == ord('\t'):
        img_select = (img_select + 1) % len(img_list)

cv.destroyAllWindows()
