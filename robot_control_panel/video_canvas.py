import tkinter as tk
from tkinter.messagebox import showerror
from pyniryo2 import *
from PIL import ImageTk, Image
import threading
import time
import cv2

class video_canvas(tk.Canvas):

    def __init__(self, parent):
        self.parent = parent
        self.stream_on = True
        self.interval = 5
        img = Image.open("./images/no_image.jpg")
        resized = img.resize((300,300))
        self.no_image=ImageTk.PhotoImage(resized)
        self.image=None
        self.canvas = tk.Canvas(self.parent, width=300, height=300)
        self.canvas.grid(row=0, column=0)
        self.image_container = self.canvas.create_image(0,0, anchor="nw",image=self.no_image) 
        try :
            self.ros_instance=NiryoRos("10.10.10.10")
            self.vision_instance=Vision(self.ros_instance)
            self.update_image()
        except : 
            showerror(title = "Error", message = "L'instance ROS n'a pas pu être ouverte\nVérifiez votre connexion au wifi du robot et réessayez")
        
    photo_img = None
    def update_image(self):
        global photo_img
        import PIL.Image
        import pyniryo
        if (self.stream_on):
            img_compressed = self.vision_instance.get_img_compressed()
            img_raw=pyniryo.uncompress_image(img_compressed)
            img_colored = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
            pil_image=PIL.Image.fromarray(img_colored)
            img_resized = pil_image.resize((300,300))
            photo_img=ImageTk.PhotoImage(img_resized)
            self.image=img_resized
            self.canvas.create_image(0,0,anchor="nw", image=photo_img)

        else :
            self.canvas.create_image(0,0, anchor="nw", image=self.no_image)

        self.parent.after(self.interval, self.update_image)

    def __stop_stream__(self):
       self.stream_on = False



