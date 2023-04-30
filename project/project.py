from tkinter import *
from tkinter import messagebox 
import tkinter.ttk as ttk
from PIL import Image, ImageTk

#超基本設定
root = Tk()

root.title("KubeTech Shop")
root.geometry("950x750")




def info(name,price,imgurl1,imurl2):
    infoScreen = Toplevel(root)
    infoScreen.geometry("200x500")
    productNameLabel=Label(infoScreen,text=name)
    productNameLabel.grid(row=0,column=0)
    princeLabel=Label(infoScreen,text=price)
    princeLabel.grid(row=1,column=0)
    infoScreen.mainloop()



#任天堂頁面

#基本設定
def nitendo():
    A1 = Toplevel(root)
    A1.title("KubeTech Shop1")
    A1.geometry("950x750")

    #row 0
    titleimgA = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
    titleimgA = titleimgA.resize((32,32))
    titleimgA = ImageTk.PhotoImage(titleimgA)
    titlelabelA = Label(A1, image = titleimgA,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

    sofabuttonA = Button(A1,font = ("Inter",18), text="熱門遊戲", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2,)
    sofabuttonA.grid(column=1,row=0,sticky = E+W,padx=5)

    beddingbuttonA = Button(A1,font = ("Inter",18), text="折價區", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2)
    beddingbuttonA.grid(column=2,row=0,sticky = E+W,padx=5)

    kitchenwarebuttonA = Button(A1,font = ("Inter",18), text="周邊商品", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
    kitchenwarebuttonA.grid(column=3,row=0,sticky = E+W,padx=5)

    loginbuttonA = Button(A1,font = ("Inter",18), text="會員登入/註冊", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,)
    loginbuttonA.grid(column=7,row=0,sticky = E+W,padx=5)

    #row=1
    bannerimgA = Image.open("./project/img/topic2.png")
    bannerimgA = bannerimgA.resize((900,298))
    bannerimgA = ImageTk.PhotoImage(bannerimgA)
    bannerlabelA = Label(A1, image = bannerimgA).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

    #row=2
    sofa1imgA = Image.open("./project/img/switch_game4.png")
    sofa1imgA = sofa1imgA.resize((220,290))
    sofa1imgA = ImageTk.PhotoImage(sofa1imgA)
    sofa1labelA = Label(A1, image = sofa1imgA).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa2imgA = Image.open("./project/img/switch_game5.png")
    sofa2imgA = sofa2imgA.resize((220,290))
    sofa2imgA = ImageTk.PhotoImage(sofa2imgA)
    sofa2labelA = Label(A1, image = sofa2imgA).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa3imgA = Image.open("./project/img/switch_game6.png")
    sofa3imgA = sofa3imgA.resize((220,290))
    sofa3imgA = ImageTk.PhotoImage(sofa3imgA)
    sofa3labelA = Label(A1, image = sofa3imgA).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa4imgA = Image.open("./project/img/switch_game7.png")
    sofa4imgA = sofa4imgA.resize((220,290))
    sofa4imgA = ImageTk.PhotoImage(sofa4imgA)
    sofa4labelA = Label(A1, image = sofa4imgA).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

    #row=3
    productname1A = Label(A1,font = ("Inter",11), text="馬力歐賽車8 豪華版", fg = "#000000",bg = "#ECE8E7")
    productname1A.grid(column=0,row=3,columnspan=2 ,padx=5)

    productname2A = Label(A1,font = ("Inter",11), text="瑪利歐高爾夫 超級衝衝", fg = "#000000",bg = "#ECE8E7")
    productname2A.grid(column=2,row=3,columnspan=2,padx=5)

    productname3A = Label(A1,font = ("Inter",11), text="瑪利歐兄弟U 豪華版", fg = "#000000",bg = "#ECE8E7")
    productname3A.grid(column=4,row=3,columnspan=2,padx=5)

    productname4A = Label(A1,font = ("Inter",11), text="寶可夢 朱", fg = "#000000",bg = "#ECE8E7")
    productname4A.grid(column=6,row=3,columnspan=2,padx=5)

    #row=4
    product1price1A = Label(A1,font = ("Inter",10), text="NT.0,846", fg = "#000000",bg = "#ECE8E7")
    product1price1A.grid(column=0,row=4 ,padx=5,sticky=W)

    product2price1A = Label(A1,font = ("Inter",10), text="NT.0,329", fg = "#000000",bg = "#ECE8E7")
    product2price1A.grid(column=2,row=4 ,padx=5, sticky=W)

    product3price1A = Label(A1,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
    product3price1A.grid(column=4,row=4 ,padx=5, sticky=W)

    product4price1A = Label(A1,font = ("Inter",10), text="NT.0,359", fg = "#000000",bg = "#ECE8E7")
    product4price1A.grid(column=6,row=4 ,padx=5, sticky=W)

    productnumberlabel1A = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel1A.grid(column=1,row=4)

    productnumberlabel2A = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel2A.grid(column=3,row=4)

    productnumberlabel3A = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel3A.grid(column=5,row=4)

    productnumberlabel4A = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel4A.grid(column=7,row=4)

    addbutton1A = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel1A,product1price1A))
    addbutton1A.grid(column=1,row=4 ,sticky=E)

    addbutton2A = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel2A,product2price1A))
    addbutton2A.grid(column=3,row=4 ,sticky=E)

    addbutton3A = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel3A,product3price1A))
    addbutton3A.grid(column=5,row=4 ,sticky=E)

    addbutton4A = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel4A,product4price1A))
    addbutton4A.grid(column=7,row=4 ,sticky=E)

    minusbutton1A = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel1A,product1price1A))
    minusbutton1A.grid(column=1,row=4 ,sticky=W)

    minusbutton2A = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel2A,product2price1A))
    minusbutton2A.grid(column=3,row=4 ,sticky=W)

    minusbutton3A = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel3A,product3price1A))
    minusbutton3A.grid(column=5,row=4 ,sticky=W)

    minusbutton4A = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel4A,product4price1A))
    minusbutton4A.grid(column=7,row=4 ,sticky=W)


    ShoppingCartA = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/Shopping Cart.png")
    ShoppingCartA = ShoppingCartA.resize((30,30))
    ShoppingCartA = ImageTk.PhotoImage(ShoppingCartA)
    CartlabelA = Label(A1, image = ShoppingCartA,width = 30,height = 30)
    CartlabelA.grid(column = 5,row = 5,sticky=E+S)

    totalvalA = StringVar()
    totalvalA.set("共消費:0元")
    totallabelA = Label(A1,textvariable=totalval,font=("Inter",18),fg="#000000")
    totallabelA.grid(row = 5, column= 6,columnspan= 2, sticky = W+S)

    checkoutbuttonA = Button(A1,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2")
    checkoutbuttonA.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )
    A1.mainloop()














    #PlatStation頁面

#基本設定

#row 0
def playstation():
    B2 = Toplevel(root)
    B2.title("KubeTech Shop2")
    B2.geometry("950x750")
    titleimg2 = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
    titleimg2 = titleimg2.resize((32,32))
    titleimg2 = ImageTk.PhotoImage(titleimg2)
    titlelabel2 = Label(B2, image = titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

    beddingbutton2 = Button(B2,font = ("Inter",18), text="熱門遊戲", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2)
    beddingbutton2.grid(column=2,row=0,sticky = E+W,padx=5)

    sofabutton2 = Button(B2,font = ("Inter",18), text="折價區", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2)
    sofabutton2.grid(column=1,row=0,sticky = E+W,padx=5)

    kitchenwarebutton2 = Button(B2,font = ("Inter",18), text="周邊商品", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
    kitchenwarebutton2.grid(column=3,row=0,sticky = E+W,padx=5)

    loginbutton2 = Button(B2,font = ("Inter",18), text="會員登入/註冊", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,)
    loginbutton2.grid(column=7,row=0,sticky = E+W,padx=5)

    #row=1
    bannerimg2 = Image.open("./project/img/topic3.png")
    bannerimg2= bannerimg2.resize((900,298))
    bannerimg2 = ImageTk.PhotoImage(bannerimg2)
    bannerlabel2 = Label(B2, image = bannerimg2).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

    #row=2
    sofa1img2 = Image.open("./project/img/switch_game1.png")
    sofa1img2 = sofa1img2.resize((220,290))
    sofa1img2 = ImageTk.PhotoImage(sofa1img2)
    sofa1label2 = Label(B2, image = sofa1img2).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa2img2 = Image.open("./project/img/PlayStation_game2.png")
    sofa2img2 = sofa2img2.resize((220,290))
    sofa2img2 = ImageTk.PhotoImage(sofa2img2)
    sofa2label2 = Label(B2, image = sofa2img2).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa3img2 = Image.open("./project/img/switch_game2.png")
    sofa3img2 = sofa3img2.resize((220,290))
    sofa3img2 = ImageTk.PhotoImage(sofa3img2)
    sofa3label2 = Label(B2, image = sofa3img2).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

    sofa4img2 = Image.open("/./project/img/PlayStation_game1.png")
    sofa4img2 = sofa4img2.resize((220,290))
    sofa4img2 = ImageTk.PhotoImage(sofa4img2)
    sofa4label2 = Label(B2, image = sofa4img2).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

    #row=3
    productname12 = Label(B2,font = ("Inter",11), text="星之卡比 豪華版 Wili", fg = "#000000",bg = "#ECE8E7")
    productname12.grid(column=0,row=3,columnspan=2)

    productname22 = Label(B2,font = ("Inter",11), text="霍格華滋的傳承", fg = "#000000",bg = "#ECE8E7")
    productname22.grid(column=2,row=3,columnspan=2)

    productname32 = Label(B2,font = ("Inter",11), text="世界遊戲大全51", fg = "#000000",bg = "#ECE8E7")
    productname32.grid(column=4,row=3,columnspan=2)

    productname42 = Label(B2,font = ("Inter",11), text="SPIDER-MAN Miles Morales", fg = "#000000",bg = "#ECE8E7")
    productname42.grid(column=6,row=3,columnspan=2)

    #row=4
    product1price22 = Label(B2,font = ("Inter",10), text="NT.0,846", fg = "#000000",bg = "#ECE8E7")
    product1price22.grid(column=0,row=4 ,padx=5,sticky=W)

    product2price22 = Label(B2,font = ("Inter",10), text="NT.0,329", fg = "#000000",bg = "#ECE8E7")
    product2price22.grid(column=2,row=4 ,padx=5, sticky=W)

    product3price22 = Label(B2,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
    product3price22.grid(column=4,row=4 ,padx=5, sticky=W)

    product4price22 = Label(B2,font = ("Inter",10), text="NT.0,359", fg = "#000000",bg = "#ECE8E7")
    product4price22.grid(column=6,row=4 ,padx=5, sticky=W)

    productnumberlabel12 = Label(B2,width = 3 ,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel12.grid(column=1,row=4)

    productnumberlabel22 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel22.grid(column=3,row=4)

    productnumberlabel32 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel32.grid(column=5,row=4)

    productnumberlabel42 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    productnumberlabel42.grid(column=7,row=4)

    addbutton12 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel12,product1price22))
    addbutton12.grid(column=1,row=4 ,sticky=E)

    addbutton22 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel22,product2price22))
    addbutton22.grid(column=3,row=4 ,sticky=E)

    addbutton32 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel32,product3price22))
    addbutton32.grid(column=5,row=4 ,sticky=E)

    addbutton42 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(productnumberlabel42,product4price22))
    addbutton42.grid(column=7,row=4 ,sticky=E)

    minusbutton12 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel12,product1price22))
    minusbutton12.grid(column=1,row=4 ,sticky=W)

    minusbutton22 = Button(root,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel22,product2price22))
    minusbutton22.grid(column=3,row=4 ,sticky=W)

    minusbutton32 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel32,product3price22))
    minusbutton32.grid(column=5,row=4 ,sticky=W)

    minusbutton42 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(productnumberlabel42,product4price22))
    minusbutton42.grid(column=7,row=4 ,sticky=W)


    ShoppingCart2 = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/Shopping Cart.png")
    ShoppingCart2 = ShoppingCart2.resize((30,30))
    ShoppingCart2 = ImageTk.PhotoImage(ShoppingCart2)
    Cartlabel2 = Label(B2, image = ShoppingCart2,width = 30,height = 30)
    Cartlabel2.grid(column = 5,row = 5,sticky=E+S)

    totalval2 = StringVar()
    totalval2.set("共消費:0元")
    totallabel2 = Label(B2,textvariable=totalval,font=("Inter",18),fg="#000000")
    totallabel2.grid(row = 5, column= 6,columnspan= 2, sticky = W+S)

    checkoutbutton2 = Button(B2,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2")
    checkoutbutton2.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )
    B2.mainloop()





























#主頁面

#基本設定for title
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

#row 0
titleimg = Image.open("project/img/logo_tree.png")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image = titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

beddingbutton = Button(root,font = ("Inter",18), text="PlayStayion", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,command = playstation)
beddingbutton.grid(column=2,row=0,sticky = E+W,padx=5)

sofabutton = Button(root,font = ("Inter",18), text="任天堂Nintendo", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2,command= nitendo)
sofabutton.grid(column=1,row=0,sticky = E+W,padx=5)

loginbutton = Button(root,font = ("Inter",18), text="會員登入/註冊", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,)
loginbutton.grid(column=7,row=0,sticky = E+W,padx=5)

#row=1
bannerimg = Image.open("./project/img/topic.png")
bannerimg = bannerimg.resize((900,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image = bannerimg).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

#row=2
sofa1img = Image.open("./project/img/switch_game1.png")
sofa1img = sofa1img.resize((220,290))
sofa1img = ImageTk.PhotoImage(sofa1img)
sofa1label = Button(root, image = sofa1img,command=lambda:info("星之卡比 豪華版 Wili","NT.0,846"))
sofa1label.grid(column = 0,row = 2,columnspan=2)
sofa2img = Image.open("./project/img/PlayStation_game2.png")
sofa2img = sofa2img.resize((220,290))
sofa2img = ImageTk.PhotoImage(sofa2img)
sofa2label = Button(root, image = sofa2img,command=lambda:info("霍格華滋的傳承","NT.0,329")).grid(column = 2,row = 2,columnspan=2)

sofa3img = Image.open("./project/img/switch_game2.png")
sofa3img = sofa3img.resize((220,290))
sofa3img = ImageTk.PhotoImage(sofa3img)
sofa3label = Label(root, image = sofa3img).grid(column = 4,row = 2,columnspan=2)

sofa4img = Image.open("./project/img/PlayStation_game1.png")
sofa4img = sofa4img.resize((220,290))
sofa4img = ImageTk.PhotoImage(sofa4img)
sofa4label = Label(root, image = sofa4img).grid(column = 6,row = 2,columnspan=2)

#row=3
productname1 = Label(root,font = ("Inter",11), text="星之卡比 豪華版 Wili", fg = "#000000",bg = "#ECE8E7")
productname1.grid(column=0,row=3,columnspan=2 ,padx=5)

productname2 = Label(root,font = ("Inter",11), text="霍格華滋的傳承", fg = "#000000",bg = "#ECE8E7")
productname2.grid(column=2,row=3,columnspan=2,padx=5)

productname3 = Label(root,font = ("Inter",11), text="世界遊戲大全51", fg = "#000000",bg = "#ECE8E7")
productname3.grid(column=4,row=3,columnspan=2,padx=5)

productname4 = Label(root,font = ("Inter",11), text="SPIDER-MAN Miles Morales", fg = "#000000",bg = "#ECE8E7")
productname4.grid(column=6,row=3,columnspan=2,padx=5)

#row=4
product1price = Label(root,font = ("Inter",10), text="NT.0,846", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=0,row=4 ,sticky=W)

product2price = Label(root,font = ("Inter",10), text="NT.0,329", fg = "#000000",bg = "#ECE8E7")
product2price.grid(column=2,row=4 , sticky=W)

product3price = Label(root,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
product3price.grid(column=4,row=4 , sticky=W)

product4price = Label(root,font = ("Inter",10), text="NT.0,359", fg = "#000000",bg = "#ECE8E7")
product4price.grid(column=6,row=4 , sticky=W)

productnumberlabel1 = Label(root, width=10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel1.grid(column=1,row=4)

productnumberlabel2 = Label(root,width=10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel2.grid(column=3,row=4)

productnumberlabel3 = Label(root,width=10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
productnumberlabel3.grid(column=5,row=4)

productnumberlabel4 = Label(root,width=10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
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

ShoppingCart = Image.open("./project/img/Shopping Cart.png")
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

