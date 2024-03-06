import cv2 as cv

video_file = 'C:\\Users\\USER\\Desktop\\SYVideo.wmv'
video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS) # FPS 값
    wait_msec = int(1 / fps * 1000) # 밀리초 단위의 대기 시간값 계산

    # frame nevigation 구성
    frame_total = int(video.get(cv.CAP_PROP_FRAME_COUNT)) # 총 프레임 수
    frame_shift = 10 # 넘길 때 몇 프레임 넘길지
    speed_table = [1/10, 1/8, 1/4, 1/2, 1, 2, 3, 4, 5, 8, 10] # 영상 속도 옵션
    speed_index = 4 # 기본 속도 인덱스

    while True:
        valid, img = video.read()
        if not valid:
            break
        
        # 이미지 보여주기
        frame = int(video.get(cv.CAP_PROP_POS_FRAMES)) # 현재 프레임 구하기
        info = f'Frame: {frame}/{frame_total}, Speed: x{speed_table[speed_index]:.2g}'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
        cv.imshow('Video Player', img)

        key = cv.waitKey(max(int(wait_msec / speed_table[speed_index]), 1))
        if key == ord(' '): # 스페이스바의 아스키 코드 값과 같을 때 (스페이스바 눌렀을 때)
            key = cv.waitKey()
        if key == 27:
            break
        elif key == ord('\t'): 
            speed_index = 4 # 속도 원상 복구
        elif key == ord('>') or key == ord('.'): # CAPS LOCK 켜져 있을 수도 있어서 키 두개씩 받음
            speed_index = min(speed_index + 1, len(speed_table) - 1) # 속도 줄임
        elif key == ord('<') or key == ord(','):
            speed_index = max(speed_index - 1, 0) # 속도 높임
        elif key == ord(']') or key == ord('}'):
            video.set(cv.CAP_PROP_POS_FRAMES, frame + frame_shift) # 10프레임 뒤로
        elif key == ord('[') or key == ord('{'):
            video.set(cv.CAP_PROP_POS_FRAMES, max(frame - frame_shift, 0)) # 10프레임 앞으로

    cv.destroyAllWindows()
