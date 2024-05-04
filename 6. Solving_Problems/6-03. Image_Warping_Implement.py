import numpy as np
import cv2 as cv

# from homography_estimation_implement import getPerspectiveTransform
def getPerspectiveTransform(src, dst):
    if len(src) == len(dst):
        # Make homogeneous coordiates if necessary
        if src.shape[1] == 2:
            src = np.hstack((src, np.ones((len(src), 1), dtype=src.dtype)))
        if dst.shape[1] == 2:
            dst = np.hstack((dst, np.ones((len(dst), 1), dtype=dst.dtype)))

        # Solve 'Ax = 0'
        A = []
        for p, q in zip(src, dst):
            A.append([0, 0, 0, q[2]*p[0], q[2]*p[1], q[2]*p[2], -q[1]*p[0], -q[1]*p[1], -q[1]*p[2]])
            A.append([q[2]*p[0], q[2]*p[1], q[2]*p[2], 0, 0, 0, -q[0]*p[0], -q[0]*p[1], -q[0]*p[2]])
        _, _, Vt = np.linalg.svd(A, full_matrices=True)
        x = Vt[-1]

        # Reorganize `x` as a matrix
        H = x.reshape(3, -1) / x[-1] # Normalize the last element as 1
        return H

def warpPerspective1(src, H, dst_size):
    # Generate an empty image
    width, height = dst_size
    channel = src.shape[2] if src.ndim > 2 else 1
    dst = np.zeros((height, width, channel), dtype=src.dtype)

    # Copy a pixel from `src` to `dst` (forword mapping)
    for py in range(img.shape[0]):
        for px in range(img.shape[1]):
            q = H @ [px, py, 1]
            qx, qy = int(q[0]/q[-1] + 0.5), int(q[1]/q[-1] + 0.5)
            if qx >= 0 and qy >= 0 and qx < width and qy < height:
                dst[qy, qx] = src[py, px]
    return dst

def warpPerspective2(src, H, dst_size):
    # Generate an empty image
    width, height = dst_size
    channel = src.shape[2] if src.ndim > 2 else 1
    dst = np.zeros((height, width, channel), dtype=src.dtype)

    # Copy a pixel from `src` to `dst` (backward mapping)
    H_inv = np.linalg.inv(H)
    for qy in range(height):
        for qx in range(width):
            p = H_inv @ [qx, qy, 1]
            px, py = int(p[0]/p[-1] + 0.5), int(p[1]/p[-1] + 0.5)
            if px >= 0 and py >= 0 and px < src.shape[1] and py < src.shape[0]:
                dst[qy, qx] = src[py, px]
    return dst

if __name__ == '__main__':
    img = cv.imread('C:\\Users\\USER\\Desktop\\memory.jpg')
    wnd_name = 'Image Warping'
    card_size = (900, 480)
    pts_src = np.array([[95, 243], [743, 121], [157, 652], [969, 372]], dtype=np.float32)
    pts_dst = np.array([[0, 0], [card_size[0], 0], [0, card_size[1]], card_size], dtype=np.float32)

    # Find planar homography and transform the original image
    H = getPerspectiveTransform(pts_src, pts_dst)
    warp1 = warpPerspective1(img, H, card_size)
    warp2 = warpPerspective2(img, H, card_size)

    # Show images generated from two methods
    cv.imshow(wnd_name + ' (Method 1)', warp1)
    cv.imshow(wnd_name + ' (Method 2)', warp2)
    cv.waitKey(0)
    cv.destroyAllWindows()
