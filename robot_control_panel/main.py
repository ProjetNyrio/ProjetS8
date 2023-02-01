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
    try :
        robot=NiryoRobot("10.10.10.10")
        connect_button.config(bg='green')
    except :
        connect_button.config(bg='red')

def select_video():
        # create instance from video capture
        video_source = 0
        vid = VideoCap(video_source, root)
        vid.update()

"""
j1_button = tk.Button(root, text="Up", height=10, width=20, command=move_up)
j1_button.grid(row=0, column=0)

down_button = tk.Button(root, text="Down",height=10, width=20, command=move_down)
down_button.grid(row=0, column=1)

left_button = tk.Button(root, text="Left",height=10, width=20, command=move_left)
left_button.grid(row=0, column=2)

right_button = tk.Button(root, text="Right",height=10, width=20, command=move_right)
right_button.grid(row=0, column=3)
"""
Title1= tk.Label(root, text="Connection and calibration functions")
Title1.grid(row=0, column=0)

camera_button = tk.Button(root, text="Launch camera stream",height=10, width=20, command=select_video)
camera_button.grid(row=1, column=3)

calibrate_button = tk.Button(root, text="Calibrate",height=10, width=20, command=calibrate_motors)
calibrate_button.grid(row=1, column=1)

homepose_button = tk.Button(root, text="Homepose",height=10, width=20, command=home_pose)
homepose_button.grid(row=1, column=2)

connect_button = tk.Button(root, text="Connect to robot",height=10, width=20, command=connect_to_robot)
connect_button.grid(row=1, column=0)

Title2= tk.Label(root, text="Control robot's arm", anchor=tk.E)
Title2.grid(row=2, column=0)

#create a stringvar for each joint of the robot's arm

j1=tk.StringVar()
j2=tk.StringVar()
j3=tk.StringVar()
j4=tk.StringVar()
j5=tk.StringVar()
j6=tk.StringVar()

tk.Label(root, text="j1").grid(row=3, column=0)
tk.Label(root, text="j2").grid(row=3, column=1)
tk.Label(root, text="j3").grid(row=3, column=2)
tk.Label(root, text="j4").grid(row=3, column=3)
tk.Label(root, text="j5").grid(row=3, column=4)
tk.Label(root, text="j6").grid(row=3, column=5)

tk.Entry(root, textvariable=j1).grid(row=4, column=0)
tk.Entry(root, textvariable=j2).grid(row=4, column=1)
tk.Entry(root, textvariable=j3).grid(row=4, column=2)
tk.Entry(root, textvariable=j4).grid(row=4, column=3)
tk.Entry(root, textvariable=j5).grid(row=4, column=4)
tk.Entry(root, textvariable=j6).grid(row=4, column=5)

def generate_command():
    command=[float(j1.get()),float(j2.get()),float(j3.get()),float(j4.get()),float(j5.get()),float(j6.get())]
    for i in range(len(command)): 
        print(command[i])

send_command_button = tk.Button(root, text="Send command",height=5, width=5, command=generate_command)
send_command_button.grid(row=4, column=6)



root.mainloop()


