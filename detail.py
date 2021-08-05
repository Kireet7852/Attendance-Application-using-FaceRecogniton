from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
import tkinter
import subprocess
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance



class Detail:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x690+0+40")      #"width*height+x+y"
        self.root.title("Detail")


        img1 = Image.open("Colleg_image/Details photo.jpg")    
        img1 = img1.resize((1330,690),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1330,height=690)



if __name__ == "__main__":
    root = Tk()
    obj = Detail(root)
    root.mainloop()