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
from detail import Detail
from showdetail import Showdetail



class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x690+0+40")      #"width*height+x+y"
        self.root.title("Face Recognition Sytem")


        #first image
        img = Image.open("Colleg_image/deepblue.jpg")    ##r to convert intoo forward slash
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open("Colleg_image/deepblue.jpg")    
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)

        #third image
        img2 = Image.open("Colleg_image/deepblue.jpg")    
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=500,height=130)

        #bg_image       behind all img1,mg2,img so y=130
        img3 = Image.open("Colleg_image/deep-blue-background.jpg")    
        img3 = img3.resize((1330,690),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1330,height=690)

        title_lb1 = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1430,height=45)

        ##current time ############
        def time():
            string=strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000, time)
        
        lb1 = Label(title_lb1,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lb1.place(x=0,y=0,width=110,height=50)
        time()


        #student button
        img4 = Image.open("Colleg_image/data.jpg")    
        img4 = img4.resize((200,210),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=200,height=200)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=250,width=200,height=40)

        ###place all other button as above and 1 video end
        #detect button
        img5 = Image.open("Colleg_image/face.jpg")    
        img5 = img5.resize((200,210),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b1 = Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=400,y=50,width=200,height=200)

        b1_1 = Button(bg_img,text="Face detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=200,height=40)

        #Attandance button
        img6 = Image.open("Colleg_image/attendance.png")    
        img6 = img6.resize((200,190),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b1 = Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=700,y=50,width=200,height=200)

        b1_1 = Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=200,height=40)

        #Show Detail
        img7 = Image.open("Colleg_image/images.jpg")    
        img7 = img7.resize((200,130),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b1 = Button(bg_img,image=self.photoimg7,command=self.show_data,cursor="hand2")
        b1.place(x=1000,y=50,width=200,height=200)

        b1_1 = Button(bg_img,text="Show Detail",command=self.show_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=250,width=200,height=40)

        #Train button
        img8 = Image.open("Colleg_image/training.png")    
        img8 = img8.resize((200,210),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b1 = Button(bg_img,image=self.photoimg8,command=self.train_details,cursor="hand2")
        b1.place(x=100,y=310,width=200,height=200)

        b1_1 = Button(bg_img,text="Train data",command=self.train_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=510,width=200,height=40)

        #Photo button
        img9 = Image.open("Colleg_image/photo.png")    
        img9 = img9.resize((200,210),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b1 = Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=400,y=310,width=200,height=200)

        b1_1 = Button(bg_img,text="Photo",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=510,width=200,height=40)

        #Detail button
        img10 = Image.open("Colleg_image/detail.png")    
        img10 = img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b1 = Button(bg_img,image=self.photoimg10,command=self.detail_data,cursor="hand2")
        b1.place(x=700,y=310,width=200,height=200)

        b1_1 = Button(bg_img,text="Details",command=self.detail_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=510,width=200,height=40)

 
        #Exit button
        img11 = Image.open("Colleg_image/exit.jpg")    
        img11 = img11.resize((200,210),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b1 = Button(bg_img,image=self.photoimg11,command=self.exit,cursor="hand2")
        b1.place(x=1000,y=310,width=200,height=200)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1000,y=510,width=200,height=40)

    def open_img(self):
        #os.startfile("data")
        subprocess.Popen(r'explorer "A:\PythonPorject\facerecog\data"')

    ##############function button
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def detail_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Detail(self.new_window)  


    def show_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Showdetail(self.new_window)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this Project",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()