import cv2 as cv

video_file = 'C:\\Users\\USER\\Desktop\\SYVideo.wmv'
target_format = 'avi'
target_fourcc = 'XVID' # avi 확장자의 코덱

# 주어진 비디오 파일 읽기
video = cv.VideoCapture(video_file)

if video.isOpened():
    target = cv.VideoWriter()
    while True:
        # 비디오에서 이미지 추출
        valid, img = video.read()
        if not valid:
            break

        if not target.isOpened():
            # target video file 열기
            target_file = video_file[:video_file.rfind('.')] + '.' + target_format
            fps = video.get(cv.CAP_PROP_FPS)
            h, w, *_ = img.shape # height, width, channel
            is_color = (img.ndim > 2) and (img.shape[2] > 1)
            # img.ndim : 이미지의 차원 // 주로 3차원 (w*h*channel)
            # img.shape[2] : 채널 // 현재 3
            target.open(target_file, cv.VideoWriter_fourcc(*target_fourcc), fps, (w, h), is_color)
        
        target.write(img)
    
    target.release()
