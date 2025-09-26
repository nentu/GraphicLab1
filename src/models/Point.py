from imports import Model
import numpy as np


def _get_vertex():
    res = [[0, 0, 0]]
    return np.array(res).astype(np.int32)


class PointModel(Model):
    def __init__(self):
        vertex_list = _get_vertex()
        super().__init__(vertex_list, list(), list())
