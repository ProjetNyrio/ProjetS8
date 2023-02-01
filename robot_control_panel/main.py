import tkinter as tk
from pyniryo2 import *
from video_capture import *

root = tk.Tk()
root.geometry("1400x900")

def move_up():
    print("Moving up")

def move_down():
    print("Moving down")

def move_left():
    print("Moving left")

def move_right():
    print("Moving right")

def calibrate_motors():
    if (arm.need_calibration()):
        robot.arm.calibrate_auto()
    else:
        robot.arm.request_new_calibration()

def home_pose():
    robot.move_to_homepose()


def connect_to_robot():
    robot=NiryoRobot("10.10.10.10")

def select_video():
        # create instance from video capture
        video_source = 0
        vid = VideoCap(video_source, root)
        vid.update()

"""
up_button = tk.Button(root, text="Up", height=10, width=20, command=move_up)
up_button.grid(row=0, column=0)

down_button = tk.Button(root, text="Down",height=10, width=20, command=move_down)
down_button.grid(row=0, column=1)

left_button = tk.Button(root, text="Left",height=10, width=20, command=move_left)
left_button.grid(row=0, column=2)

right_button = tk.Button(root, text="Right",height=10, width=20, command=move_right)
right_button.grid(row=0, column=3)
"""
camera_button = tk.Button(root, text="Launch camera stream",height=10, width=20, command=select_video)
camera_button.grid(row=0, column=0)

calibrate_button = tk.Button(root, text="Calibrate",height=10, width=20, command=calibrate_motors)
calibrate_button.grid(row=0, column=1)

homepose_button = tk.Button(root, text="Homepose",height=10, width=20, command=home_pose)
homepose_button.grid(row=0, column=2)

connect_button = tk.Button(root, text="Connect to robot",height=10, width=20, command=connect_to_robot)
connect_button.grid(row=0, column=3)



root.mainloop()


