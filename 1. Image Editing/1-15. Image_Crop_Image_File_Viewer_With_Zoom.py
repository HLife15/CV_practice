import numpy as np
import cv2 as cv

def mouse_event_handler(event, x, y, flags, param):
    if event == cv.EVENT_MOUSEMOVE:
        param[0] = x
        param[1] = y

def image_viewer(img_file, zoom_level=10, zoom_box_radius=5, zoom_box_margin=10):
    img = cv.imread(img_file)
    if img is None:
        return False
    img_height, img_width, *_ = img.shape

    cv.namedWindow('Image Viewer')
    mouse_xy = [-1, -1]
    cv.setMouseCallback('Image Viewer', mouse_event_handler, mouse_xy)

    while True:
        img_copy = img.copy()
        if mouse_xy[0] >= zoom_box_radius and mouse_xy[0] < (img_width - zoom_box_radius) and \
            mouse_xy[0] >= zoom_box_radius and mouse_xy[1] < (img_height - zoom_box_radius):
            img_crop = img[mouse_xy[1]-zoom_box_radius:mouse_xy[1]+zoom_box_radius, \
                           mouse_xy[0]-zoom_box_radius:mouse_xy[0]+zoom_box_radius, :]
            
            zoom_box = cv.resize(img_crop, None, None, zoom_level, zoom_level)

            s = zoom_box_margin
            e = zoom_box_margin + len(zoom_box)
            img_copy[s:e, s:e, :] = zoom_box

        cv.imshow('Image Viewer', img_copy)
        key = cv.waitKey(10)
        if key == 27: # ESC
            break
    
    cv.destroyAllWindows()
    return True

if __name__ == '__main__':
    img_file = 'C:\\Users\\USER\\Desktop\\kleague.png'
    if not image_viewer(img_file):
        print(f'Cannot open the given file, {img_file}.')
