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
import base64
import io

from mysql.connector import cursor


class Moredetail:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1430x690+0+40")      #"width*height+x+y"
        self.root.title("More detail")
        

        #################variable###################
        self.var_std_id = StringVar()
        self.var_adhaar = StringVar()
        self.var_caste = StringVar()
        self.var_ssc = StringVar()
        self.var_hsc = StringVar()
        self.var_cet = StringVar()
        self.var_activity = StringVar()
        self.var_image = StringVar()
        self.var_image1 = StringVar()
        self.label = StringVar()
        
        
        
        
        
        

        #first image
        img = Image.open("Colleg_image/student.jpg")    ##r to convert intoo forward slash
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=500,height=130)

        #second image
        img1 = Image.open("Colleg_image/attend.jpg")    
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=500,y=0,width=500,height=130)

        #third image
        img2 = Image.open("Colleg_image/student.jpg")    
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb1 = Label(self.root,image=self.photoimg2)
        f_lb1.place(x=1000,y=0,width=500,height=130)  



        #bg_image       behind all img1,mg2,img so y=130
        img3 = Image.open("Colleg_image/red.jpg")    
        img3 = img3.resize((1430,690),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,bg="GREEN")
        bg_img.place(x=0,y=130,width=1430,height=690)

        title_lb1 = Label(bg_img,text="MORE DETAILS",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1430,height=45)  

        main_frame = Frame(bg_img,bd=2,bg="GREEN")     #br=border
        main_frame.place(x=5,y=55,width=1410,height=515)

        #left label frame
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="More Details",font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=10,width=665,height=480)

        
        #studentid
        studentId_label = Label(left_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #  #Aadharid
        # Name_label = Label(left_frame,text="Aadhar No:",font=("times new roman",13,"bold"),bg="white")
        # Name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        # Name_entry=ttk.Entry(left_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        # Name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Aadharid
        Aadharid_label = Label(left_frame,text="Aadhar No:",font=("times new roman",13,"bold"),bg="white")
        Aadharid_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Aadharid_entry=ttk.Entry(left_frame,textvariable=self.var_adhaar,width=19,font=("times new roman",13,"bold"))
        Aadharid_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Caste
        Caste_label = Label(left_frame,text="Caste:",font=("times new roman",13,"bold"),bg="white")
        Caste_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Caste_entry=ttk.Combobox(left_frame,textvariable=self.var_caste,font=("times new roman",12,"bold"),state="readonly",width=20)     #3readonly
        Caste_entry["values"] = ("Select Caste","General","OBC","SC","ST",)
        Caste_entry.current(0)
        Caste_entry.grid(row=1,column=1,padx=2,pady=10)

        #SSC 
        SSCmarks_label = Label(left_frame,text="10th Marks:",font=("times new roman",13,"bold"),bg="white")
        SSCmarks_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        SSCmarks_entry=ttk.Entry(left_frame,textvariable=self.var_ssc,width=19,font=("times new roman",13,"bold"))
        SSCmarks_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #HSC 
        HSCmarks_label = Label(left_frame,text="12th Marks:",font=("times new roman",13,"bold"),bg="white")
        HSCmarks_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        HSCmarks_entry=ttk.Entry(left_frame,textvariable=self.var_hsc,width=20,font=("times new roman",13,"bold"))
        HSCmarks_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #CET marks
        CETmarks_label = Label(left_frame,text="CET Percentile:",font=("times new roman",13,"bold"),bg="white")
        CETmarks_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        CETmarks_entry=ttk.Entry(left_frame,textvariable=self.var_cet,width=19,font=("times new roman",13,"bold"))
        CETmarks_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

          #Activites
        Activites_label = Label(left_frame,text="Activites:",font=("times new roman",13,"bold"),bg="white")
        Activites_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Activites_entry=ttk.Entry(left_frame,textvariable=self.var_activity,width=20,font=("times new roman",13,"bold"))
        Activites_entry.grid(row=3,column=1,padx=10,pady=5,ipady=20,sticky=W)

        

         #image file
        image_label = Label(left_frame,text="Image:",font=("times new roman",13,"bold"),bg="white")
        image_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        # image_btn = Button(left_frame,text="Browse",command=self.add_image,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # image_btn.grid(row=3,column=3)
        

        # img_label = Label(left_frame,text=" ")
        # img_label.grid(row=4,column=3),
        # img_label.configure()
        self.photo_frame = ttk.LabelFrame(left_frame,text="Photo")
        self.photo_frame.grid(row=4,column=1)
        self.button()
    

        


        

        #buttons frame
        btn_frame = Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=7,y=420,width=642,height=35)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=660,height=480)

        photo_lbl = Label(right_frame)
        photo_lbl.place(x=300,y=0,width=20,height=10)


        

        

        ##search frame
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=2,y=20,width=655,height=70)

        search_label = Label(search_frame,text="Search by:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        
        self.search_var = StringVar()
        search_combo = ttk.Combobox(search_frame,textvariable=self.search_var,font=("times new roman",12,"bold"),state="readonly",width=15)     #3readonly
        search_combo["values"] = ("Select Option","Student_id")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,sticky=W)

        self.searchTxt_var = StringVar()
        search_entry=ttk.Entry(search_frame,width=20,textvariable=self.searchTxt_var,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn = Button(search_frame,text="Search",width=9,command=self.search_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn = Button(search_frame,text="Show All",command=self.fetch_data,width=9,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        ###table frame
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=2,y=95,width=655,height=300)

        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table= ttk.Treeview(table_frame,column=("id","adhaar","caste","ssc","hsc","cet","activity","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        
        self.student_table.heading("id",text="ID")
        self.student_table.heading("adhaar",text="Adhaar")
        self.student_table.heading("caste",text="Caste")
        self.student_table.heading("ssc",text="SSC")
        self.student_table.heading("hsc",text="HSC")
        self.student_table.heading("cet",text="CET")
        self.student_table.heading("activity",text="Activity")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

    
        self.student_table.column("id",width=100)
        self.student_table.column("adhaar",width=100)
        self.student_table.column("caste",width=100)
        self.student_table.column("ssc",width=100)
        self.student_table.column("hsc",width=100)
        self.student_table.column("cet",width=100)
        self.student_table.column("activity",width=100)
        self.student_table.column("photo",width=200)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    def button(self):
        self.button=ttk.Button(self.photo_frame,text="Browser",command=self.add_image)
        self.button.grid(row=0,column=0)

    def add_image(self):
        self.var_image = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file", filetypes=(("JPG","*.jpg"), ("JPEG","*.jpeg"), ("PNG","*.png"), ("all files", "*.*")))
        self.label = ttk.Label(self.photo_frame,text="",width=27)
        self.label.grid(row=1,column=0)
        self.label.configure(text=self.var_image)
        
        global img
        img=Image.open(self.var_image)
        img = img.resize((170,160),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(img)

        self.label2=Label(self.photo_frame,image=photo)
        self.label2.image = photo
        self.label2.grid(row=2,column=0)
    
        
    




    def add_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student1 value(%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_std_id.get(),
                    self.var_adhaar.get(),
                    self.var_caste.get(),
                    self.var_ssc.get(),
                    self.var_hsc.get(),
                    self.var_cet.get(),
                    self.var_activity.get(),
                    self.var_image
                               ))
                conn.commit()
                self.fetch_data()
                
                conn.close()
                self.fetch_data()
                messagebox.showinfo("Success","Student details has been added Successsfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    def photo(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select photo from student1")
            conn.commit()
            self.fetch_data()
            
            conn.close()
            messagebox.showinfo("Success","Student details has been added Successsfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student1")
        data=my_cursor.fetchall()

        
    
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student1 where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted Student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_std_id.set(data[0]),
        self.var_adhaar.set(data[1]),
        self.var_caste.set(data[2]),
        self.var_ssc.set(data[3]),
        self.var_hsc.set(data[4]),
        self.var_cet.set(data[5]),
        self.var_activity.set(data[6]),
        self.var_image.set(data[7])

        

        
        
        

        

        

    def update_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you what to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student1 set adhaar=%s,caste=%s,ssc=%s,hsc=%s,cet=%s,activity=%s,photo=%s where Student_id=%s",(
                            self.var_adhaar.get(),
                            self.var_caste.get(),
                            self.var_ssc.get(),
                            self.var_hsc.get(),
                            self.var_cet.get(),
                            self.var_activity.get(),
                            self.var_image,
                            self.var_std_id.get()
                    ))
                else:
                    if not Upadate:
                        return 
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def search_data(self):
        if self.search_var.get()=="" or self.searchTxt_var.get()=="":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1 where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
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

    
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_adhaar.set(""),
        self.var_caste.set("Select Caste"),
        self.var_ssc.set(""),
        self.var_hsc.set(""),
        self.var_cet.set(""),
        self.var_activity.set(""),
        self.label.configure(text=""),
        self.label2.configure(image="")
        
        


if __name__ == "__main__":
    root = Tk()
    obj = Moredetail(root)
    root.mainloop()