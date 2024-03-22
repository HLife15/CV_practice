import numpy as np
from scipy.spatial.transform import Rotation

# 주어진 3D 회전
euler = (45, 30, 60) # XYZ에서의 [deg]

# 3D 회전 물체 생성
robj = Rotation.from_euler('zyx', euler[::-1], degrees=True)

# 다른 표현
print('\n## Euler Angle (ZYX)')
print(np.rad2deg (robj.as_euler('zyx'))) # ZYX에서의 [60, 30, 45] [deg] 
print('\n## Rotation Matrix')
print(robj.as_matrix())
print('\n## Rotation Vector')
print(robj.as_rotvec()) # [0.97, 0.05, 1.17]
print('\n## Quaternion (XYZW)')
print(robj.as_quat()) # [0.44, 0.02, 0.53, 0.72]
