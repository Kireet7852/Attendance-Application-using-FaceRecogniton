from os import pardir
from tkinter import *
from tkinter import ttk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from shutil import copy2
from tkinter import filedialog


class Moredetail:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+40")      #"width*height+x+y"
        self.root.title("More detail")

        #################variable###################
        self.var_std_id = StringVar()
        self.var_std_type = StringVar()
        
        #first image
        img = Image.open(r"C:\python\facerecog\Colleg_image\student.jpg")    ##r to convert intoo forward slash
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open(r"C:\python\facerecog\Colleg_image\attend.jpg")    
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)

        #third image
        img2 = Image.open(r"C:\python\facerecog\Colleg_image\student.jpg")    
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=500,height=130)  



        #bg_image       behind all img1,mg2,img so y=130
        img3 = Image.open(r"C:\python\facerecog\Colleg_image\red.jpg")    
        img3 = img3.resize((1430,690),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,bg="green")
        bg_img.place(x=0,y=130,width=1430,height=690)

        title_lb1 = Label(bg_img,text="MORE DETAILS",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1430,height=45)  

        main_frame = Frame(bg_img,bd=2,bg="RED")     #br=border
        main_frame.place(x=5,y=55,width=1410,height=515)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="More Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=1340,height=480)

        
        #studentid
        studentId_label = Label(left_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #Aadharid
        Aadharid_label = Label(left_frame,text="Aadhar No:",font=("times new roman",13,"bold"),bg="white")
        Aadharid_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Aadharid_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        Aadharid_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Caste
        Caste_label = Label(left_frame,text="Caste:",font=("times new roman",13,"bold"),bg="white")
        Caste_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Caste_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        Caste_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #SSC 
        SSCmarks_label = Label(left_frame,text="10th Marks:",font=("times new roman",13,"bold"),bg="white")
        SSCmarks_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        SSCmarks_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        SSCmarks_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #HSC 
        HSCmarks_label = Label(left_frame,text="12th Marks:",font=("times new roman",13,"bold"),bg="white")
        HSCmarks_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        HSCmarks_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        HSCmarks_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #CET marks
        CETmarks_label = Label(left_frame,text="CET Percentile:",font=("times new roman",13,"bold"),bg="white")
        CETmarks_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        CETmarks_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        CETmarks_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

          #Activites
        Activites_label = Label(left_frame,text="Activites:",font=("times new roman",13,"bold"),bg="white")
        Activites_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Activites_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        Activites_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         

        #buttons frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=420,width=655,height=35)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=1)

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Field are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student1 value(%s,%s)",(
                    self.var_std_id.get(),
                    self.var_std_type.get()
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successsfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    
    def reset_data(self):
        pass
    


if __name__ == "__main__":
    root = Tk()
    obj = Moredetail(root)
    root.mainloop()