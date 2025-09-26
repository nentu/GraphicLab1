from imports import Model, draw_model, rotate
import numpy as np


class PositionModel:
    def __init__(self, camera, model):
        self.camera = camera
        self.model = model

        self.global_coord = np.array([0, 0, 0])

    def _move(self, x=0, y=0, z=0, move_global=True):
        for i, shift in {
            0: x,
            2: y,
            1: -z,
        }.items():
            self.model.vertex_list[:, i] += shift
        if move_global:
            self.global_coord += [x, y, z]

    def move(self, x=0, y=0, z=0):
        self._move(x, y, z, True)

    def rotate(self, y=0, p=0, r=0):
        self._move(*(-self.global_coord), move_global=False)
        rotate(self.model, p, y, r)
        self._move(*self.global_coord, move_global=False)

    def draw_model(self, plane, color_id):
        y, p, r = self.camera.ypr

        self._move(*(-self.camera.xyz), move_global=False)
        rotate(self.model, p, y, r)
        self.projected_model = self.model.apply_transform(self.camera.intrinsic_matrix)
        rotate(self.model, p, y, r, invert=True)
        self._move(*self.camera.xyz, move_global=False)

        draw_model(plane, self.projected_model, color_id=color_id)
