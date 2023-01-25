import tkinter
import tkinter.filedialog
import cv2
import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
import numpy as np
import random

class ROBOT:
    def __init__(self, window=None):
        self.window = window
