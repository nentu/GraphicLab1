import numpy as np


class Camera:
    xyz: np.array
    ypr: np.array
    intrinsic_matrix: np.array

    def __init__(
        self,
        intrinsic_matrix: np.array,
        xyz=np.array([0, 0, 0]),
        ypr=np.array([0, 0, 0]),
    ):
        self.xyz = np.array(xyz) * [1, 1, 1]
        self.ypr = np.array(ypr)
        self.intrinsic_matrix = intrinsic_matrix
