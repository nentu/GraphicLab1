import numpy as np

I = 10

o_point = [-100, -100, 100]
pl_point = [-85, -84, 78]

p0 = np.array([0, 0, 0])
p1 = np.array([-30, 0, 0])
p2 = np.array([-21, 0, 21])


x = 0
y = 0


def count_local_coords(p0, p1, p2, x, y):
    return np.int32(
        p0
        + (
            (p1 - p0) / np.linalg.norm(p1 - p0) * x
            + (p2 - p0) / np.linalg.norm(p2 - p0) * y
        )
    )


def normal_vector(p0, p1, p2):
    n_vec = (p2 - p0) * (p1 - p0)
    n_vec = np.cross((p1 - p0), (p2 - p0))
    return np.int32(n_vec / (np.linalg.norm(n_vec)))


def count_alpha(l_point, p0, p1, p2, pl):
    n = normal_vector(p0, p1, p2)
    s = l_point - pl
    return np.arccos((n * s).sum() / (np.linalg.norm(s)))


def count_theta(o, pl, l_point):
    v1 = o - pl
    v2 = l_point - pl
    return np.arccos((v1 * v2).sum() / (np.linalg.norm(v1) * np.linalg.norm(v2)))


def count_e(
    i_rgb,
    o,
    pl,
    l_point,
    p0,
    p1,
    p2,
):
    theta = count_theta(o, pl, l_point)
    alpha = count_alpha(l_point, p0, p1, p2, pl)
    # print(f"theta={theta / np.pi * 180}")
    # print(f"alpha={alpha / np.pi * 180}")
    r = np.linalg.norm(pl - l_point)
    # print(f"{r=}")
    return (i_rgb * np.cos(theta) * np.cos(alpha)) / (r**2)
