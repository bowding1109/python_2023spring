from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk


root = Tk()
root.title("20230219")
root.geometry("1000x300+500+150")

def show():
    text = (checkbtnVal1.get())+" "+(checkbtnVal2.get())+" "+(checkbtnVal3.get())
    statusBar2["text"] = text

checkbtnVal1 = StringVar()
checkbtnVal2 = StringVar()
checkbtnVal3 = StringVar()

title2label = Label(root,text = "轉機次數:")
title2label.grid(row=0,column=0,sticky=W)

checkbtn1 = Checkbutton(root,text="直飛",variable = checkbtnVal1,onvalue="直飛",offvalue="",fg="pink",command=show)
checkbtn1.grid(row=1,column=0,sticky=W)

checkbtn2 = Checkbutton(root,text="轉機1次",variable = checkbtnVal2,onvalue="轉機1次",offvalue="",fg="pink",command=show)
checkbtn2.grid(row=1,column=1,sticky=W)

checkbtn3 = Checkbutton(root,text="轉機2次以上",variable = checkbtnVal3,onvalue="轉機2次以上",offvalue="",fg="pink",command=show)
checkbtn3.grid(row=1,column=2,sticky=W)

statusBar2 = Label(root,text="",fg="black",bg="white",anchor=W,relief="sunken",bd=2)

statusBar2.grid(row=10,column=0,columnspan=3,sticky=W+E+S)

# sframe1 = ScrolledFrame(root)
# sframe1.grid()

# sframe1.bind_arrow_keys(root)
# sframe1.bind_scroll_wheel(root)

# inner_frame = sframe1.display_widget(Frame)

# btn1 = Button(inner_frame,text = "1",height = 5)
# btn2 = Button(inner_frame,text = "2",height = 5)
# btn3 = Button(inner_frame,text = "3",height = 5)
# btn4 = Button(inner_frame,text = "4",height = 5)
# btn5 = Button(inner_frame,text = "5",height = 5)
# btn1.grid(row = 0)
# btn2.grid(row = 1)
# # btn3.grid(row = 2)
# # btn4.grid(row = 3)
# # btn5.grid(row = 4)

root.mainloop()