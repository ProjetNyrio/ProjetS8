from tkinter import ttk, END

import pyniryo
from pyniryo2 import NiryoRos, Vision
from video_canvas import *
import imageio
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
import Pmw
from PIL import Image, ImageTk

import PIL.Image
import PIL.ImageTk
import PIL.ImageFilter
from PIL import Image, ImageTk

# Créer une fenêtre principale
root = tk.Tk()
root.title("Interface de traitement d'image et de contrôle de robot")
root.geometry("1280x723")
root.style1 = False
root.page1 = None
root.page2 = None
Pmw.initialise(root)
# Définir le thème
root.tk.call('source', './Azure-ttk-theme/azure.tcl')
root.tk.call('set_theme', 'dark')
        
root.configure(bg="#008080")  # Définir la couleur de fond

root.option_add('*TkFDialog*foreground','black')
# Créer un label avec le message de bienvenue
welcome_label = tk.Label(root, text="Traitement d'image et Contrôle de robot bras", font=("Arial", 24), fg="#FFFFFF", bg="#008080")
welcome_label.pack(pady=20)

# Créer un bouton "Exit"
exit_button = tk.Button(root, text="Exit", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=root.destroy)
exit_button.pack(pady=10)



# Définir une fonction pour afficher la deuxième fenêtre
def afficher_deuxieme_fenetre():
    # Créer une nouvelle fenêtre
    if (root.page1 == None):
        root.page1 = tk.Toplevel(root)
        root.page1.title("Panneau de contrôle")
        root.page1.geometry("1130x600")
        style = ttk.Style(root.page1)
        #root.page1.tk.call('source', './Azure-ttk-theme/azure.tcl')
        #root.page1.tk.call('set_theme', 'light')
    else : 
        root.page1.deiconify()

    root.withdraw()
    # Ajouter des éléments à la deuxième fenêtre
    # tk.Label(fenetre2, text="Bienvenue dans la deuxième fenêtre!").pack()
    # tk.Button(fenetre2, text="Fermer", command=fenetre2.destroy).pack()

    global robot
    robot = None
    root.page1.video_canvas1 = None

    def retour1():
        root.deiconify()
        root.page1.withdraw()
        if hasattr(root.page1.video_canvas1, "ros_instance"):
            root.page1.video_canvas1.ros_instance.close()
         
    def close_connection():
        robot.close_connection()

    def home_pose():
        robot.move_to_home_pose()

    def learning_mode():
        robot.set_learning_mode(True)

    def connect_to_robot():
        global robot
        try :
            robot = NiryoRobot("10.10.10.10")
            robot.calibrate_auto()
        except : 
            showerror(title = "Error", message = "Connection échouée\nVérifiez que vous êtes bien connectés au wifi du robot et réessayer")

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
        if (root.page1.video_canvas1 != None):
            root.page1.video_canvas1.stream_on = True
        else:
            root.page1.video_canvas1 = video_canvas(video_frame)

    def capture_img():
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("All files", "*.*")])
        if not filename:
            return
        root.page1.video_canvas1.image.save(filename)

    def end_stream():
        if hasattr(root.page1.video_canvas1, "ros_instance"):
            root.page1.video_canvas1.ros_instance.close()
        root.page1.video_canvas1.__stop_stream__()
        

    def window_closing():
        if messagebox.askokcancel("Quit", "Voulez vous quitter?"):
            if (root.page1.video_canvas1 != None):
                root.page1.video_canvas1.ros_instance.close()
            root.page1.destroy()
            root.destroy()

    Title1 = ttk.Label(root.page1, text="Connection et calibrage")
    Title1.grid(row=0, column=0, columnspan=3, sticky=tk.W)
    Title1.configure(font=("Helvetica", 18, "bold"))

    blank = ttk.Label(root.page1, text="   \n")
    blank.grid(row=1, column=0)

    frame1 = ttk.Frame(root.page1)

    close_connection_button = ttk.Button(frame1, text="  Déconnection  ", command=close_connection)
    close_connection_button.grid(row=0, column=2, ipadx=20, ipady=15)

    homepose_button = ttk.Button(frame1, text="    Homepose    ", command=home_pose)
    homepose_button.grid(row=0, column=1, ipadx=30, ipady=15)
    tooltip_hp = Pmw.Balloon(root) #Calling the tooltip
    tooltip_hp.bind(homepose_button,"Ramène le bras et l'outil du robot dans leurs positions initiales")

    connect_button = ttk.Button(frame1, text="Connection robot", style="Accent.TButton", command=connect_to_robot)
    connect_button.grid(row=0, column=0, ipadx=20, ipady=15)
    tooltip_connect = Pmw.Balloon(root) #Calling the tooltip
    tooltip_connect.bind(connect_button,"Connectez vous au wifi du robot\nCe bouton vous permet d'établir une connexion directe avec un Niryo Ned via la librairie PyNiryo")

    learning_mode_button = ttk.Button(frame1, text=" Learning mode ", command=learning_mode)
    learning_mode_button.grid(row=0, column=3, ipadx=22, ipady=15)
    tooltip_lm = Pmw.Balloon(root) #Calling the tooltip
    tooltip_lm.bind(learning_mode_button,'Passe le robot en mode apprentissage ce qui arrête son mouvement actuel')
    
    frame1.grid(row=2, column=0, columnspan=8, sticky=tk.W)

    blank2 = ttk.Label(root.page1, text="   \n")
    blank2.grid(row=3, column=0)

    Title2 = ttk.Label(root.page1, text="Contrôle du bras")
    Title2.grid(row=4, column=0, columnspan=2, sticky=tk.W)
    Title2.configure(font=("Helvetica", 18, "bold"))

    blank3 = ttk.Label(root.page1, text="   \n")
    blank3.grid(row=5, column=0)

    # create a stringvar for each joint of the robot's arm

    j1 = tk.StringVar()
    j2 = tk.StringVar()
    j3 = tk.StringVar()
    j4 = tk.StringVar()
    j5 = tk.StringVar()
    j6 = tk.StringVar()

    ttk.Label(root.page1, text="Bras Axe 1").grid(row=6, column=0)
    ttk.Label(root.page1, text="Bras Axe 2").grid(row=6, column=1)
    ttk.Label(root.page1, text="Bras Axe 3").grid(row=6, column=2)
    ttk.Label(root.page1, text="Outil Axe 1").grid(row=8, column=0)
    ttk.Label(root.page1, text="Outil Axe 2").grid(row=8, column=1)
    ttk.Label(root.page1, text="Outil Axe 3").grid(row=8, column=2)

    ttk.Entry(root.page1, textvariable=j1).grid(row=7, column=0, sticky=tk.W)
    ttk.Entry(root.page1, textvariable=j2).grid(row=7, column=1, sticky=tk.W)
    ttk.Entry(root.page1, textvariable=j3).grid(row=7, column=2, sticky=tk.W)
    ttk.Entry(root.page1, textvariable=j4).grid(row=9, column=0, sticky=tk.W)
    ttk.Entry(root.page1, textvariable=j5).grid(row=9, column=1, sticky=tk.W)
    ttk.Entry(root.page1, textvariable=j6).grid(row=9, column=2, sticky=tk.W)

    def generate_command():
        try:
            command = [float(j1.get()), float(j2.get()), float(j3.get()), float(j4.get()), float(j5.get()),
                       float(j6.get())]
        except:
            messagebox.showerror('Error',
                                 'Commande')
            return
        try:
            robot.move_joints(command)
        except:
            if (robot == None):
                messagebox.showerror('Error', "Vous n'êtes pas connecté à un robot")
            else :
                messagebox.showerror('Error', 'Commande en dehors de la plage de valeurs acceptées')
    
    send_command_button = ttk.Button(root.page1, text="Envoi commande", command=generate_command)
    send_command_button.grid(row=6, rowspan=4, column=3, ipadx=18, ipady=12, sticky="sw")
    tooltip_1 = Pmw.Balloon(root) #Calling the tooltip
    tooltip_1.bind(send_command_button,"Assurez-vous d'être connecté à un robot pour envoyer une commande\nRenseignez des valeurs comprises dans [-1;1]\nRenseignez 0 si vous souhaitez garder un axe immobile")

    blank4 = ttk.Label(root.page1, text="   \n")
    blank4.grid(row=10, column=0)

    tools_frame = ttk.Frame(root.page1)
    Title3 = ttk.Label(tools_frame, text="Utilisation d'outils")
    Title3.grid(row=0, column=0, columnspan=3, sticky=tk.W)
    Title3.configure(font=("Helvetica", 18, "bold"))

    blank5 = ttk.Label(tools_frame, text="   \n")
    blank5.grid(row=1, column=0)

    grasp_button = ttk.Button(tools_frame, text=" Attraper ", command=grasp_gripper)
    grasp_button.grid(row=2, column=1, rowspan=2, ipadx=26, ipady=15, sticky="nsew")

    release_button = ttk.Button(tools_frame, text=" Relacher ", command=release_gripper)
    release_button.grid(row=2, column=2, rowspan=2, ipadx=24, ipady=15, sticky="nsew")

    update_tools_button = ttk.Button(tools_frame, text="Detection outils", command=update_tools)
    update_tools_button.grid(row=2, column=0, rowspan=2, ipadx=28, ipady=15, sticky="nsew")
    tooltip_up = Pmw.Balloon(root) #Calling the tooltip
    tooltip_up.bind(update_tools_button,"Ce bouton permet de réactualiser la détection des outils par le robot\nA utiliser en début de séance et à chaque changement d'outil")

    tools_frame.grid(row=11, column=0, columnspan=4, rowspan=5, sticky=tk.W)

    blank6 = ttk.Label(root.page1, text="\t")
    blank6.grid(row=0, column=6)

    Title4 = ttk.Label(root.page1, text="Caméra")
    Title4.grid(row=0, column=7, columnspan=3, sticky=tk.W)
    Title4.configure(font=("Helvetica", 18, "bold"))

    blank7 = ttk.Label(root.page1, text="   \n")
    blank7.grid(row=1, column=0)

    open_camera = ttk.Button(root.page1, text="Ouvrir stream caméra", command=get_img)
    open_camera.grid(row=2, column=7, ipadx=10, ipady=10, sticky=tk.W)
    tooltip_oc = Pmw.Balloon(root) #Calling the tooltip
    tooltip_oc.bind(open_camera,"Ouvre une instance ROS pour acceder à la caméra du robot connecté")

    video_frame_style = ttk.Style()
    video_frame_style.configure("video.TFrame", background="#4A4A4A")
    video_frame = ttk.Frame(root.page1, style="video.TFrame", height=300, width=300)

    end_stream_button = ttk.Button(root.page1, text="  Quitter le stream  ", command=end_stream)
    end_stream_button.grid(row=11, column=7, ipadx=10, ipady=10, sticky=tk.W)

    capture_image_button = ttk.Button(root.page1, text="Enregistrer l'image", command=capture_img)
    capture_image_button.grid(row=11, column=8, ipadx=10, ipady=10, sticky=tk.W)
    tooltip_ci = Pmw.Balloon(root) #Calling the tooltip
    tooltip_ci.bind(capture_image_button,"Enregistre l'image actuelle du stream video")

    video_frame.grid(row=3, column=7, rowspan=8, columnspan=2, sticky=tk.W)

    button_exit = ttk.Button(root.page1, text="Retour", command=retour1)
    button_exit.grid(row=12, column=8, sticky="se")
    tooltip_ex = Pmw.Balloon(root) #Calling the tooltip
    tooltip_ex.bind(button_exit,"Retour à la page d'accueil")
    root.page1.protocol("WM_DELETE_WINDOW", window_closing)
    root.page1.mainloop()

file_path = ''
def afficher_troisieme_fenetre():
    if (root.page2 == None):
        root.page2 = tk.Toplevel(root)
        root.page2.title("Python IDLE")
        root.page2.geometry("1280x720+150+80")
        root.page2.configure(bg="#323846")
        root.page2.resizable(False, False)
    # global before_image
    # after_img = Image.new('RGB', (150, 150), (255, 255, 255))

   # file_path = ''
    else :
        root.page2.deiconify()

    root.withdraw()

    def retour2():
        root.deiconify()
        root.page2.withdraw()
        file_path=''
        if hasattr(root.page2, "file"):
            root.page2.file.close()
            root.page2.file = None
        

    def set_file_path(path):
        global file_path
        file_path = path

    def open_file():
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        with open(path, 'r') as root.page2.file:
            code = root.page2.file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            set_file_path(path)

    def save():
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
        else:
            path = file_path
        with open(path, 'w') as root.page2.file:
            code = code_input.get('1.0', END)
            root.page2.file.write(code)
            set_file_path(path)

    def run():
        if file_path == '':
            messagebox.showerror("Python IDLE", "Save your Code")
            return 0
        # code = code_input.get("1.0", "end-1c")
        command = f'python3 {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if (os.path.exists("./after.png")):
            beaa = Image.open("./after.png")
            resized = beaa.resize((400,350))
            after_image = ImageTk.PhotoImage(resized)
            after_label.config(image=after_image)
            after_label.image = after_image 
        code_output.insert('1.0', output)
        code_output.insert('1.0', error)

    def save_image(after_image=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG", ".png"), ("All Files", ".*")])
        Image.open("/home/mateo/Documents/ProjetS8/robot_control_panel/after.png").save(file_path)
        # Mettre à jour les images dans les labels

    def select_image():
        file_path = tkinter.filedialog.askopenfilename()
        before_img = Image.open(file_path)
        resized = before_img.resize((400,300))
        before_image = ImageTk.PhotoImage(resized)
        before_label = tk.Label(root.page2, image=before_image)
        before_label.grid(row=0, column=0)
        before_label.configure(image=before_image)
        before_label.image = before_image
        before_label.grid(row=0, column=0)
        before_label.place(x=850, y=400, width=400, height=300)

    def Capture():
        try :
            ros_instance = NiryoRos("10.10.10.10")  # Hotspot
            vision_instance = Vision(ros_instance)
            img_c = vision_instance.get_img_compressed()
            img_raw = pyniryo.uncompress_image(img_c)
            imageio.imwrite('/home/mateo/Documents/ProjetS8/robot_control_panel/aftr.png', img_raw)
            im_cv = cv2.imread('/home/mateo/Documents/ProjetS8/robot_control_panel/aftr.png')
            image_rgb = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
            cv2.imwrite('/home/mateo/Documents/ProjetS8/robot_control_panel/afeetr.png', image_rgb)
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG", ".png"), ("All Files", ".*")])
            Image.open("/home/mateo/Documents/ProjetS8/robot_control_panel/afeetr.png").save(file_path)
            ros_instance.close()
        except :
            showerror(title = "Error", message = "L'instance ROS n'a pas pu être ouverte\nVérifiez votre connexion au wifi du robot et réessayez")


    def window_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.page2.destroy()
            root.destroy()


    before_label = tk.Label(root.page2)
    before_label.grid(row=0, column=0)
    before_label.place(x=850, y=0, width=400, height=350)
    # 850 0
    # Créer le label pour l'image après le traitement
    after_label = tk.Label(root.page2)
    after_label.grid(row=1, column=0)
    after_label.place(x=850, y=10, width=400, height=350)

    code_input = Text(root.page2, font="cosolas 18")
    code_input.place(x=150, y=0, width=680, height=400)

    code_output = Text(root.page2,font="consolas 15", bg="#323846", fg="lightgreen")
    code_output.place(x=150, y=400, width=680, height=300)

    Open = PhotoImage(file="./images_natives/open.png")
    Save = PhotoImage(file="./images_natives/save.png")
    Run = PhotoImage(file="./images_natives/run.png")
    saveimage = PhotoImage(file="./images_natives/m_download.png")
    selectimage = PhotoImage(file="./images_natives/m_main.png")
    capture = PhotoImage(file="./images_natives/ImageC.png")

    open_code_button = Button(root.page2, image=Open, bg="#323846", bd=0, highlightthickness=0, command=open_file)
    open_code_button.place(x=30, y=30)

    save_code_button = Button(root.page2, image=Save, bg="#323846", bd=0, highlightthickness=0, command=save)
    save_code_button.place(x=30, y=145)
    

    Button(root.page2, image=Run, bg="#323846", bd=0, highlightthickness=0, command=run).place(x=30, y=260)
    
    
    save_image_button = Button(root.page2, image=saveimage, bg="#323846", bd=0, highlightthickness=0, command=save_image)
    save_image_button.place(x=30, y=380)
    

    select_image_button = Button(root.page2, image=selectimage, bg="#323846", bd=0, highlightthickness=0, command=select_image)
    select_image_button.place(x=30, y=500)
    

    capture_button = Button(root.page2, image=capture, bg="#323846", bd=0, highlightthickness=0, command=Capture)
    capture_button.place(x=45, y=630)

    
    tooltip_oc = Pmw.Balloon(root) 
    tooltip_oc.bind(open_code_button,'Ouvrir un fichier de code python')

    tooltip_sc = Pmw.Balloon(root) 
    tooltip_sc.bind(save_code_button,'Sauvegarder le code')

    tooltip_si = Pmw.Balloon(root) 
    tooltip_si.bind(save_image_button,"Enregistrer l'image du résultat")
    
    tooltip_cap = Pmw.Balloon(root)
    tooltip_cap.bind(capture_button,'Capturer une image depuis la caméra du robot')

    tooltip_sel = Pmw.Balloon(root)
    tooltip_sel.bind(select_image_button,'Ouvrir un fichier image à traiter')



    button2 = ttk.Button(root.page2, text="Retour", command=retour2)
    button2.grid(row=2, column=1, padx=50, pady=5)
    
    root.page2.protocol("WM_DELETE_WINDOW", window_closing)
    root.page2.mainloop()

# Ajouter un bouton à la première fenêtre pour afficher la deuxième fenêtre

bouton2 = tk.Button(root, text="Contrôle du bras", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=afficher_deuxieme_fenetre)
bouton2.pack(pady=10)

bouton3 = tk.Button(root, text="Python IDLE", font=("Arial", 16), fg="#FFFFFF", bg="#003366", command=afficher_troisieme_fenetre)
bouton3.pack(pady=10)
"""
bouton2 = ttk.Button(root, text="Contrôle du bras", command=afficher_deuxieme_fenetre)
bouton2.pack(pady=10)

bouton3 = ttk.Button(root, text="Python IDLE", command=afficher_troisieme_fenetre)
bouton3.pack(pady=10)
"""
# Lancer la boucle principale
root.mainloop()
