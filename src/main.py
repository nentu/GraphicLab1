import os
import pickle
import numpy as np
import cv2

from imports import (
    get_depth_map,
    ObjModel,
    get_intrinsic_matrix,
    Cube,
    CameraModel,
)

from PositionModel import PositionModel
from Camera import Camera
from models.Arrow import ArrowModel
from models.Triangle import TriangleModel
from models.Point import PointModel
from main_utils import update_camera_pos, EscCode, draw_point_name
from ECounter import (
    count_local_coords,
    normal_vector,
    count_alpha,
    count_theta,
    count_e,
)


def create_grid(min, max, step):
    res = list()
    for x in np.arange(min, max, step):
        for y in np.arange(min, max, step):
            res.append([x, y])

    return res


if __name__ == "__main__":
    plane_shape = np.array([640, 640])
    camera_angle = (90, 90)

    intrinsic_matrix = get_intrinsic_matrix(*camera_angle, *plane_shape)
    if os.path.isfile("camera.pickle"):
        with open("camera.pickle", "rb") as f:
            camera = pickle.load(f)
    else:
        camera = Camera(
            xyz=[-97, -112, 77],
            ypr=[6, -10, 0],
            intrinsic_matrix=intrinsic_matrix,
        )

    triangle = PositionModel(model=TriangleModel(30), camera=camera)
    oArrow = PositionModel(model=ArrowModel(30), camera=camera)
    oArrow.move(-100, 100, 100)
    oArrow.rotate(-45, 0, 0)

    print(triangle.model.vertex_list)
    print(oArrow.model.vertex_list)

    model_list = [triangle, oArrow]
    x = 1
    y = 1
    while True:
        plane = np.ones(shape=(*plane_shape, 3), dtype=np.uint8) * 255

        for i, model in enumerate(model_list):
            model.draw_model(plane, -i)

        for i in range(3):
            draw_point_name(triangle, i, f"P{i}", plane)
        p0, p1, p2 = triangle.model.vertex_list
        # print("p2=", np.int32(p2))
        l_point = count_local_coords(p0, p1, p2, x, y)
        n_point = normal_vector(p0, p1, p2) * 30
        n_point += l_point
        print("n_point=", n_point)
        key = cv2.waitKey(0)

        if key == ord("j"):
            x += 1
        elif key == ord("l"):
            x -= 1
        elif key == ord("i"):
            y += 1
        elif key == ord("k"):
            y -= 1

        p_model = PositionModel(model=PointModel(), camera=camera)
        p_model.move(x=l_point[0], y=l_point[2], z=l_point[1])

        pl = oArrow.model.vertex_list[0]
        po = oArrow.model.vertex_list[1]
        # alpha = count_alpha(l_point, p0, p1, p2, pl)
        # theta = count_theta(po, pl, l_point)
        e_rgb = count_e(1e6, po, pl, l_point, p0, p1, p2)
        # print(f"{pl=}")
        # print("a =", alpha / np.pi * 180)
        # print("o =", theta / np.pi * 180)
        # print("E_rgb =", e_rgb)

        p_model.draw_model(plane, int(e_rgb))
        draw_point_name(p_model, 0, "L", plane)

        n_model = PositionModel(model=PointModel(), camera=camera)
        n_model.move(x=n_point[0], y=n_point[2], z=n_point[1])
        n_model.draw_model(plane, -3)
        draw_point_name(n_model, 0, "N", plane)

        for _x, _y in create_grid(-100, 100, 10):
            l_point = count_local_coords(p0, p1, p2, _x, _y)
            e_rgb = count_e(1e6, po, pl, l_point, p0, p1, p2)
            e_rgb = np.clip(e_rgb, 0, 30) / 30 * 99
            p_model = PositionModel(model=PointModel(), camera=camera)
            p_model.move(x=l_point[0], y=l_point[2], z=l_point[1])
            p_model.draw_model(plane, int(e_rgb))

        cv2.imshow("depth", plane)
        update_camera_pos(key, camera)
        if key == EscCode:
            break

    if "y" in "":  # input("Save cam pos: yes/no: "):
        with open("camera.pickle", "wb") as f:
            pickle.dump(camera, f)
    cv2.destroyAllWindows()
