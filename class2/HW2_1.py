from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
import tkinter.ttk as ttk

root = Tk()
root.geometry("300x100")

sframe1 = ScrolledFrame(root)
sframe1.grid()

sframe1.bind_arrow_keys(root)
sframe1.bind_scroll_wheel(root)

inner_frame = sframe1.display_widget(Frame)

def show():
    text = (checkbtnVal1.get())+" "+(checkbtnVal2.get())+" "+(checkbtnVal3.get())+(checkbtnVal5.get())+" "+(checkbtnVal6.get())+" "+(checkbtnVal7.get())+" "
    statusBar2["text"] = text

checkbtnVal1 = StringVar()
checkbtnVal2 = StringVar()
checkbtnVal3 = StringVar()
checkbtnVal5 = StringVar()
checkbtnVal6 = StringVar()
checkbtnVal7 = StringVar()

title2label = Label(inner_frame,text = "請選擇餐點種類:")
title2label.grid(row=0,column=0,sticky=W)

checkbtn1 = Checkbutton(inner_frame,text="和牛",variable = checkbtnVal1,onvalue="和牛",offvalue="",fg="pink",command=show)
checkbtn1.grid(row=1,column=0,sticky=W)

checkbtn2 = Checkbutton(inner_frame,text="伊比利豬",variable = checkbtnVal2,onvalue="伊比利豬",offvalue="",fg="pink",command=show)
checkbtn2.grid(row=1,column=1,sticky=W)

checkbtn3 = Checkbutton(inner_frame,text="海鮮",variable = checkbtnVal3,onvalue="海鮮",offvalue="",fg="pink",command=show)
checkbtn3.grid(row=1,column=2,sticky=W)

checkbtn4 = Label(inner_frame,text="請選擇飲料種類:")
checkbtn4.grid(row=2,column=0,sticky=W)

checkbtn5 = Checkbutton(inner_frame,text="莊園咖啡",variable = checkbtnVal5,onvalue="莊園咖啡",offvalue="",fg="pink",command=show)
checkbtn5.grid(row=3,column=0,sticky=W)

checkbtn6 = Checkbutton(inner_frame,text="日月潭蜜香紅茶",variable = checkbtnVal6,onvalue="日月潭蜜香紅茶",offvalue="",fg="pink",command=show)
checkbtn6.grid(row=3,column=1,sticky=W)

checkbtn7 = Checkbutton(inner_frame,text="伯爵奶茶",variable = checkbtnVal7,onvalue="伯爵奶茶",offvalue="",fg="pink",command=show)
checkbtn7.grid(row=3,column=2,sticky=W)


statusBar2 = Label(inner_frame,text="",fg="black",bg="white",anchor=W,relief="sunken",bd=2)

statusBar2.grid(row=4,column=0,columnspan=3,sticky=W+E+S)


















root.mainloop()