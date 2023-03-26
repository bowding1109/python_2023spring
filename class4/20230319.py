from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title("20230319")
root.geometry("500x300")

# def getValue(e):
#     value.set("年齡: "+str(year_scale.get()))
# #建立 Scale 元件
# year_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue)
# year_scale.grid(row = 1, column = 0, columnspan = 3)

# value = StringVar()
# value.set("年齡: 0")

# statusBar = Label(root, textvariable = value, fg = "black",bg = "White",anchor = W,relief="sunken",bd = 2)
# statusBar.grid(row = 2,column=0,columnspan=3,sticky = W+E+S)


# value = StringVar()

# title1label2 = Label(root, text = "身高:")
# title1label2.grid(row =3 ,column= 0, columnspan= 2, sticky = W)

# title1label3 = Label(root, textvariable = value)
# title1label3.grid(row =3 ,column= 1, columnspan= 2, sticky = W)

# height = Spinbox(root,from_=99,to = 250, textvariable = value)
# height.grid(row = 4, column = 0, columnspan = 3, sticky=W+E+S)



title1label = Label(root,text = "請選擇顏色(R,G,B)")
title1label.grid(row=0,column=0,sticky=W)

def getValue_r(e):
    value.set("R: "+str(r_scale.get()))
#建立 Scale 元件
r_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_r)
r_scale.grid(row = 2, column = 0, columnspan = 3)

value = StringVar()
value.set("R: 0")

statusBar = Label(root, textvariable = value)
statusBar.grid(row = 1,column=0,columnspan=3,sticky = W)

def getValue_g(e):
    value.set("G: "+str(g_scale.get()))
#建立 Scale 元件
g_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_g)
g_scale.grid(row = 4, column = 0, columnspan = 3)

value = StringVar()
value.set("G: 0")

statusBar = Label(root, textvariable = value)
statusBar.grid(row = 3,column=0,columnspan=3,sticky = W)

def getValue_b(e):
    value.set("B: "+str(b_scale.get()))
#建立 Scale 元件
b_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_b)
b_scale.grid(row = 6, column = 0, columnspan = 3)

value = StringVar()
value.set("B: 0")

statusBar = Label(root, textvariable = value)
statusBar.grid(row = 5,column=0,columnspan=3,sticky = W)





root.mainloop()