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
from main_utils import update_camera_pos, EscCode, draw_point_name


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

    model_list = [triangle, oArrow]
    while True:
        plane = np.zeros(shape=(*plane_shape, 3))

        for model in model_list:
            model.draw_model(plane)

        for i in range(3):
            draw_point_name(triangle, i, f"P{i}", plane)
        # oArrow.rotate(0, 0, 1)

        cv2.imshow("depth", plane)
        key = cv2.waitKey(1)
        update_camera_pos(key, camera)
        if key == EscCode:
            break

    if "y" in "":  # input("Save cam pos: yes/no: "):
        with open("camera.pickle", "wb") as f:
            pickle.dump(camera, f)
    cv2.destroyAllWindows()
