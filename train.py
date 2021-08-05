from os import pardir
from tkinter import *
from tkinter import ttk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x690+0+40")      #"width*height+x+y"
        self.root.title("Face Recognition Sytem")


        title_lb1 = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="Red")
        title_lb1.place(x=0,y=0,width=1430,height=45)

        img_top = Image.open("Colleg_image/train2.jpg")    ##r to convert intoo forward slash
        img_top = img_top.resize((1339,300),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1339,height=300)

        #button
        b1_1 = Button(self.root,text="Train Data",command=self.train_clasifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=355,width=1439,height=45)

        img_bottom = Image.open("Colleg_image/train2.jpg")    ##r to convert intoo forward slash
        img_bottom = img_bottom.resize((1339,300),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=400,width=1339,height=300)

    
    def train_clasifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      #Gray scael image
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ##############Train the classifer and save######################
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()