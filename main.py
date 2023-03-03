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

root=tk.Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")
root.resizable(False,False)
#global before_image
#after_img = Image.new('RGB', (150, 150), (255, 255, 255))

file_path=''
def set_file_path(path):
    global file_path
    file_path=path
def open_file():
       path=askopenfilename(filetypes=[('Python Files','*.py')])
       with open(path,'r') as file:
           code=file.read()
           code_input.delete('1.0',END)
           code_input.insert('1.0',code)
           set_file_path(path)
def save():
    if file_path=='':
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_path
    with open(path,'w') as file:
        code=code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)
def run():
    if file_path=='':
        messagebox.showerror("Python IDLE","Save your Code")
        return 0
    #code = code_input.get("1.0", "end-1c")
    command = f'python {file_path}'
    #after_img=eval(code)
    #after_image = ImageTk.PhotoImage(after_img)
    #after_label.config(image=after_image)
    #after_label.image = after_image
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   # process=subprocess.run(command)
    output, error = process.communicate()
    #code_output.insert('1.0', output)
    #bytes_io = io.BytesIO(output)
    #image = Image.open(io.BytesIO(output))
    beaa=Image.open("C:/Users/halaoui/Downloads/after.png")
    after_image = ImageTk.PhotoImage(beaa)
    code_output.insert('1.0', error)
    after_label.config(image=after_image)
    after_label.image = after_image

def save_image(after_image=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG", "*.png"), ("All Files", "*.*")])
    Image.open("C:/Users/halaoui/Downloads/after.png").save(file_path)
    #Mettre à jour les images dans les labels
def select_image():
    file_path = tkinter.filedialog.askopenfilename()
    before_img = Image.open(file_path)
    before_image = ImageTk.PhotoImage(before_img)
    before_label = tk.Label(root, image=before_image)
    before_label.grid(row=0, column=0)
    before_label.configure(image=before_image)
    before_label.image = before_image
    before_label.grid(row=0, column=0)
    before_label.place(x=850, y=400, width=400, height=300)



#before_image = Image.open("len.png")
#before_image = ImageTk.PhotoImage(before_image)
before_label = tk.Label(root)
before_label.grid(row=0, column=0)
before_label.place(x=850,y=400, width=400, height=300)

# Créer le label pour l'image après le traitement
#after_img = Image.new('RGB', (100, 100), (255, 255, 255))
#after_image = ImageTk.PhotoImage(after_img)
after_label = tk.Label(root)
after_label.grid(row=1, column=0)
after_label.place(x=400,y=400, width=400, height=300)

code_input= Text(root,font="cosolas 18")
code_input.place(x=150,y=0, width=680, height=400)

code_output=Text(root,font="consolas 15",bg="#323846",fg="lightgreen")
code_output.place(x=850,y=0,width=500,height=300)

Open=PhotoImage(file="open.png")
Save=PhotoImage(file="save.png")
Run=PhotoImage(file="run.png")
saveimage=PhotoImage(file="m_download.png")
selectimage=PhotoImage(file="m_main.png")



Button(root,image=Open,bg="#323846",bd=0,command=open_file).place(x=30,y=30)
Button(root,image=Save,bg="#323846",bd=0,command=save).place(x=30,y=145)
Button(root,image=Run,bg="#323846",bd=0,command=run).place(x=30,y=260)
Button(root,image=saveimage,bg="#323846",bd=0,command=save_image).place(x=30,y=380)
Button(root,image=selectimage,bg="#323846",bd=0,command=select_image).place(x=30,y=500)

root.mainloop()