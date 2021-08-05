from os import pardir, truncate
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
from student import Student



class Showdetail:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+40")      #"width*height+x+y"
        self.root.title("Student Information")

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob= StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_fees = StringVar()
        self.var_radio1=StringVar()


        #first image
        img = Image.open(r"A:\PythonPorject\facerecog\Colleg_image\student.jpg")    ##r to convert intoo forward slash
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open(r"A:\PythonPorject\facerecog\Colleg_image\attend.jpg")    
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)

        #third image
        img2 = Image.open(r"A:\PythonPorject\facerecog\Colleg_image\student.jpg")    
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=500,height=130)  


        #bg_image       behind all img1,mg2,img so y=130
        img3 = Image.open(r"A:\PythonPorject\facerecog\Colleg_image\red.jpg")    
        img3 = img3.resize((1430,690),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1430,height=690)

        title_lb1 = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1430,height=45)  

        main_frame = Frame(bg_img,bd=2,bg="RED")     #br=border
        main_frame.place(x=5,y=55,width=1410,height=515)

        #left label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=0,y=0,width=1340,height=490)

        ##search frame
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=2,y=5,width=1320,height=70)

        search_label = Label(search_frame,text="Search by:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        # self.search_branch_var = StringVar()
        # search_combo = ttk.Combobox(search_frame,textvariable=self.search_branch_var,font=("times new roman",12,"bold"),state="readonly",width=15)     #3readonly
        # search_combo["values"] = ("Select Department","Computer","IT","Mechnical","Civil")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=10,sticky=W)

        self.search_var = StringVar()
        search_combo = ttk.Combobox(search_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),state="readonly",width=15)     #3readonly
        search_combo["values"] = ("Select Option","roll","name","adhaar")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,sticky=W)

        self.searchTxt_var = StringVar()
        search_entry=ttk.Entry(search_frame,width=20,textvariable=self.searchTxt_var,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=9,command=self.search_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn = Button(search_frame,text="Show All",width=9,command=self.fetch_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        


        ###table frame
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=2,y=80,width=1320,height=380)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table= ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","fees","adhaar","caste","ssc","hsc","cet","activity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="sem")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="division")
        self.student_table.heading("roll",text="Roll no")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOb")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="address")
        self.student_table.heading("fees",text="Fees")
        self.student_table.heading("adhaar",text="Adhaar")
        self.student_table.heading("caste",text="Caste")
        self.student_table.heading("ssc",text="SSC")
        self.student_table.heading("hsc",text="HSC")
        self.student_table.heading("cet",text="CET")
        self.student_table.heading("activity",text="Activity")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("fees",width=100)
        self.student_table.column("adhaar",width=100)
        self.student_table.column("caste",width=100)
        self.student_table.column("ssc",width=100)
        self.student_table.column("hsc",width=100)
        self.student_table.column("cet",width=100)
        self.student_table.column("activity",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()
    
    def fetch_data1(self):
        self.fetch_data()
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from s1")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def truncate(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("TRUNCATE TABLE s1")
        data=my_cursor.fetchall()
        self.fetch_data()

    def fetch_data(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT student.Dep,student.course,student.Year,student.Semester,student.Student_id,student.Name,student.Division,student.Roll,student.Gender,student.DOB,student.Email,student.Phone,student.Address,student.fees,student1.adhaar,student1.caste,student1.ssc,student1.hsc,student1.cet,student1.activity FROM student LEFT JOIN student1 ON student.Student_id=student1.Student_id ORDER BY `student`.`Student_id` ASC")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def search_data(self):
        if self.search_var.get()=="" or self.searchTxt_var.get()=="":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * FROM student LEFT JOIN student1 ON student.Student_id=student1.Student_id where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                    conn.commit()
                    #self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
    
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_fees.set(data[13])
        self.var_radio1.set(data[14]),


if __name__ == "__main__":
    root = Tk()
    obj = Showdetail(root)
    root.mainloop()