import time
import os
import tkinter as tk
from video_canvas import *
from pyniryo import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1120x600")
root.title("Robot control panel")
style = ttk.Style(root)
root.tk.call('source', '../ttkthemes/Azure-ttk-theme/azure.tcl')
root.tk.call('set_theme', 'dark')
global robot
robot=None
root.video_canvas1=None

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

def grasp_callback(_msg):
    print("Grasped") 

def release_callback(_msg):
    print("Released") 

def grasp_gripper():
    robot.grasp_with_tool()

def release_gripper():
    robot.release_with_tool()

def get_img():
    if (root.video_canvas1 != None):
        root.video_canvas1.stream_on = True
    else :
        root.video_canvas1 = video_canvas(video_frame)

def capture_img():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("All files", "*.*")])
    if not filename:
        return
    video_canvas1.image.save(filename)

def end_stream():
    root.video_canvas1.__stop_stream__()

def window_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        if (root.video_canvas1 != None):
            root.video_canvas1.ros_instance.close()
        root.destroy()

Title1= ttk.Label(root, text="Connection et calibrage")
Title1.grid(row=0, column=0, columnspan=3, sticky=tk.W)
Title1.configure(font=("Helvetica", 18, "bold"))

blank=ttk.Label(root, text="   \n")
blank.grid(row=1, column=0)

frame1 = ttk.Frame(root)

close_connection_button = ttk.Button(frame1, text="Close connection", command=close_connection)
close_connection_button.grid(row=0, column=2, ipadx=20, ipady=15)

homepose_button = ttk.Button(frame1, text="  Homepose  ", command=home_pose)
homepose_button.grid(row=0, column=1, ipadx=30, ipady=15)

connect_button = ttk.Button(frame1, text="Connect to robot",style="Accent.TButton", command=connect_to_robot)
connect_button.grid(row=0, column=0, ipadx=20, ipady=15)


learning_mode_button = ttk.Button(frame1, text=" Learning mode ", command=learning_mode)
learning_mode_button.grid(row=0, column=3, ipadx=22, ipady=15)

frame1.grid(row=2, column=0, columnspan=8, sticky=tk.W)

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
send_command_button.grid(row=6, rowspan=4,  column=3, ipadx=18, ipady=12, sticky="sw")

blank4=ttk.Label(root, text="   \n")
blank4.grid(row=10, column=0)

tools_frame=ttk.Frame(root)
Title3= ttk.Label(tools_frame, text="Utilisation du gripper")
Title3.grid(row=0, column=0, columnspan=3, sticky=tk.W)
Title3.configure(font=("Helvetica", 18, "bold"))

blank5=ttk.Label(tools_frame, text="   \n")
blank5.grid(row=1, column=0)

grasp_button = ttk.Button(tools_frame, text=" Grasp gripper ",command=grasp_gripper)
grasp_button.grid(row=2, column=1,rowspan=2, ipadx=26, ipady=15, sticky="nsew")

release_button = ttk.Button(tools_frame, text="Release gripper", command=release_gripper)
release_button.grid(row=2, column=2,rowspan=2, ipadx=24, ipady=15, sticky="nsew")

update_tools_button = ttk.Button(tools_frame, text=" Update tools ", command=update_tools)
update_tools_button.grid(row=2, column=0,rowspan=2, ipadx=28, ipady=15, sticky="nsew")

tools_frame.grid(row=11, column=0, columnspan=4, rowspan=5, sticky=tk.W)


blank6=ttk.Label(root, text="\t")
blank6.grid(row=0, column=6)

Title4= ttk.Label(root, text="Caméra")
Title4.grid(row=0, column=7, columnspan=3, sticky=tk.W)
Title4.configure(font=("Helvetica", 18, "bold"))


blank7=ttk.Label(root, text="   \n")
blank7.grid(row=1, column=0)


open_camera = ttk.Button(root, text="Open camera stream", command=get_img)
open_camera.grid(row=2, column=7, ipadx=10, ipady=10, sticky=tk.W)

video_frame_style=ttk.Style()
video_frame_style.configure("video.TFrame", background="#4A4A4A")
video_frame = ttk.Frame(root, style="video.TFrame", height=300, width=300)

end_stream_button = ttk.Button(root, text="End camera stream", command=end_stream)
end_stream_button.grid(row=11, column=7, ipadx=10, ipady=10, sticky=tk.W)

capture_image_button = ttk.Button(root, text="Enregistrer l'image", command=capture_img)
capture_image_button.grid(row=11, column=8, ipadx=10, ipady=10, sticky=tk.W) 
video_frame.grid(row=3, column=7, rowspan=8, columnspan=2, sticky=tk.W)

root.protocol("WM_DELETE_WINDOW", window_closing)
root.mainloop()


