from tkinter import *
from PIL import Image, ImageTk
from tkscrolledframe import ScrolledFrame
from tkinter import ttk
from tkinter import filedialog
import tkinter.ttk as ttk

root = Tk()
root.title("20230319")
root.geometry("500x300")

# title1label = Label(root,text = "請選擇顏色(R,G,B)")
# title1label.grid(row=0,column=0,sticky=W)

# def getValue_r(e):
#     r_value.set("R: "+str(r_scale.get()))
# #建立 Scale 元件
# r_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_r)
# r_scale.grid(row = 2, column = 0, columnspan = 3)

# r_value = StringVar()
# r_value.set("R: 0")

# statusBar = Label(root, textvariable = r_value)
# statusBar.grid(row = 1,column=0,columnspan=3,sticky = W)

# def getValue_g(e):
#     g_value.set("G: "+str(g_scale.get()))
# #建立 Scale 元件
# g_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_g)
# g_scale.grid(row = 4, column = 0, columnspan = 3)

# g_value = StringVar()
# g_value.set("G: 0")

# statusBar = Label(root, textvariable = g_value)
# statusBar.grid(row = 3,column=0,columnspan=3,sticky = W)

# def getValue_b(e):
#     b_value.set("B: "+str(b_scale.get()))
# #建立 Scale 元件
# b_scale = Scale(root,from_ = 0, to = 100, orient= "horizontal",resolution= 1,length = 300,showvalue = True, command = getValue_b)
# b_scale.grid(row = 6, column = 0, columnspan = 3)

# b_value = StringVar()
# b_value.set("B: 0")

# statusBar = Label(root, textvariable = b_value)
# statusBar.grid(row = 5,column=0,columnspan=3,sticky = W)

#建立下getValue function
def getValue(a):
    #取得RGB
    r = int(color_scale1.get())
    g = int(color_scale2.get())
    b = int(color_scale3.get())
    #數值轉換為16進位
    hex = "#{:02x}{:02x}{:02x}".format(r,g,b)
    #分別設定Label 文字內容
    title1label1["text"]="R: "+str(color_scale1.get())
    title1label2["text"]="G  "+str(color_scale2.get())
    title1label3["text"]= "B: "+str(color_scale3.get())

    statusBar1["bg"] = hex
    statusBar1["text"] = hex
#建立標題Label
title1label = Label(root, text="選擇顏色(R,G,B)")
title1label.grid(row = 0,column= 0,columnspan= 2, sticky=W)
#建立Scale元件
color_scale1 = Scale(root, from_=0, to=225, orient="horizontal", resolution=1,length=300,showvalue=True,command=getValue)
color_scale1.grid(row=2,column=0,columnspan=3)

color_scale2 = Scale(root, from_=0, to=225, orient="horizontal", resolution=1,length=300,showvalue=True,command=getValue)
color_scale2.grid(row=4,column=0,columnspan=3)

color_scale3 = Scale(root, from_=0, to=225, orient="horizontal", resolution=1,length=300,showvalue=True,command=getValue)
color_scale3.grid(row=6,column=0,columnspan=3)
#建立標題 Label
title1label1 = Label(root, text="R:0")
title1label1.grid(row=1,column=0,columnspan=2,sticky=W)
#建立標題 Label
title1label2 = Label(root, text="G:0")
title1label2.grid(row=3,column=0,columnspan=2,sticky=W)
#建立標題 Label
title1label3 = Label(root, text="B:0")
title1label3.grid(row=5,column=0,columnspan=2,sticky=W)
#建立 Label
statusBar1 = Label(root, text = "",fg = "white",bg = "white",relief = "sunken",bd = 2,font = (20),anchor = "center")
statusBar1.grid(row=7,column=0,columnspan=3,sticky=W+E+S)



root.mainloop()