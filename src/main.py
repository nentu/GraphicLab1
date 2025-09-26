from imports import (
    get_depth_map,
    ObjModel,
    get_intrinsic_matrix,
    Cube,
    Camera,
)
import numpy as np
import cv2
from PositionModel import PositionModel

if __name__ == "__main__":
    plane_shape = np.array([640, 640])
    camera_angle = (90, 90)

    intrinsic_matrix = get_intrinsic_matrix(*camera_angle, *plane_shape)
    # print(angle_coordinates)

    model = PositionModel(
        model=Camera(100),
        intrinsic_matrix=intrinsic_matrix,
    )

    model.move(y=60)

    while True:
        plane = np.zeros(shape=(*plane_shape, 3))

        model.rotate(r=0.3)

        model.draw_model(plane)

        cv2.imshow("depth", plane)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
