import numpy as np

I = 10

o_point = [-100, -100, 100]
pl_point = [-85, -84, 78]

p0 = np.array([0, 0, 0])
p1 = np.array([-30, 0, 0])
p2 = np.array([-21, 0, 21])


x = 0
y = 0


def count_e(i_rgb, theta, alpha, r):
    return (i_rgb * np.cos(theta) * np.cos(alpha)) / (r**2)
