from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
root = Tk()
root.title("20230219")
root.geometry("1000x300+500+150")

table = ttk.Treeview(root, columns=["Product Name","Unit Price","Quantity"])
table.heading("#0", text="Product Name")
table.heading("#1",text = "Unit Price")
table.heading("#2",text = "Quantity")
table.heading("#3",text = "Subtotal")

table.column("#0",width=250,anchor=CENTER)
table.column("#1",anchor=CENTER)
table.column("#2",anchor=CENTER)
table.column("#3",anchor=CENTER)
table.pack()

root.mainloop()