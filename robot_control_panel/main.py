import tkinter as tk
from pyniryo2 import *
from video_capture import *
from tkinter import *
from tkinter import messagebox
from PIL import Image

root = tk.Tk()
root.geometry("1300x780")
robot=None

def calibrate_motors():
    robot.arm.calibrate_auto()

def home_pose():
    robot.arm.move_to_home_pose()

def connect_to_robot():
    global robot
    try :
        robot=NiryoRobot("10.10.10.10")
        connect_button.config(bg='green')
    except :
        connect_button.config(bg='red')

def update_tools():
    robot.tool.update_tool()

def select_video():
        # create instance from video capture
        video_source = 0
        vid = VideoCap(video_source, root)
        vid.update()

#A ESSAYER, peut etre meme ajouter un premier appel avant, doc pas claire
def grasp_callback(_msg)
    print("Grasped") 

def release_callback(_msg)
    print("Released") 

def grasp_gripper():
    robot.tool.grasp_with_tool(grasp_callback)

def release_gripper():
    robot.tool.release_with_tool(release_callback)


def get_img():
    img_compressed=vision.get_img_compressed()
    camera_info = vision.get_camera_intrinsics()
    img = pyniryo.uncompress_image(img_compressed)
    img = pyniryo.undistort_image(img, camera_info.intrinsics, camera_info.distortion)


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
Title1= tk.Label(root, text="Connection et calibrage")
Title1.grid(row=0, column=0, columnspan=3, sticky=tk.W)
Title1.configure(font=("Helvetica", 18, "bold"))

blank=tk.Label(root, text="   \n")
blank.grid(row=1, column=0)


#camera_button = tk.Button(root, text="Launch camera stream",height=10, width=16, command=select_video)
#camera_button.grid(row=2, column=3, sticky=tk.W)

calibrate_button = tk.Button(root, text="Calibrate",height=10, width=16, command=calibrate_motors)
calibrate_button.grid(row=2, column=1, sticky=tk.W)

homepose_button = tk.Button(root, text="Homepose",height=10, width=16, command=home_pose)
homepose_button.grid(row=2, column=2, sticky=tk.W)

connect_button = tk.Button(root, text="Connect to robot",height=10, width=16, command=connect_to_robot)
connect_button.grid(row=2, column=0, sticky=tk.W)

update_tools_button = tk.Button(root, text="Update tools",height=10, width=16, command=update_tools)
update_tools_button.grid(row=2, column=3, sticky=tk.W)


blank2=tk.Label(root, text="   \n")
blank2.grid(row=3, column=0)


Title2= tk.Label(root, text="Contrôle du bras")
Title2.grid(row=4, column=0, columnspan=2, sticky=tk.W)
Title2.configure(font=("Helvetica", 18, "bold"))

blank3=tk.Label(root, text="   \n")
blank3.grid(row=5, column=0)

#create a stringvar for each joint of the robot's arm

j1=tk.StringVar()
j2=tk.StringVar()
j3=tk.StringVar()
j4=tk.StringVar()
j5=tk.StringVar()
j6=tk.StringVar()

tk.Label(root, text="j1").grid(row=6, column=0)
tk.Label(root, text="j2").grid(row=6, column=1)
tk.Label(root, text="j3").grid(row=6, column=2)
tk.Label(root, text="j4").grid(row=8, column=0)
tk.Label(root, text="j5").grid(row=8, column=1)
tk.Label(root, text="j6").grid(row=8, column=2)

tk.Entry(root, textvariable=j1).grid(row=7, column=0, sticky=tk.W)
tk.Entry(root, textvariable=j2).grid(row=7, column=1, sticky=tk.W)
tk.Entry(root, textvariable=j3).grid(row=7, column=2, sticky=tk.W)
tk.Entry(root, textvariable=j4).grid(row=9, column=0, sticky=tk.W)
tk.Entry(root, textvariable=j5).grid(row=9, column=1, sticky=tk.W)
tk.Entry(root, textvariable=j6).grid(row=9, column=2, sticky=tk.W)

def generate_command():
    try :
        command=[float(j1.get()),float(j2.get()),float(j3.get()),float(j4.get()),float(j5.get()),float(j6.get())]
    except :
        messagebox.showerror('Error', 'You are sending an incomplete command, input 0 for the joints you dont plan to move')
        return
    try :
        robot.arm.move_joints(command)
    except : 
        messagebox.showerror('Error', 'No robot connection established')

send_command_button = tk.Button(root, text="Send command",height=4, width=10, command=generate_command)
send_command_button.grid(row=6, rowspan=4,  column=3, sticky=tk.S)

blank4=tk.Label(root, text="   \n")
blank4.grid(row=10, column=0)


Title3= tk.Label(root, text="Utilisation du gripper")
Title3.grid(row=11, column=0, columnspan=3, sticky=tk.W)
Title3.configure(font=("Helvetica", 18, "bold"))

blank5=tk.Label(root, text="   \n")
blank5.grid(row=12, column=0)

grasp_button = tk.Button(root, text="Grasp gripper",height=10, width=16, command=grasp_gripper)
grasp_button.grid(row=13, column=0, sticky=tk.W)

release_button = tk.Button(root, text="Release gripper",height=10, width=16, command=release_gripper)
release_button.grid(row=13, column=1, sticky=tk.W)

blank6=tk.Label(root, text="\t")
blank6.grid(row=0, column=6)

Title4= tk.Label(root, text="Caméra")
Title4.grid(row=0, column=7, columnspan=3, sticky=tk.W)
Title4.configure(font=("Helvetica", 18, "bold"))


blank7=tk.Label(root, text="   \n")
blank7.grid(row=1, column=0)


open_camera = tk.Button(root, text="Open camera stream",height=10, width=16, command=get_img)
open_camera.grid(row=2, column=7, sticky=tk.W)



root.mainloop()


