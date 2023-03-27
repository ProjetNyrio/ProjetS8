from tkinter import ttk, END
from video_canvas import *
from pyniryo import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import tkinter
import tkinter.filedialog
import code
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import os
import io
import tkinter
import tkinter.filedialog
import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
import numpy as np
import random
from PIL import Image, ImageTk

import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
from PIL import Image, ImageTk

# Créer une fenêtre principale
root = tk.Tk()
root.title("Welcome to my app!")
root.geometry("1280x723")
root.style1=False 

# Définir le thème
root.configure(bg="#008080")  # Définir la couleur de fond

# Créer un label avec le message de bienvenue
welcome_label = tk.Label(root, text="Welcome to my App!", font=("Arial", 24), fg="#FFFFFF", bg="#008080")
welcome_label.pack(pady=20)

# Créer un bouton "Exit"
exit_button = tk.Button(root, text="Exit", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=root.destroy)
exit_button.pack(pady=10)

#THEMES DARK SUR TOUTE LINTERFACE
#style = ttk.Style(root)
#root.tk.call('source', '../ttkthemes/Azure-ttk-theme/azure.tcl')
#root.tk.call('set_theme', 'dark')
    
# Définir une fonction pour afficher la deuxième fenêtre
def afficher_deuxieme_fenetre():
    # Créer une nouvelle fenêtre
    root1 = tk.Toplevel(root)
    root1.title("Panneau de contrôle")
    root1.geometry("1120x600")
    root.withdraw()

    # Ajouter des éléments à la deuxième fenêtre
    #tk.Label(fenetre2, text="Bienvenue dans la deuxième fenêtre!").pack()
    #tk.Button(fenetre2, text="Fermer", command=fenetre2.destroy).pack()
   
    global robot
    robot=None
    root1.video_canvas1=None

    def retour1():
        root.deiconify()
        root1.withdraw()


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
        if (root1.video_canvas1 != None):
            root1.video_canvas1.stream_on = True
        else :
            root1.video_canvas1 = video_canvas(video_frame)

    def capture_img():
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("All files", "*.*")])
        if not filename:
            return
        root1.video_canvas1.image.save(filename)

    def end_stream():
        root1.video_canvas1.__stop_stream__()

    def window_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            if (root1.video_canvas1 != None):
                root1.video_canvas1.ros_instance.close()
            root1.destroy()
            root.destroy()

    Title1= ttk.Label(root1, text="Connection et calibrage")
    Title1.grid(row=0, column=0, columnspan=3, sticky=tk.W)
    Title1.configure(font=("Helvetica", 18, "bold"))

    blank=ttk.Label(root1, text="   \n")
    blank.grid(row=1, column=0)

    frame1 = ttk.Frame(root1)

    close_connection_button = ttk.Button(frame1, text="Close connection", command=close_connection)
    close_connection_button.grid(row=0, column=2, ipadx=20, ipady=15)

    homepose_button = ttk.Button(frame1, text="  Homepose  ", command=home_pose)
    homepose_button.grid(row=0, column=1, ipadx=30, ipady=15)

    connect_button = ttk.Button(frame1, text="Connect to robot",style="Accent.TButton", command=connect_to_robot)
    connect_button.grid(row=0, column=0, ipadx=20, ipady=15)


    learning_mode_button = ttk.Button(frame1, text=" Learning mode ", command=learning_mode)
    learning_mode_button.grid(row=0, column=3, ipadx=22, ipady=15)

    frame1.grid(row=2, column=0, columnspan=8, sticky=tk.W)

    blank2=ttk.Label(root1, text="   \n")
    blank2.grid(row=3, column=0)


    Title2= ttk.Label(root1, text="Contrôle du bras")
    Title2.grid(row=4, column=0, columnspan=2, sticky=tk.W)
    Title2.configure(font=("Helvetica", 18, "bold"))

    blank3=ttk.Label(root1, text="   \n")
    blank3.grid(row=5, column=0)

#create a stringvar for each joint of the robot's arm

    j1=tk.StringVar()
    j2=tk.StringVar()
    j3=tk.StringVar()
    j4=tk.StringVar()
    j5=tk.StringVar()
    j6=tk.StringVar()

    ttk.Label(root1, text="j1").grid(row=6, column=0)
    ttk.Label(root1, text="j2").grid(row=6, column=1)
    ttk.Label(root1, text="j3").grid(row=6, column=2)
    ttk.Label(root1, text="j4").grid(row=8, column=0)
    ttk.Label(root1, text="j5").grid(row=8, column=1)
    ttk.Label(root1, text="j6").grid(row=8, column=2)

    ttk.Entry(root1, textvariable=j1).grid(row=7, column=0, sticky=tk.W)
    ttk.Entry(root1, textvariable=j2).grid(row=7, column=1, sticky=tk.W)
    ttk.Entry(root1, textvariable=j3).grid(row=7, column=2, sticky=tk.W)
    ttk.Entry(root1, textvariable=j4).grid(row=9, column=0, sticky=tk.W)
    ttk.Entry(root1, textvariable=j5).grid(row=9, column=1, sticky=tk.W)
    ttk.Entry(root1, textvariable=j6).grid(row=9, column=2, sticky=tk.W)

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

    send_command_button = ttk.Button(root1, text="Send command", command=generate_command)
    send_command_button.grid(row=6, rowspan=4,  column=3, ipadx=18, ipady=12, sticky="sw")

    blank4=ttk.Label(root1, text="   \n")
    blank4.grid(row=10, column=0)

    tools_frame=ttk.Frame(root1)
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


    blank6=ttk.Label(root1, text="\t")
    blank6.grid(row=0, column=6)

    Title4= ttk.Label(root1, text="Caméra")
    Title4.grid(row=0, column=7, columnspan=3, sticky=tk.W)
    Title4.configure(font=("Helvetica", 18, "bold"))


    blank7=ttk.Label(root1, text="   \n")
    blank7.grid(row=1, column=0)


    open_camera = ttk.Button(root1, text="Open camera stream", command=get_img)
    open_camera.grid(row=2, column=7, ipadx=10, ipady=10, sticky=tk.W)

    video_frame_style=ttk.Style()
    video_frame_style.configure("video.TFrame", background="#4A4A4A")
    video_frame = ttk.Frame(root1, style="video.TFrame", height=300, width=300)

    end_stream_button = ttk.Button(root1, text="End camera stream", command=end_stream)
    end_stream_button.grid(row=11, column=7, ipadx=10, ipady=10, sticky=tk.W)

    capture_image_button = ttk.Button(root1, text="Enregistrer l'image", command=capture_img)
    capture_image_button.grid(row=11, column=8, ipadx=10, ipady=10, sticky=tk.W) 
    video_frame.grid(row=3, column=7, rowspan=8, columnspan=2, sticky=tk.W)

    button_exit = ttk.Button(root1, text="StartPage", command=retour1)
    button_exit.grid(row=12, column=8, sticky="se")
    
    root1.protocol("WM_DELETE_WINDOW", window_closing)
    root1.mainloop()


def afficher_troisieme_fenetre():
    # Créer une nouvelle fenêtre
    root2 = tk.Toplevel(root)
    root.withdraw()
    root2.title("Python IDLE")
    root2.geometry("1280x720+150+80")
    root2.configure(bg="#323846")
    root2.resizable(False, False)
    # global before_image
    # after_img = Image.new('RGB', (150, 150), (255, 255, 255))

    file_path = ''

    def retour2():
        root.deiconify()
        root2.withdraw()

    def set_file_path(path):
        global file_path
        file_path = path

    def open_file():
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as file:
            code = file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            set_file_path(path)

    def save():
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as file:
            code = code_input.get('1.0', END)
            file.write(code)
            set_file_path(path)

    def run():
        if file_path == '':
            messagebox.showerror("Python IDLE", "Save your Code")
            return 0
        # code = code_input.get("1.0", "end-1c")
        command = f'python {file_path}'
        # after_img=eval(code)
        # after_image = ImageTk.PhotoImage(after_img)
        # after_label.config(image=after_image)
        # after_label.image = after_image
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # process=subprocess.run(command)
        output, error = process.communicate()
        # code_output.insert('1.0', output)
        # bytes_io = io.BytesIO(output)
        # image = Image.open(io.BytesIO(output))
        beaa = Image.open("C:/Users/halaoui/Downloads/after.png")
        after_image = ImageTk.PhotoImage(beaa)
        code_output.insert('1.0', error)
        after_label.config(image=after_image)
        after_label.image = after_image

    def save_image(after_image=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG", "*.png"), ("All Files", "*.*")])
        Image.open("C:/Users/halaoui/Downloads/after.png").save(file_path)
        # Mettre à jour les images dans les labels

    def select_image():
        file_path = tkinter.filedialog.askopenfilename()
        before_img = Image.open(file_path)
        before_image = ImageTk.PhotoImage(before_img)
        before_label = tk.Label(root2, image=before_image)
        before_label.grid(row=0, column=0)
        before_label.configure(image=before_image)
        before_label.image = before_image
        before_label.grid(row=0, column=0)
        before_label.place(x=850, y=400, width=400, height=300)

    # before_image = Image.open("len.png")
    # before_image = ImageTk.PhotoImage(before_image)
    before_label = tk.Label(root2)
    before_label.grid(row=0, column=0)
    before_label.place(x=850, y=400, width=400, height=300)

    # Créer le label pour l'image après le traitement
    # after_img = Image.new('RGB', (100, 100), (255, 255, 255))
    # after_image = ImageTk.PhotoImage(after_img)
    after_label = tk.Label(root2)
    after_label.grid(row=1, column=0)
    after_label.place(x=400, y=400, width=400, height=300)

    code_input = Text(root2, font="cosolas 18")
    code_input.place(x=150, y=0, width=680, height=400)

    code_output = Text(root2, font="consolas 15", bg="#323846", fg="lightgreen")
    code_output.place(x=850, y=0, width=500, height=300)

    Open = PhotoImage(file="open.png")
    Save = PhotoImage(file="save.png")
    Run = PhotoImage(file="run.png")
    saveimage = PhotoImage(file="m_download.png")
    selectimage = PhotoImage(file="m_main.png")

    Button(root2, image=Open, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
    Button(root2, image=Save, bg="#323846", bd=0, command=save).place(x=30, y=145)
    Button(root2, image=Run, bg="#323846", bd=0, command=run).place(x=30, y=260)
    Button(root2, image=saveimage, bg="#323846", bd=0, command=save_image).place(x=30, y=380)
    Button(root2, image=selectimage, bg="#323846", bd=0, command=select_image).place(x=30, y=500)

    button2 = ttk.Button(root2, text="StartPage", command=retour2)
    button2.grid(row=2, column=1, padx=70, pady=700)

    root.mainloop()

# Ajouter un bouton à la première fenêtre pour afficher la deuxième fenêtre
bouton = tk.Button(root, text="Contrôle du bras", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=afficher_deuxieme_fenetre)
bouton.pack(pady=10)

bouton1 = tk.Button(root, text="Python IDLE", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=afficher_troisieme_fenetre)
bouton1.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
