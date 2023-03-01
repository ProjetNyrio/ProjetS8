import os.system
import tkinter as tk
from pyniryo import *
from video_capture import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

root = tkinter.Tk()
root.geometry("1300x780")
root.title("Robot control panel")
style = ttk.Style(root)
root.tk.call('source', '../ttkthemes/Azure-ttk-theme/azure.tcl')
root.tk.call('set_theme', 'dark')
global robot
robot=None

def close_connection():
    robot.close_connection()

def home_pose():
    robot.move_to_home_pose()

def learning_mode():
    robot.set_learning_mode(True)

def connect_to_robot():
    global robot
    robot=NiryoRobot("10.10.10.10")
    robot.calibrate_auto()

def update_tools():
    robot.update_tool()

def select_video():
        # create instance from video capture
        video_source = 0
        vid = VideoCap(video_source, root)
        vid.update()

#A ESSAYER, peut etre meme ajouter un premier appel avant, doc pas claire
def grasp_callback(_msg):
    print("Grasped") 

def release_callback(_msg):
    print("Released") 

def grasp_gripper():
    robot.grasp_with_tool()

def release_gripper():
    robot.release_with_tool()

def get_img():
    os.popen("python3 ROS.py")

Title1= ttk.Label(root, text="Connection et calibrage")
Title1.grid(row=0, column=0, columnspan=3, sticky=tk.W)
Title1.configure(font=("Helvetica", 18, "bold"))

blank=ttk.Label(root, text="   \n")
blank.grid(row=1, column=0)

frame1 = ttk.Frame(root)

close_connection_button = ttk.Button(frame1, text="Close connection", command=close_connection)
close_connection_button.grid(row=0, column=2, ipadx=20, ipady=15)

homepose_button = ttk.Button(frame1, text="Homepose", command=home_pose)
homepose_button.grid(row=0, column=1, ipadx=20, ipady=15)

connect_button = ttk.Button(frame1, text="Connect to robot",style="Accent.TButton", command=connect_to_robot)
connect_button.grid(row=0, column=0, ipadx=20, ipady=15)


learning_mode_button = ttk.Button(frame1, text="Learning mode", command=learning_mode)
learning_mode_button.grid(row=0, column=3, ipadx=20, ipady=15)

frame1.grid(row=2, column=0, columnspan=8, sticky=tk.W)

update_tools_button = ttk.Button(root, text="Update tools", command=update_tools)
update_tools_button.grid(row=13, column=0, ipadx=20, ipady=15)


blank2=ttk.Label(root, text="   \n")
blank2.grid(row=3, column=0)


Title2= ttk.Label(root, text="Contrôle du bras")
Title2.grid(row=4, column=0, columnspan=2, sticky=tk.W)
Title2.configure(font=("Helvetica", 18, "bold"))

blank3=ttk.Label(root, text="   \n")
blank3.grid(row=5, column=0)

#create a stringvar for each joint of the robot's arm

j1=tk.StringVar()
j2=tk.StringVar()
j3=tk.StringVar()
j4=tk.StringVar()
j5=tk.StringVar()
j6=tk.StringVar()

ttk.Label(root, text="j1").grid(row=6, column=0)
ttk.Label(root, text="j2").grid(row=6, column=1)
ttk.Label(root, text="j3").grid(row=6, column=2)
ttk.Label(root, text="j4").grid(row=8, column=0)
ttk.Label(root, text="j5").grid(row=8, column=1)
ttk.Label(root, text="j6").grid(row=8, column=2)

ttk.Entry(root, textvariable=j1).grid(row=7, column=0, sticky=tk.W)
ttk.Entry(root, textvariable=j2).grid(row=7, column=1, sticky=tk.W)
ttk.Entry(root, textvariable=j3).grid(row=7, column=2, sticky=tk.W)
ttk.Entry(root, textvariable=j4).grid(row=9, column=0, sticky=tk.W)
ttk.Entry(root, textvariable=j5).grid(row=9, column=1, sticky=tk.W)
ttk.Entry(root, textvariable=j6).grid(row=9, column=2, sticky=tk.W)

def generate_command():
    try :
        command=[float(j1.get()),float(j2.get()),float(j3.get()),float(j4.get()),float(j5.get()),float(j6.get())]
    except :
        messagebox.showerror('Error', 'You are sending an incomplete command, input 0 for the joints you dont plan to move')
        return
    try :
        robot.move_joints(command)
    except : 
        messagebox.showerror('Error', 'No robot connection established')

send_command_button = ttk.Button(root, text="Send command", command=generate_command)
send_command_button.grid(row=6, rowspan=4,  column=3, ipadx=4, ipady=10, sticky=tk.S)

blank4=ttk.Label(root, text="   \n")
blank4.grid(row=10, column=0)


Title3= ttk.Label(root, text="Utilisation du gripper")
Title3.grid(row=11, column=0, columnspan=3, sticky=tk.W)
Title3.configure(font=("Helvetica", 18, "bold"))

blank5=ttk.Label(root, text="   \n")
blank5.grid(row=12, column=0)

grasp_button = ttk.Button(root, text="Grasp gripper", command=grasp_gripper)
grasp_button.grid(row=13, column=1, ipadx=20, ipady=15, sticky=tk.W)

release_button = ttk.Button(root, text="Release gripper", command=release_gripper)
release_button.grid(row=13, column=2, ipadx=20, ipady=15,  sticky=tk.W)

blank6=ttk.Label(root, text="\t")
blank6.grid(row=0, column=6)

Title4= ttk.Label(root, text="Caméra")
Title4.grid(row=0, column=7, columnspan=3, sticky=tk.W)
Title4.configure(font=("Helvetica", 18, "bold"))


blank7=ttk.Label(root, text="   \n")
blank7.grid(row=1, column=0)


open_camera = ttk.Button(root, text="Open camera stream", command=get_img)
open_camera.grid(row=2, column=7, sticky=tk.W)


root.mainloop()


