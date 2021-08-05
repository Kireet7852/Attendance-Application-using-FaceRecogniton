from tkinter import *
from tkinter import messagebox

def click():
    pname = file.get()
    read = open(pname+".txt","w")
    content = read.write("pj u")
    print(content)
    read.close()
    messagebox.showinfo("Vlaue",pname)

root = Tk()
root.geometry("200x100+400+100")
root.title("File Name")
file= StringVar()

screen = Entry(root,textvariable=file,font="lucida 19 bold")
screen.pack(fill=X,ipadx=8,pady=15,padx=8)

f = Frame(root,bg="grey")
f.pack()
b=Button(f,text="Name of the file",command=click)
b.pack(side=LEFT)




root.mainloop()