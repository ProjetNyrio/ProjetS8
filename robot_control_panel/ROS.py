from pyniryo2 import *
ros_instance = NiryoRos("10.10.10.10") # Hotspot
vision_instance = Vision(ros_instance)

import pyniryo
img_c=vision_instance.get_img_compressed()
img_raw=pyniryo.uncompress_image(img_c)
pyniryo.show_img_and_wait_close("image", img_raw)

ros_instance.close()



