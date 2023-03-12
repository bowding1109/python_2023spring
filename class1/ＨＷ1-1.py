from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk
root = Tk()
root.geometry("300x200")

button1 = Button(root,text = "start")
button2 = Button(root,text = "stop")

label1 = Label(root, text="初始化",fg="black",bg="white",anchor=W,relief="sunken",bd=2)
label1 .pack(side = "bottom",fill="x")

label2 = Label(root, text="運行中",fg="black",bg="white",anchor=W,relief="sunken",bd=2)
label2 .pack(side = "bottom",fill="x")

label3 = Label(root, text="已停止",fg="black",bg="white",anchor=W,relief="sunken",bd=2)
label3 .pack(side = "bottom",fill="x")

root.mainloop()