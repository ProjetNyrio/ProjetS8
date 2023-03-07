import tkinter as tk
from pyniryo2 import *
from PIL import ImageTk, Image
import threading
import time

class video_label(tk.Label):

    def __init__(self, parent):
        self.parent = parent
        self.stream_on = False
        img = Image.open("./images/no_image.jpg")
        resized = img.resize((300,300))
        self.image=ImageTk.PhotoImage(resized)
        self.label = tk.Label(parent, image = self.image)
        self.label.configure(bg="#4A4A4A")
        super().__init__(parent)

    def __start_stream__(self):
        #self.ros_instance = NiryoRos("10.10.10.10") # Hotspot
        #self.vision_instance = Vision(ros_instance)
        self.stream_on = True

        def thread_function():
            import pyniryo
            while (self.stream_on == True):
                img_compressed = vision_instance.get_img_compressed()
                img_raw=pyniryo.uncompress_image(img_c)
                #CONVERT TO PIL IMG
                time.sleep(0.03)

        def test_thread_function():
            img1=Image.open("./images/no_image.jpg")
            img2=Image.open("./images/imageniryodoc.jpg")
            image2 = img2.resize((300, 300))
            image1 = img1.resize((300, 300))
            im1=ImageTk.PhotoImage(image1)
            im2=ImageTk.PhotoImage(image2)
            while (self.stream_on == True):
                self.image=img1
                self.label.configure(image=im1)
                time.sleep(0.3)
                self.image=img2
                self.label.configure(image=im2)
                time.sleep(0.3)

        self.stream_thread = threading.Thread(target=test_thread_function)
        self.stream_thread.start()

    def __stop_stream__(self):
        self.stream_on=False
        #ros_instance.close()



