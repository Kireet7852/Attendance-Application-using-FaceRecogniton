from logging import log
import subprocess
from tkinter import Tk,Label, Toplevel
from time import sleep
from tkinter import *
from main import Face_Recognition_System


class LoadingSplash:
    def __init__(self,root):
        #seettting root window
        self.root=root
        self.root.config(bg="black")
        self.root.title("Custom Loader")
        self.root.attributes("-fullscreen",True)

        #loading text:
        Label(self.root,text="Loading....",font="Bahnschrift 15",bg="black",fg="#FFBD09").place(x=490,y=320)

        #loading blocks:
        for i in range(15):
            Label(self.root, bg="#1F2732",width=2,height=1).place(x=(i+22)*22,y=350)

        #update root to see animation:
        self.root.update()
        self.play_animation()

        
    
    #loader animation:
    def play_animation(self):
        for i in range(4):
            for j in range(16):
                #make block yellow:
                Label(self.root,bg="#FFBD09",width=2,height=1).place(x=(j+22)*22,y=350)
                sleep(0.06)
                self.root.update_idletasks()
                #make block darker:
                Label(self.root,bg="#1F2732",width=2,height=1).place(x=(j+22)*22,y=350)
        self.main_page()
        
            

    def main_page(self):
        self.root.destroy()
        # self.new_window = Tk()
        # self.app = login(self.new_window)
        subprocess.Popen(['Python','login_ui.py'])

if __name__ == "__main__":
    root = Tk()
    obj = LoadingSplash(root)
    root.mainloop()