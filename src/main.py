from imports import (
    draw_model,
    get_depth_map,
    ObjModel,
    get_intrinsic_matrix,
    rotate,
    Cube,
    Camera,
)
import numpy as np
import cv2

if __name__ == "__main__":
    plane_shape = np.array([640, 640])
    camera_angle = (90, 90)

    intrinsic_matrix = get_intrinsic_matrix(*camera_angle, *plane_shape)
    # print(angle_coordinates)

    shift = 0
    rotation = 180

    h = 0
    k = 1

    while True:
        plane = np.zeros(shape=(*plane_shape, 3))

        model = Camera(99)

        # model.vertex_list[:, 1] -= 0.5

        rotate(model, 180, rotation, 0)
        model.vertex_list[:, 2] += 300 + shift

        # plane += 255

        projected_model = model.apply_transform(intrinsic_matrix)

        draw_model(plane, projected_model)

        cv2.imshow("depth", plane)
        if cv2.waitKey(1) == ord("q"):
            break

        shift += 1
        rotation += 0.2
        # k += 2e-3

    cv2.destroyAllWindows()
