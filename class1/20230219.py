from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root = Tk()
root.title("20230219")
root.geometry("1000x300+500+150")

def start():
    pass
def stop():
    pass
#開啟圖片
img = Image.open("/Users/silvia/Documents/python_2023spring/logo_tree (1).png")
#轉換為tk圖片物件
tk_img = ImageTk.PhotoImage(img)
#設定程式icon
root.iconphoto(True,tk_img)
#建立 Label
# label1 = Label(root, text="flat",relief = "flat")
# label1.pack()
# #加入視窗
# label2 = Label(root,text="flat",relief="groove")
# label2.pack()
# label3 = Label(root,text="flat",relief="raised")
# label3.pack()
# label4 = Label(root,text="flat",relief="ridge")
# label4.pack()
# label5 = Label(root,text="flat",relief="solid")
# label5.pack()
# label6 = Label(root,text="flat",relief="sunken")
# label6.pack()
# mybutton1 = Button(root, text="start",bg="white")
# mybutton1.pack()
# mybutton2 = Button(root, text="stop",bg="white")
# mybutton2.pack()
statusBar = Label(root, text="processing...",fg="black",bg="white",anchor=W,relief="sunken",bd=2)
#加入視窗
statusBar.pack(side = "bottom",fill="x")
table = ttk.Treeview(root, columns=["Product Name","Unit Price","Quantity"])
# create columns title
table.heading("#0", text="Product Name")
table.heading("#1",text = "Unit Price")
table.heading("#2",text = "Quantity")
table.heading("#3",text = "Subtotal")
#set column type                                                     
table.column("#0",width=250,anchor=CENTER)
table.column("#1",anchor=CENTER)
table.column("#2",anchor=CENTER)
table.column("#3",anchor=CENTER)
#建立內容,從total行是用淺藍色底
table.tag_configure("totalcolor",background="#E7E2E2")

table.insert("", index= "end" ,text="sofa",values=("20000","2","40000"))
table.pack()
root.mainloop()