import sys
from tkinter import Widget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox, QAction
from main import Face_Recognition_System
import tkinter
from tkinter import *
import os
import subprocess
import mysql.connector

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi(r"ui/login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbuttton.clicked.connect(self.gotocreate)
        

    # def loginfunction(self):
    #     username=self.username.text()
    #     password=self.password.text()
    #     print("Successfully login iiwth email ",username," and password ",password)
    #     list_of_files = os.listdir()
    #     if username in list_of_files:
    #         file1 = open(username, "r")
    #         verify = file1.read().splitlines()
    #         if password in verify:
    #             print("success loginin")
    #             self.new_window()
 
    #         else:
    #             QMessageBox.about(self,"Password","Wrong Password")
 
    #     else:
    #         QMessageBox.about(self,"Username","Wrong Username")

    def loginfunction(self):
        username=self.username.text()
        password=self.password.text()
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select username,password from user where username like '"+username+"'and password like '"+password+"'")
            result=my_cursor.fetchone()
            conn.commit()
            #self.fetch_data()
            conn.close()
        except Exception as es:
            QMessageBox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        
        if result==None:
            QMessageBox.about(self,"Password","Wrong Password")
        else:
            print("success loginin")
            self.new_window()

    
    # def login_success(self):
    #     print("success loginin")
    #     self.new_window()

    def new_window(self):
        # self.new_window = Toplevel(Tk())
        # self.app = Face_Recognition_System(self.new_window)
        subprocess.Popen(['Python','main.py'])
        self.close(QtWidgets.qApp.quit)
        
    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi(r"ui/createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    # def createaccfunction(self):
    #     username=self.username.text()
    #     if(self.password.text()==self.confirmpassword.text()):
    #         password=self.password.text()
    #         print("successfully created acc")
    #         file = open(username, "w")
    #         file.write(username + "\n")
    #         file.write(password)
    #         file.close()
    #         login=Login()
    #         widget.addWidget(login)
    #         widget.setCurrentIndex(widget.currentIndex()+1)

    def createaccfunction(self):
        username=self.username.text()
        if(self.password.text()==self.confirmpassword.text()):
            password=self.password.text()
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into user value(%s,%s)",(
                    username,password
                ))
                                        
                conn.commit()
                conn.close()
                QMessageBox.about(self,"Success","Student details has been added Successsfully")
            except Exception as es:
                QMessageBox.about(self,"Error",f"Due To :{str(es)}")
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
    

    

if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=Login()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(480)
    widget.setFixedHeight(600)
    widget.show()
    app.exec_()