from pyniryo import *
from PIL import Image
image = Image.open('worksp.png')

robot = NiryoRobot("10.10.10.10")

status, im_work = extract_img_workspace(image, workspace_ratio=1.0)
# Trying to pick target using camera
obj_found, shape_ret, color_ret = robot.vision_pick(im_work)
if obj_found:
    print("objet trouvé")
robot.set_learning_mode(True)
