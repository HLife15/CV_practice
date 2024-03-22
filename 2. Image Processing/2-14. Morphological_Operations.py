import cv2 as cv
import numpy as np

# morphological operations과 커널 정리
morph_operations = [
    {'name': 'Erode',     'operation': cv.MORPH_ERODE},  # Alternative) cv.erode()
    {'name': 'Dilate',    'operation': cv.MORPH_DILATE}, # Alternative) cv.dilate()
    {'name': 'Open',      'operation': cv.MORPH_OPEN},
    {'name': 'Close',     'operation': cv.MORPH_CLOSE},
    {'name': 'Gradient',  'operation': cv.MORPH_GRADIENT},
    {'name': 'Tophat',    'operation': cv.MORPH_TOPHAT},
    {'name': 'Blackhat',  'operation': cv.MORPH_BLACKHAT},
    {'name': 'Hitmiss',   'operation': cv.MORPH_HITMISS},
]

kernel_tables = [
    {'name': '3x3 Box',   'kenerl': np.ones((3, 3), dtype=np.uint8)},
    {'name': '5x5 Box',   'kenerl': np.ones((5, 5), dtype=np.uint8)},
    {'name': '5x1 Bar',   'kernel': np.ones((5, 1), dtype=np.uint8)},
    {'name': '1x5 Bar',   'kernel': np.ones((1, 5), dtype=np.uint8)},
    {'name': '5x5 Cross', 'kernel': np.array([[0,0,1,0,0], [0,0,1,0,0], [1,1,1,1,1], [0,0,1,0,0], [0,0,1,0,0]], dtype=np.uint8)},
]

# 흑백 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)
assert img is not None, 'Cannot read the given image'

# 컨트롤 파라미터 초기화
morph_select = 0
kernel_select = 0
n_iterations = 1

while True:
    # 커널과 함께 이미지에 morphological operation 적용
    m_name, operation = morph_operations[morph_select].values() # Make alias
    k_name, kernel = kernel_tables[kernel_select].values()      # Make alias
    result = cv.morphologyEx(img, operation, kernel, iterations=n_iterations)

    # 모든 이미지 보여주기
    info = f'{m_name}({n_iterations}) with {k_name}'
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 255), thickness=2)
    cv.putText(result, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0))
    merge = np.hstack((img, result))
    cv.imshow('Morphological Operation: Original | Result', merge)

    # 키 설정
    key = cv.waitKey()
    if key == 27: # ESC
        break
    elif key == ord('+') or key == ord('='):
        morph_select = (morph_select + 1) % len(morph_operations)
    elif key == ord('-') or key == ord('_'):
        morph_select = (morph_select - 1) % len(morph_operations)
    elif key == ord(']') or key == ord('}'):
        kernel_select = (kernel_select + 1) % len(kernel_tables)
    elif key == ord('[') or key == ord('{'):
        kernel_select = (kernel_select - 1) % len(kernel_tables)
    elif key == ord(')') or key == ord('0'):
        n_iterations += 1
    elif key == ord('(') or key == ord('9'):
        n_iterations = max(n_iterations - 1, 1)

cv.destroyAllWindows()
