from imports import Model
import numpy as np


def _gen_edge_seq():
    res = list()

    res.append([0, 1])
    res.append([1, 2])
    res.append([2, 3])
    res.append([3, 1])
    return np.array(res)


def _get_vertex(r):
    res = [
        [0, 0, 0],
        [r, 0, 0],
        [r * (1 - 0.1), 0.1 * r, 0],
        [r * (1 - 0.1), -0.1 * r, 0],
    ]
    return np.array(res).astype(np.int32)


class ArrowModel(Model):
    def __init__(self, r):
        vertex_list = _get_vertex(r)
        super().__init__(vertex_list, _gen_edge_seq(), list())
