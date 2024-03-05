import cv2 as cv

video_file = 'C:\\Users\\USER\\Desktop\\SYVideo.wmv'
# ▼ 추가 예시
# image sequence 의 경우 : video_file = 'C:\\Users\\USER\\Desktop\\SYVideo_%04d.png'
# camera 의 경우 : video_file = 0 (카메라가 한 대 연결되어 있을 때의 index 값)

# 주어진 비디오 파일 읽기
video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS) # FPS 값
    wait_msec = int(1 / fps * 1000) # 밀리초 단위의 대기 시간값 계산

    while True:
        # 영상으로부터 이미지 읽기
        valid, img = video.read()
        if not valid: # ex) 영상이 끝났을 때...
            break
        
        # 이미지 보여주기
        cv.imshow('Video Player', img)

        # ESC 눌렀을 때 중지
        key = cv.waitKey(wait_msec)
        if key == 27:
            break
    
    cv.destroyAllWindows()
