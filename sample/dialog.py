import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

user_inp=simpledialog.askstring("test","what is your naem?:")

print("heelo",user_inp)