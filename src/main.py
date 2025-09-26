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


def count_inner_coords(p0, p1, p2, x, y):
    return np.int32(
        p0
        + (
            (p1 - p0) / np.linalg.norm(p1 - p0) * x
            + (p2 - p0) / np.linalg.norm(p2 - p0) * y
        )
    )


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
    oArrow.rotate(-45, 0, -48)

    print(triangle.model.vertex_list)
    print(oArrow.model.vertex_list)

    model_list = [triangle, oArrow]
    x = 0
    y = 0
    while True:
        plane = np.zeros(shape=(*plane_shape, 3))

        for model in model_list:
            model.draw_model(plane)

        for i in range(3):
            draw_point_name(triangle, i, f"P{i}", plane)
        p0, p1, p2 = triangle.model.vertex_list
        print("p2=", np.int32(p2))
        point = count_inner_coords(p0, p1, p2, x, y)
        print("point=", point)
        key = cv2.waitKey(0)

        if key == ord("a"):
            x += 1
        elif key == ord("d"):
            x -= 1
        elif key == ord("w"):
            y += 1
        elif key == ord("s"):
            y -= 1

        p_model = PositionModel(model=PointModel(), camera=camera)
        p_model.move(x=point[0], y=point[2], z=point[1])

        p_model.draw_model(plane)

        cv2.imshow("depth", plane)
        # update_camera_pos(key, camera)
        if key == EscCode:
            break

    if "y" in "":  # input("Save cam pos: yes/no: "):
        with open("camera.pickle", "wb") as f:
            pickle.dump(camera, f)
    cv2.destroyAllWindows()
