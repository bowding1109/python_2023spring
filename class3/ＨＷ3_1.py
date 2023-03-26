from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
import tkinter.ttk as ttk
root = Tk()
root.title("20230219")
root.geometry("500x300")


def choose_brand():
    titleVar.set("廠牌: "+ str(box.current()+1)+"."+box.get())
    listVar = StringVar()

    BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
    Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
    Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]


    if box.get() == "BMW":
        listVar.set(BMW)
        listbox = Listbox(root,selectmode="extended",listvariable=listVar)
        listbox.grid(row = 4,column=0,sticky = W)
    elif box.get() == "Mercedes Benz":
        listVar.set(Mercedes)
        listbox = Listbox(root,selectmode="extended",listvariable=listVar)
        listbox.grid(row = 4,column=0,sticky = W)

    elif box.get() == "Audi":
        listVar.set(Audi)
        listbox = Listbox(root,selectmode="extended",listvariable=listVar)
        listbox.grid(row = 4,column=0,sticky = W)
    
titleVar = StringVar()
titleVar.set("廠牌:")

title1label = Label(root,textvariable=titleVar)
title1label.grid(row=0,column=0,sticky=W)

box = ttk.Combobox(root, values = ["BMW","Mercedes Benz","Audi"])
box.grid(row=1,column=0,sticky = W)
box.current(0)

btn1 = Button(root,text = "OK",command = choose_brand)
btn1.grid(row = 2,column=0,sticky=W)

label1 = Label(root,text = "請選擇型號:")
label1.grid(row=3,sticky=W)




# listbox.insert(1,"A1")
# listbox.insert(2,"A3")
# listbox.insert(3,"A4")


root.mainloop()