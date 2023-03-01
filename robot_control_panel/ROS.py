from pyniryo2 import *
ros_instance = NiryoRos("10.10.10.10") # Hotspot
vision_instance = Vision(ros_instance)

import pyniryo
while "User do not press Escape neither q":
    img_c=vision_instance.get_img_compressed()
    img_raw=pyniryo.uncompress_image(img_c)
    key = pyniryo.show_img("Images raw & undistorted", img_raw, wait_ms=30)
    if key in [27, ord("q")]:  # Will break loop if the user press Escape or Q
        break

ros_instance.close()



