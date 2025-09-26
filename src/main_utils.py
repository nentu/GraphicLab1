import cv2

UpCode = 82
RightCode = 83
DownCode = 84
LeftCode = 81
EscCode = 27


def update_camera_pos(key, camera):
    if key == ord("a"):
        camera.xyz[0] += -1
    elif key == ord("d"):
        camera.xyz[0] += 1
    elif key == ord("w"):
        camera.xyz[1] += 1
    elif key == ord("s"):
        camera.xyz[1] += -1
    elif key == ord("q"):
        camera.xyz[2] += 1
    elif key == ord("e"):
        camera.xyz[2] += -1

    if key == RightCode:
        camera.ypr[0] += 1
    elif key == LeftCode:
        camera.ypr[0] += -1
    elif key == UpCode:
        camera.ypr[1] += 1
    elif key == DownCode:
        camera.ypr[1] += -1


def draw_point_name(model, point_id, name, plane):
    plane_coord = list(map(int, model.projected_model.vertex_list[point_id, :2]))

    plane = cv2.putText(
        img=plane,
        text=name,
        org=plane_coord,
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=0.5,
        color=(125, 246, 55),
        thickness=1,
    )
