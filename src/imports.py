import sys
import os

script_path = os.path.dirname(os.path.abspath(__file__))

sys.path.append(script_path + "/../3d_reconstruction/src/basic_graphic")
print(sys.path[-1])
from draw_utils import draw_model, get_depth_map
from models.obj_read import ObjModel
from utils import get_intrinsic_matrix, rotate
from models.cube import Cube
from models.camera import Camera as CameraModel
from models.model import Model
