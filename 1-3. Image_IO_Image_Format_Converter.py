import cv2 as cv

img_file = 'C:\\Users\\USER\\Desktop\\kleague.png'
target_format = 'jpg' # 바꿀 확장자

img = cv.imread(img_file)

if img is not None:
    target_file = img_file[:img_file.rfind('.')] + '.' + target_format
    # kleague.png 에서 .png[. 이후 부분]을 지우고 .target_format[jpg] 를 붙인다
    cv.imwrite(target_file, img) # jpg 이미지 저장
