from imports import Model, draw_model, rotate


class PositionModel:
    def __init__(self, model, xyz, ypr, intrinsic_matrix):
        self.model = model
        self.xyz = xyz
        self.ypr = ypr
        self.intrinsic_matrix = intrinsic_matrix

        self.move(*xyz)
        self.rotate(*ypr)

    def move(self, x=0, y=0, z=0):
        for i, shift in {
            0: x,
            1: y,
            2: z,
        }.items():
            self.model.vertex_list[:, i] += shift

    def rotate(self, y=0, p=0, r=0):
        rotate(self.model, y, p, r)

    def draw_model(self, plane):
        projected_model = self.model.apply_transform(self.intrinsic_matrix)
        draw_model(plane, projected_model)
