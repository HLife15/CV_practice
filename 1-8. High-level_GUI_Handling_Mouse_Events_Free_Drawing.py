import cv2 as cv
import numpy as np

def mouse_event_handler(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 누르고 있을 때
        param[0] = True # 그림 그려지는 중
        param[1] = (x, y) # 현재 마우스 좌표
    elif event == cv.EVENT_LBUTTONUP:
        param[0] = False
    elif event == cv.EVENT_MOUSEMOVE and param[0]: # 마우스 누른 채 이동하면
        param[1] = (x, y) # 계속 마우스 좌표 업데이트

# init_brush_radius = 3 // 반지름 3의 원으로 브러시 모양 설정
def free_drawing(canvas_width=640, canvas_height=480, init_brush_radius=3):
    # 캔버스와 팔레트 준비
    canvas = np.full((canvas_height, canvas_width, 3), 255, dtype=np.uint8)
    palette = [(0 ,0 ,0), (255 ,255 ,255), (0, 0, 255), (0, 255, 0), (255 ,0 ,0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    
    # 초기 설정
    mouse_state = [False, (-1, -1)] # [마우스 왼클릭, 마우스 좌표]
    brush_color = 0 # palette[0]
    brush_radius = init_brush_radius

    # 이벤트들이 발생할 윈도우 띄우고 마우스 콜백 함수 등록
    cv.namedWindow('Free Drawing')
    cv.setMouseCallback('Free Drawing', mouse_event_handler, mouse_state)

    while True:
        # 점 그리기
        mouse_left_button_click, mouse_xy = mouse_state
        if mouse_left_button_click:
            cv.circle(canvas, mouse_xy, brush_radius, palette[brush_color], -1)

        # 캔버스 보여주기
        canvas_copy = canvas.copy()
        info = f'Brush Radius : {brush_radius}'
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (127, 127, 127), thickness=2)
        cv.putText(canvas_copy, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, palette[brush_color])
        cv.imshow('Free Drawing', canvas_copy)

        # key event 진행
        key = cv.waitKey(1)
        if key == 27:
            break
        elif key == ord('\t'):
            brush_color = (brush_color + 1) % len(palette) # 나머지 연산 (색깔키 계속 누르면 다시 처음으로 가게)
        elif key == ord('+') or key == ord('='):
            brush_radius += 1
        elif key == ord('-') or key == ord('_'):
            brush_radius = max(brush_radius - 1, 1)
    
    cv.destroyAllWindows()

if __name__ == '__main__':
    free_drawing()
