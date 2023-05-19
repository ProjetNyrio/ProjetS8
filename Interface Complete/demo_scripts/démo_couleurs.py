from pyniryo import *
import cv2

img = cv2.imread("./workspace.jpg")

blue_min_hsv = [60, 35, 40]
blue_max_hsv = [125, 255, 255]

img_threshold_blue = threshold_hsv(img, list_min_hsv=blue_min_hsv,
                                   list_max_hsv=blue_max_hsv, reverse_hue=False)

cv2.imwrite("./after.png", img_threshold_blue)


