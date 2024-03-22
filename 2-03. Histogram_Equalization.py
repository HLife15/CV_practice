import matplotlib.pyplot as plt # 그래프를 그려주는 패키지
import cv2 as cv

# 회색 이미지 불러오기
img = cv.imread('C:\\Users\\USER\\Desktop\\kleague.png', cv.IMREAD_GRAYSCALE)

# 히스토그램 균등화
img_tran = cv.equalizeHist(img)

# 히스토그램 나타내기
bin_width = 4 # 기본값 = 1, 반드시 2의 거듭제곱 형태여야 함.
bin_num = int(256/bin_width)
hist = cv.calcHist([img], [0], None, [bin_num], [0, 255])
hist_tran = cv.calcHist([img_tran], [0], None, [bin_num], [0, 255])

# 모든 이미지와 히스토그램 보여주기
plt.subplot(2, 2, 1)
plt.imshow(img, cmap = 'gray')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.plot(range(0, 256, bin_width), hist / 1000)
plt.xlabel('Intensity [0, 255]')
plt.ylabel('Frequency (1k)')
plt.subplot(2, 2, 3)
plt.imshow(img_tran, cmap = 'gray')
plt.axis('off')
plt.subplot(2, 2, 4)
plt.plot(range(0, 256, bin_width), hist_tran / 1000)
plt.xlabel('Intensity [0, 255]')
plt.ylabel('Frequency (1k)')
plt.show()
