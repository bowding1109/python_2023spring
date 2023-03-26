from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
import tkinter.ttk as ttk
root = Tk()
root.title("20230219")
root.geometry("1000x300+500+150")


# sframe1 = ScrolledFrame(root,width=300,height = 300)
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
# btn3.grid(row = 2)
# btn4.grid(row = 3)
# btn5.grid(row = 4)
def choose_brand():
    titleVar.set("廠牌: "+ str(box.current()+1)+"."+box.get())
    
titleVar = StringVar()
titleVar.set("廠牌:")
#建立標題 Label
title1label = Label(root,textvariable=titleVar)
title1label.grid(row=0,column=0,columnspan=2,sticky=W)
#建立下拉式選單 Combobox
box = ttk.Combobox(root, values = ["BMW","Mercedes Benz","Audi"])
box.grid(row=1,column=0,sticky = W)
box.current(0)
# 建立按鈕 Button
btn1 = Button(root,text = "OK",command = choose_brand)
btn1.grid(row = 2,column=0,sticky=W)

# listbox = Listbox(root,selectmode="extended")
# listbox.grid()

listVar = StringVar()

BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]

listVar.set(BMW)

listbox = Listbox(root,selectmode="extended",listvariable=listVar)
listbox.grid(row = 2,column=0)


listbox.insert(1,"A1")
listbox.insert(2,"A3")
listbox.insert(3,"A4")

# filePath = filedialog.askopenfilename()

# filePath = filedialog.askopenfilename(title = "選取照片")

# filePath = filedialog.askopenfilename(title = "選取照片",initialdir = "/Users/silvia/Documents/python_2023spring/class3")

# filePath = filedialog.askopenfilename(title = "選取照片",initialdir = "/Users/silvia/Documents/python_2023spring/class2",multiple = True)
# print(filePath)

root.mainloop()


