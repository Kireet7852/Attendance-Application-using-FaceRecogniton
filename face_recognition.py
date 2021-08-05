from logging import setLogRecordFactory
from os import pardir
from tkinter import *
from tkinter import ttk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import data
import mysql.connector
from time import strftime
from tkinter import simpledialog
from datetime import datetime
import cv2
import os
import numpy as np
import shutil



class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x690+0+40")      #"width*height+x+y"
        self.root.title("Face Recognition Sytem")


        title_lb1 = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lb1.place(x=0,y=0,width=1430,height=45)

        #1st image
        img_top = Image.open("Colleg_image/face3.jpg")    ##r to convert intoo forward slash
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lb1 = Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=650,height=700)

        #2nd image
        img_bottom = Image.open("Colleg_image/face4.jpg")    ##r to convert intoo forward slash
        img_bottom = img_bottom.resize((680,700),Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lb1 = Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=650,y=55,width=680,height=700)

        #button
        b1_1 = Button(f_lb1,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=360,y=570,width=200,height=40)

    #######attendance##########
    def mark_attendance(self,i,r,n,d):
        

        with open("attendances.csv","r+",newline="\n") as f:

            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present,")

    def clock_out(self):
        with open("clock_out.csv","w") as f:
            now=datetime.now()
            ltString=now.strftime("%H:%M:%S")  
            f.write(f"{ltString}\n") 
        
        
    

    def timesheet(self):
        file1 = "attendances.csv"
        file2 = "clock_out.csv"
        file=simpledialog.askstring("Filename","Enter the filename:")
        with open(file+".csv","w") as outfile:
            for files in (file1,file2):
                with open(files) as  infile:
                    outfile.write(infile.read())

    

    

                


    ##########face recognition#############
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1) & 0xFF==ord('q'):
                self.clock_out()
                break
        video_cap.release()
        cv2.destroyAllWindows()

        self.timesheet()
        
    
    
    
            

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()