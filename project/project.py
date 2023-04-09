from tkinter import *
from tkinter import messagebox 
import tkinter.ttk as ttk
from PIL import Image, ImageTk




def showdetail():
    detailWindow = Toplevel(root)
    detailWindow.title("KubeTech Shop")
    detailWindow.geometry("850x250")

    table = ttk.Treeview(detailWindow, columns=["Product Name","Unit Price","Quantity"])
    table.heading("#0", text="Product Name")
    table.heading("#1",text = "Unit Price")
    table.heading("#2",text = "Quantity")
    table.heading("#3",text = "Subtotal")

    table.column("#0",width=250,anchor=CENTER)
    table.column("#1",anchor=CENTER)
    table.column("#2",anchor=CENTER)    
    table.column("#3",anchor=CENTER)
    table.tag_configure("totalcolor",background="#E7E2E2")

    subtotal1 = int(productnumberlabel1["text"])*int(product1price["text"].split(".")[1].replace(",",""))
    table.insert("", index= "end" ,text= productname1["text"],values= [product1price["text"],productnumberlabel1["text"],subtotal1])
    
    subtotal2 = int(productnumberlabel2["text"])*int(product2price["text"].split(".")[1].replace(",",""))
    table.insert("", index= "end" ,text= productname2["text"] ,values= [product1price["text"],productnumberlabel2["text"],subtotal2])

    subtotal3 = int(productnumberlabel3["text"])*int(product3price["text"].split(".")[1].replace(",",""))
    table.insert("", index= "end" ,text=productname3["text"],values= [product1price["text"],productnumberlabel3["text"],subtotal3])

    subtotal4 = int(productnumberlabel4["text"])*int(product4price["text"].split(".")[1].replace(",",""))
    table.insert("", index= "end" ,text=productname4["text"],values= [product1price["text"],productnumberlabel4["text"],subtotal4])

    table.pack()
    detailWindow.mainloop()

def add(numlabel,pricelabel):
    numlabel["text"] = int(numlabel["text"])+1
    price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
    total = int(totalval.get().split(":")[1].replace("元","").strip())
    totalval.set("共消費: "+str(total+price)+" 元")
def minus(numlabel,pricelabel):
    if int(numlabel["text"])>0:
        numlabel["text"] = int(numlabel["text"])-1
        price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
        total = int(totalval.get().split(":")[1].replace("元","").strip())
        totalval.set("共消費: "+str(total-price)+" 元")
    else:
        messagebox.showwarning("showarnng","The number of products can\'t be below 0.")


root = Tk()

root.title("書店網站")

root.geometry("880x650")
#row = 0
titleimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image = titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

sofabutton = Button(root,font = ("Inter",18), text="小說", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
sofabutton.grid(column=1,row=0,sticky = E+W,padx=5)

beddingbutton = Button(root,font = ("Inter",18), text="漫畫", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2)
beddingbutton.grid(column=2,row=0,sticky = E+W,padx=5)

kitchenwarebutton = Button(root,font = ("Inter",18), text="雜誌", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
kitchenwarebutton.grid(column=3,row=0,sticky = E+W,padx=5)

loginbutton = Button(root,font = ("Inter",18), text="會員登入/註冊", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,)
loginbutton.grid(column=7,row=0,sticky = E+W,padx=5)
#row=1
bannerimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/封面.png")
bannerimg = bannerimg.resize((852,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image = bannerimg).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

#row=2
sofa1img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/漫畫.png")
sofa1img = sofa1img.resize((202,200))
sofa1img = ImageTk.PhotoImage(sofa1img)
sofa1label = Label(root, image = sofa1img).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

sofa2img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/小說2.png")
sofa2img = sofa2img.resize((202,200))
sofa2img = ImageTk.PhotoImage(sofa2img)
sofa2label = Label(root, image = sofa2img).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

sofa3img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/雜誌.png")
sofa3img = sofa3img.resize((202,200))
sofa3img = ImageTk.PhotoImage(sofa3img)
sofa3label = Label(root, image = sofa3img).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

sofa4img = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/小說.png")
sofa4img = sofa4img.resize((202,200))
sofa4img = ImageTk.PhotoImage(sofa4img)
sofa4label = Label(root, image = sofa4img).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

#row=3
productname1 = Label(root,font = ("Inter",11), text="SPY×FAMILY 間諜家家酒【1-9集】", fg = "#000000",bg = "#ECE8E7")
productname1.grid(column=0,row=3,columnspan=2 ,padx=5)

productname2 = Label(root,font = ("Inter",11), text="你要好好的", fg = "#000000",bg = "#ECE8E7")
productname2.grid(column=2,row=3,columnspan=2,padx=5)

productname3 = Label(root,font = ("Inter",11), text="少年牛頓雜誌 11月號/2022 第218期", fg = "#000000",bg = "#ECE8E7")
productname3.grid(column=4,row=3,columnspan=2,padx=5)

productname4 = Label(root,font = ("Inter",11), text="紅樓夢", fg = "#000000",bg = "#ECE8E7")
productname4.grid(column=6,row=3,columnspan=2,padx=5)

#row=4
product1price = Label(root,font = ("Inter",10), text="NT.0,846", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=0,row=4 ,padx=5,sticky=W)

product2price = Label(root,font = ("Inter",10), text="NT.0,329", fg = "#000000",bg = "#ECE8E7")
product2price.grid(column=2,row=4 ,padx=5, sticky=W)

product3price = Label(root,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
product3price.grid(column=4,row=4 ,padx=5, sticky=W)

product4price = Label(root,font = ("Inter",10), text="NT.0,359", fg = "#000000",bg = "#ECE8E7")
product4price.grid(column=6,row=4 ,padx=5, sticky=W)

productnumberlabel1 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel1.grid(column=1,row=4)

productnumberlabel2 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel2.grid(column=3,row=4)

productnumberlabel3 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel3.grid(column=5,row=4)

productnumberlabel4 = Label(root,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel4.grid(column=7,row=4)

addbutton1 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel1,product1price))
addbutton1.grid(column=1,row=4 ,sticky=E)

addbutton2 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel2,product2price))
addbutton2.grid(column=3,row=4 ,sticky=E)

addbutton3 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel3,product3price))
addbutton3.grid(column=5,row=4 ,sticky=E)

addbutton4 = Button(root,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel4,product4price))
addbutton4.grid(column=7,row=4 ,sticky=E)

minusbutton1 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel1,product1price))
minusbutton1.grid(column=1,row=4 ,sticky=W)

minusbutton2 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel2,product2price))
minusbutton2.grid(column=3,row=4 ,sticky=W)

minusbutton3 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel3,product3price))
minusbutton3.grid(column=5,row=4 ,sticky=W)

minusbutton4 = Button(root,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel4,product4price))
minusbutton4.grid(column=7,row=4 ,sticky=W)

#row5
root.rowconfigure(5,weight=2)

detaillistbutton = Button(root,font = ("Inter",10), text="詳細清單", fg = "#1E1E1E",bg = "#E7E2E2",command = showdetail)
detaillistbutton.grid(row=5, column = 0, sticky = W+S, padx = 5, pady =1 )

ShoppingCart = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/Shopping Cart.png")
ShoppingCart = ShoppingCart.resize((30,30))
ShoppingCart = ImageTk.PhotoImage(ShoppingCart)
Cartlabel = Label(root, image = ShoppingCart,width = 30,height = 30)
Cartlabel.grid(column = 5,row = 5,sticky=E+S)

totalval = StringVar()
totalval.set("共消費:0元")
totallabel = Label(root,textvariable=totalval,font=("Inter",18),fg="#000000")
totallabel.grid(row = 5, column= 6,columnspan= 2, sticky = W+S)

checkoutbutton = Button(root,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2")
checkoutbutton.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )



root.mainloop()