from imports import Model
import numpy as np


def _gen_edge_seq():
    res = [[0, 1], [0, 2]]
    return np.array(res)


def _get_vertex(r):
    res = [[0, 0, 0], [-r, 0, 0], [-r * np.cos(np.pi / 4), 0, r * np.sin(np.pi / 4)]]
    return np.array(res).astype(np.int32)


class TriangleModel(Model):
    def __init__(self, r):
        vertex_list = _get_vertex(r)
        super().__init__(vertex_list, _gen_edge_seq(), list())
