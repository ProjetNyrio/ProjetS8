import tkinter as tk
import tkinter.filedialog
import cv2
import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
import numpy as np
import random
robot_ip_adress = "10.10.10.10"

class RobotControlPanel(tk.Tk):
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        #connect to robot and calibrate
        self.robot = NiryoRobot(robot_ip_adress)
        self.create_widgets()
    
    def create_widgets(self):
        # Create frame for buttons
        buttons_frame = ttk.Frame(self)
        buttons_frame.grid(row=0, column=0, padx=10, pady=10)

        # Create buttons
        self.forward_button = ttk.Button(buttons_frame, text="Forward", command=self.move_forward)
        self.forward_button.grid(row=0, column=1)
        self.left_button = ttk.Button(buttons_frame, text="Left", command=self.move_left)
        self.left_button.grid(row=1, column=0)
        self.stop_button = ttk.Button(buttons_frame, text="Stop", command=self.stop)
        self.stop_button.grid(row=1, column=1)
        self.right_button = ttk.Button(buttons_frame, text="Right", command=self.move_right)
        self.right_button.grid(row=1, column=2)
        self.backward_button = ttk.Button(buttons_frame, text="Backward", command=self.move_backward)
        self.backward_button.grid(row=2, column=1)

    def move_forward(self):
        self.robot.send_command("F")
        
    def move_left(self):
        self.robot.send_command("L")
        
    def stop(self):
        self.robot.send_command("S")

    def move_right(self):
        self.robot.send_command("R")

    def move_backward(self):
        self.robot.send_command("B")
        
    def close_conn(self):
        self.robot.close()
        self.destroy()

if __name__ == "__main__":
    control_panel = RobotControlPanel(tk.Tk(), 'Robot Control Panel')
    control_panel.protocol("WM_DELETE_WINDOW", control_panel.close_conn)
    control_panel.mainloop()

