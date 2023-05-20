from tkinter import *
from tkinter import messagebox 
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.multipart import MIMEMultipart
import smtplib


#超基本設定
root = Tk()

root.title("KubeTech Shop") 
root.geometry("950x750")

account_name = ""
account_password = ""
account_email = ""


total = 0

point = 0

def detailWindow1():
    detail = Toplevel(root)
    detail.title("KubeTech Shop")
    detail.geometry("400x450")
    detail_title = Label(detail,font = ("bold",20), text="詳細介紹", fg = "#000000",bg = "#ECE8E7")
    detail_title.grid(column=0,row=0 )

    detail_word = Label(detail,font = ("Inter",18),text = "主機平台:Switch" ,fg = "#000000",bg = "#ECE8E7")
    detail_word.grid(column=0,row=1 ,padx=5,sticky = W)

    detail_word2 = Label(detail,font = ("Inter",18),text = "遊戲類型:動作" ,fg = "#000000",bg = "#ECE8E7")
    detail_word2.grid(column=0,row=2 ,padx=5,sticky = W)

    detail_word3 = Label(detail,font = ("Inter",18),text = "遊戲人數:1~4人" ,fg = "#000000",bg = "#ECE8E7")
    detail_word3.grid(column=0,row=3 ,padx=5,sticky = W)

    detail_word4 = Label(detail,font = ("Inter",18),text = "發行公司:Nintendo" ,fg = "#000000",bg = "#ECE8E7")
    detail_word4.grid(column=0,row=4 ,padx=5,sticky = W)

    detail_word5 = Label(detail,font = ("Inter",18),text = "遊戲語別:中文" ,fg = "#000000",bg = "#ECE8E7")
    detail_word5.grid(column=0,row=5 ,padx=5,sticky = W)

    detail_word6 = Label(detail,font = ("Inter",18),text = "遊戲內容:卡比為了幫助宇宙飛船上的魔法洛亞而\n展開了冒險,途中會搜集到新道具並且支持\n四人遊玩" ,fg = "#000000",bg = "#ECE8E7")
    detail_word6.grid(column=0,row=6,sticky = W)

    detail_img= Image.open("./project/img/detail1.png")
    detail_img = detail_img.resize((360,210))
    detail_img = ImageTk.PhotoImage(detail_img)
    detail_img_label = Label(detail, image = detail_img)
    detail_img_label.grid(column = 0, row= 7 ,columnspan=8,sticky=W,padx = 5)
    detail.mainloop()

def detailWindow2():
    detailB = Toplevel(root)
    detailB.title("KubeTech Shop")
    detailB.geometry("400x450")
    detail2_title = Label(detailB,font = ("bold",20), text="詳細介紹", fg = "#000000",bg = "#ECE8E7")
    detail2_title.grid(column=0,row=0 )

    detail2_word = Label(detailB,font = ("Inter",18),text = "主機平台:PlayStation4" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word.grid(column=0,row=1 ,padx=5,sticky = W)

    detail2_word2 = Label(detailB,font = ("Inter",18),text = "遊戲類型:角色扮演" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word2.grid(column=0,row=2 ,padx=5,sticky = W)

    detail2_word3 = Label(detailB,font = ("Inter",18),text = "遊戲人數:1人" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word3.grid(column=0,row=3 ,padx=5,sticky = W)

    detail2_word4 = Label(detailB,font = ("Inter",18),text = "發行公司:Warner Bros.Entertainment" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word4.grid(column=0,row=4 ,padx=5,sticky = W)

    detail2_word5 = Label(detailB,font = ("Inter",18),text = "遊戲語別:中文" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word5.grid(column=0,row=5 ,padx=5,sticky = W)

    detail2_word6 = Label(detailB,font = ("Inter",18),text = "遊戲內容:玩家將扮演到霍格華滋魔法與巫術學院\n的魔法學徒,學習基本魔法後可以自由在學院探索\n此外玩家將要培養自身魔法以及寵物來對抗敵人" ,fg = "#000000",bg = "#ECE8E7")
    detail2_word6.grid(column=0,row=6,sticky = W)

    detail2_img= Image.open("./project/img/detail2.png")
    detail2_img = detail2_img.resize((360,210))
    detail2_img = ImageTk.PhotoImage(detail2_img)
    detail2_img_label = Label(detailB, image = detail2_img)
    detail2_img_label.grid(column = 0, row= 7 ,columnspan=8,sticky=W,padx = 5)
    detailB.mainloop()




def detailWindow3():
    detailC = Toplevel(root)
    detailC.title("KubeTech Shop")
    detailC.geometry("400x450")
    detail3_title = Label(detailC,font = ("bold",20), text="詳細介紹", fg = "#000000",bg = "#ECE8E7")
    detail3_title.grid(column=0,row=0 )

    detail3_word = Label(detailC,font = ("Inter",18),text = "主機平台:Switch" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word.grid(column=0,row=1 ,padx=5,sticky = W)

    detail3_word2 = Label(detailC,font = ("Inter",18),text = "遊戲類型:益智" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word2.grid(column=0,row=2 ,padx=5,sticky = W)

    detail3_word3 = Label(detailC,font = ("Inter",18),text = "遊戲人數:4人" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word3.grid(column=0,row=3 ,padx=5,sticky = W)

    detail3_word4 = Label(detailC,font = ("Inter",18),text = "發行公司:Nitendo" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word4.grid(column=0,row=4 ,padx=5,sticky = W)

    detail3_word5 = Label(detailC,font = ("Inter",18),text = "遊戲語別:中文" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word5.grid(column=0,row=5 ,padx=5,sticky = W)

    detail3_word6 = Label(detailC,font = ("Inter",18),text = "遊戲內容:本遊戲裡面共可以玩到51種不同的懷舊\n小遊戲 而且有些小遊戲可以支持四個人一起玩" ,fg = "#000000",bg = "#ECE8E7")
    detail3_word6.grid(column=0,row=6,sticky = W)

    detail3_img= Image.open("./project/img/detail3.png")
    detail3_img = detail3_img.resize((360,210))
    detail3_img = ImageTk.PhotoImage(detail3_img)
    detail3_img_label = Label(detailC, image = detail3_img)
    detail3_img_label.grid(column = 0, row= 7 ,columnspan=8,sticky=W,padx = 5)
    detailC.mainloop()



def detailWindow4():
    detailD = Toplevel(root)
    detailD.title("KubeTech Shop")
    detailD.geometry("400x450")
    detail3_title = Label(detailD,font = ("bold",20), text="詳細介紹", fg = "#000000",bg = "#ECE8E7")
    detail3_title.grid(column=0,row=0 )

    detail4_word = Label(detailD,font = ("Inter",18),text = "主機平台:Playstation4" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word.grid(column=0,row=1 ,padx=5,sticky = W)

    detail4_word2 = Label(detailD,font = ("Inter",18),text = "遊戲類型:動作" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word2.grid(column=0,row=2 ,padx=5,sticky = W)

    detail4_word3 = Label(detailD,font = ("Inter",18),text = "遊戲人數:1人" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word3.grid(column=0,row=3 ,padx=5,sticky = W)

    detail4_word4 = Label(detailD,font = ("Inter",18),text = "發行公司:Sony Interactive" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word4.grid(column=0,row=4 ,padx=5,sticky = W)

    detail4_word5 = Label(detailD,font = ("Inter",18),text = "遊戲語別:中文" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word5.grid(column=0,row=5 ,padx=5,sticky = W)

    detail4_word6 = Label(detailD,font = ("Inter",18),text = "遊戲內容:你講扮演少年邁爾斯,你將體驗他是如何\n跟隨者他的老師成為獨當一面的蜘蛛俠" ,fg = "#000000",bg = "#ECE8E7")
    detail4_word6.grid(column=0,row=6,sticky = W)

    detail4_img= Image.open("./project/img/detail4.png")
    detail4_img = detail4_img.resize((360,210))
    detail4_img = ImageTk.PhotoImage(detail4_img)
    detail4_img_label = Label(detailD, image = detail4_img)
    detail4_img_label.grid(column = 0, row= 7 ,columnspan=8,sticky=W,padx = 5)
    
    detailD.mainloop()


#加減功能
def add(numlabel,pricelabel):
    global total
    numlabel["text"] = int(numlabel["text"])+1
    price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
    total = int(totalval.get().split(":")[1].replace("元","").strip())
    totalval.set("共消費: "+str(total+price)+" 元")
def minus(numlabel,pricelabel):
    global total
    if int(numlabel["text"])>0:
        numlabel["text"] = int(numlabel["text"])-1
        price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
        total = int(totalval.get().split(":")[1].replace("元","").strip())
        totalval.set("共消費: "+str(total-price)+" 元")
    else:
        messagebox.showwarning("showarnng","The number of products can\'t be below 0.")






#詳細清單
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







def signUP(password, account_namePass,account_emailPass,account_passwordPass):
    global account_name
    global account_password
    global account_email
    if password == "12345":
        messagebox.showwarning("showwarning","已註冊成功，可以關閉視窗盡情享受購物體驗")
        account_name = account_namePass
        account_email = account_emailPass
        account_password = account_passwordPass
        print(account_name,account_email,account_password)
    else:
        messagebox.showwarning("showwarning","驗證碼不正確!")

def logIN(account,password2):
    global account_name
    global account_password
    if account == account_name:
        if password2 == password2:
            messagebox.showwarning("showwarning","成功")
            print(account,account_name,password2,password2)
        else:
            messagebox.showwarning("showwarning","密碼錯了")
    else:
        messagebox.showwarning("showwarning","帳號錯了")

#註冊會員
def register_page():
    global account_name
    global account_password
    global account_email
    C1 = Toplevel(root)
    C1.title("KubeTech Shop1")
    C1.geometry("450x350")
    #row 0
    space= Frame(C1, width=260, height= 50)
    space.grid(column=0,row=0)
    login_title = Label(C1,font = ("bold",30), text="歡迎註冊", fg = "#000000",bg = "#ECE8E7")
    login_title.grid(column=0,row=0 ,padx=5,sticky = E)
    #row 1
    login_name = Label(C1,font = ("Inter",20), text="請輸入您的帳號名字", fg = "#000000",bg = "#ECE8E7")
    login_name.grid(column=0,row=1,sticky = W)
    #row 2
    login_nameBox = Entry(C1 ,width=30)
    login_nameBox.grid(column=0,row = 2 )
    #row3
    login_secrict = Label(C1,font = ("Inter",20), text="請輸入您的帳號密碼", fg = "#000000",bg = "#ECE8E7")
    login_secrict.grid(column=0,row=3,sticky = W)
    #row4
    login_passwordBox = Entry(C1 ,width=30)
    login_passwordBox.grid(column=0,row = 4 )
    #row5
    login_gmail = Label(C1,font = ("Inter",20), text="請輸入您的Gmail", fg = "#000000",bg = "#ECE8E7")
    login_gmail.grid(column=0,row=5,sticky = W)
    #row6
    login_gmailBox = Entry(C1 ,width=30)
    login_gmailBox.grid(column=0,row = 6 )
    #row7
    login_gmailpassword = Label(C1,font = ("Inter",20), text="請輸入您的Gmail驗證碼", fg = "#000000",bg = "#ECE8E7")
    login_gmailpassword.grid(column=0,row=7,sticky = W)
    #row8
    login_gmailpasswordBox = Entry(C1 ,width=30)
    login_gmailpasswordBox.grid(column=0,row = 8 )

    login_gmailpassword_button = Button(C1,font = ("bold",20), text="發送註冊號", fg = "#1E1E1E",bg = "#E7E2E2", width = 7,pady=2,command = lambda:gmailtest(account_name = login_nameBox.get(),account_password = login_passwordBox.get(),account_email = login_gmailBox.get()))
    login_gmailpassword_button.grid(column=1,row=8,padx=5,sticky =E)

    login_button = Button(C1,font = ("bold",25), text="註冊", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2, command =lambda:signUP(login_gmailpasswordBox.get(),login_nameBox.get(),login_gmailpasswordBox.get(),login_passwordBox.get()))
    login_button.grid(column=0,row=9,padx=5,sticky =E)
    

    C1.mainloop()




#會員登入
def login_page():

    D1 = Toplevel(root)
    D1.title("KubeTech Shop1")
    D1.geometry("450x350")
    #row 0
    space= Frame(D1, width=260, height= 50)
    space.grid(column=0,row=0)
    login_title = Label(D1,font = ("bold",30), text="歡迎登入", fg = "#000000",bg = "#ECE8E7")
    login_title.grid(column=0,row=0 ,padx=5,sticky = E)
    #row 1
    login_name = Label(D1,font = ("Inter",20), text="請輸入您的帳號名字", fg = "#000000",bg = "#ECE8E7")
    login_name.grid(column=0,row=1,sticky = W)
    #row 2
    login_nameBox = Entry(D1 ,width=30)
    login_nameBox.grid(column=0,row = 2 )
    #row3
    login_secrict = Label(D1,font = ("Inter",20), text="請輸入您的帳號密碼", fg = "#000000",bg = "#ECE8E7")
    login_secrict.grid(column=0,row=3,sticky = W)
    #row4
    login_passwordBox = Entry(D1 ,width=30)
    login_passwordBox.grid(column=0,row = 4 )
    #row5
    login_button = Button(D1,font = ("bold",25), text="登入", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,command =lambda:logIN(login_nameBox.get(),login_passwordBox.get()))
    login_button.grid(column=0,row=5,padx=5,sticky =E)
    D1.mainloop()



#信用卡付費
def cashcard(member):
    global point
    point = int(totalval.get().split(":")[1].replace("元","").strip())*0.1
    if member == '普通':
        tempContent = "親愛的顧客 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是使用信用卡付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '白銀(每年5000元)':
        tempContent = "親愛的白金會員 您好\n這裡是kubshop:\n 感謝您光臨本店進行購物,這是你剛消費的金額,總價打九五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.95)+"\n請確認您此次消費是使用信用卡付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '黃金(每年10000元)':
        tempContent = "親愛的黃金會員 您好\n這裡是kubshop:\n 感謝您光臨本店進行購物,這是你剛消費的金額,總價打九折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.9)+"\n請確認您此次消費是使用信用卡付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '鑽石(每年30000元)':
        tempContent = "親愛的鑽石會員 您好\n這裡是kubshop:\n 感謝您光臨本店進行購物,這是你剛消費的金額,總價打八五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.85)+"\n請確認您此次消費是使用信用卡付款\nkubshop期待您下次的光臨 love you 3000"
    text = MIMEText(tempContent)

    content = MIMEMultipart()#
    content["subject"] = "kubshop 通知"
    content["from"] = "bowding99@gmail.com"
    print(account_email)
    content["to"] = "bowding99@gmail.com"

    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")


    with open("class5/password.txt","r") as f: 
        mailToken = f.read()

    with smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("bowding99@gmail.com",mailToken)
            smtp.send_message(content)
            print("Email is Sended completely")
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)





#貨到付款
def place(member):
    global point
    point = int(totalval.get().split(":")[1].replace("元","").strip())*0.1
    if member == '普通':
        tempContent = "親愛的顧客 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是貨到付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '白銀(每年5000元)':
        tempContent = "親愛的白金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打九五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.95)+"\n請確認您此次消費是貨到付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '黃金(每年10000元)':
        tempContent = "親愛的黃金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打九折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.9)+"\n請確認您此次消費是貨到付款\nkubshop期待您下次的光臨 love you 3000"
    elif member == '鑽石(每年30000元)':
        tempContent = "親愛的鑽石會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打八五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.85)+"\n請確認您此次消費是貨到付款\nkubshop期待您下次的光臨 love you 3000"

    text = MIMEText(tempContent)

    content = MIMEMultipart()#
    content["subject"] = "kubshop 通知"
    content["from"] = "bowding99@gmail.com"
    print(account_email)
    content["to"] = "bowding99@gmail.com"

    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")


    with open("class5/password.txt","r") as f: 
        mailToken = f.read()

    with smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("bowding99@gmail.com",mailToken)
            smtp.send_message(content)
            print("Email is Sended completely")
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)






#銀行付款
def bank(member):
    global point
    point = int(totalval.get().split(":")[1].replace("元","").strip())*0.1
    if member == '普通':
        tempContent = "親愛的顧客 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是利用銀行轉帳\nkubshop期待您下次的光臨 love you 3000"
    elif member == '白銀(每年5000元)':
        tempContent = "親愛的白金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打九五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.95)+"\n請確認您此次消費是利用銀行轉帳\nkubshop期待您下次的光臨 love you 3000"
    elif member == '黃金(每年10000元)':
        tempContent = "親愛的黃金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打九折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.9)+"\n請確認您此次消費是利用銀行轉帳\nkubshop期待您下次的光臨 love you 3000"
    elif member == "鑽石(每年30000元)":
        tempContent = "親愛的鑽石會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是你剛消費的金額,總價打八五折"+str(int(totalval.get().split(":")[1].replace("元","").strip())*0.85)+"\n請確認您此次消費是利用銀行轉帳\nkubshop期待您下次的光臨 love you 3000"
    text = MIMEText(tempContent)

    content = MIMEMultipart()#
    content["subject"] = "kubshop 通知"
    content["from"] = "bowding99@gmail.com"
    print(account_email)
    content["to"] = "bowding99@gmail.com"

    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")


    with open("class5/password.txt","r") as f: 
        mailToken = f.read()

    with smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("bowding99@gmail.com",mailToken)
            smtp.send_message(content)
            print("Email is Sended completely")
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)


def point_1(member):
    global point
    point = int(point) - int(totalval.get().split(":")[1].replace("元","").strip())
    if member == '普通':
        tempContent = "親愛的顧客 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是您剛消費的金額(由於此次利用點數消費故此筆消費不適用會員折扣及累積消費點數)"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是利用點數折抵\nkubshop期待您下次的光臨 love you 3000"
    elif member == '白銀(每年5000元)':
        tempContent = "親愛的白金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是您剛消費的金額(由於此次利用點數消費故此筆消費不適用會員折扣及累積消費點數)"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是利用點數折抵\nkubshop期待您下次的光臨 love you 3000"
    elif member == '黃金(每年10000元)':
        tempContent = "親愛的黃金會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是您剛消費的金額(由於此次利用點數消費故此筆消費不適用會員折扣及累積消費點數)"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是利用點數折抵\nkubshop期待您下次的光臨 love you 3000"
    elif member == "鑽石(每年30000元)":
        tempContent = "親愛的鑽石會員 您好\n這裡是kubshop:\n感謝您光臨本店進行購物,這是您剛消費的金額(由於此次利用點數消費故此筆消費不適用會員折扣及累積消費點數)"+str(int(totalval.get().split(":")[1].replace("元","").strip()))+"\n請確認您此次消費是利用點數折抵\nkubshop期待您下次的光臨 love you 3000"
    text = MIMEText(tempContent)

    content = MIMEMultipart()#
    content["subject"] = "kubshop 通知"
    content["from"] = "bowding99@gmail.com"
    print(account_email)
    content["to"] = "bowding99@gmail.com"

    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")


    with open("class5/password.txt","r") as f: 
        mailToken = f.read()

    with smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("bowding99@gmail.com",mailToken)
            smtp.send_message(content)
            print("Email is Sended completely")
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)














def gmailtest(account_name,account_password,account_email):

    text = MIMEText("您的註冊號是12345")

    content = MIMEMultipart()#
    content["subject"] = "由 kube shop 發來的驗證碼"
    content["from"] = "bowding99@gmail.com"
    print(account_email)
    content["to"] = account_email

    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")


    with open("class5/password.txt","r") as f: 
        mailToken = f.read()

    with smtp: 
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login("bowding99@gmail.com",mailToken)
            smtp.send_message(content)
            print("Email is Sended completely")
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)



def checkout():
    global point
    E1 = Toplevel(root)
    E1.title("KubeTech Shop1")
    E1.geometry("350x350")
# 會員功能
    listbox = Listbox(E1,selectmode="extended")
    listbox.insert(1,"普通")
    listbox.insert(2,"白銀(每年5000元)")
    listbox.insert(3,"黃金(每年10000元)")
    listbox.insert(4,"鑽石(每年30000元)")
    listbox.grid(column=0,row=0)
    point_view = Label(E1,font = ("bold",18), text = "您的點數:"+str(point),fg = "#000000",bg = "#ECE8E7")
    point_view.grid(column=1,row=0)
#row0
    checkout_label = Label(E1,font = ("bold",20), text="請選擇付款方式", fg = "#000000",bg = "#ECE8E7")
    checkout_label.grid(column=0,row=1)
    
#row1
    cashcard_button = Button(E1,font = ("Inter",18), text="信用卡付費", fg = "#1E1E1E",bg = "#ECE8E7",command = lambda:cashcard(listbox.get(listbox.curselection())))
    cashcard_button.grid(column=0,row=2,padx=5)
#row2
    place_button = Button(E1,font = ("Inter",18), text="貨到付款", fg = "#1E1E1E",bg = "#ECE8E7",command = lambda:place(listbox.get(listbox.curselection())))
    place_button.grid(column=0,row=3,padx=5)
#row3
    bank_button = Button(E1,font = ("Inter",18), text="銀行轉帳", fg = "#1E1E1E",bg = "#ECE8E7",command = lambda:bank(listbox.get(listbox.curselection())))
    bank_button.grid(column=0,row=4,padx=5)

    point_button = Button(E1,font = ("Inter",18), text="點數折抵", fg = "#1E1E1E",bg = "#ECE8E7",command = lambda:point_1(listbox.get(listbox.curselection())))
    point_button.grid(column=0,row=5,padx=5)
    E1.mainloop()














#任天堂頁面

#基本設定
def nitendo():
    A1 = Toplevel(root)
    A1.title("KubeTech Shop1")
    A1.geometry("950x750")

    #row 0
    nitendo_titleimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
    nitendo_titleimg = nitendo_titleimg.resize((32,32))
    nitendo_titleimg = ImageTk.PhotoImage(nitendo_titleimg)
    nitendo_titleimg = Label(A1, image = nitendo_titleimg,width = 32,height = 32)
    nitendo_titleimg.grid(column = 0,row = 0,sticky=W)

    nitendo_topic1_button = Button(A1,font = ("Inter",18), text="熱門遊戲", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2)
    nitendo_topic1_button.grid(column=1,row=0,sticky = E+W,padx=5)

    nitendo_topic2_button = Button(A1,font = ("Inter",18), text="折價區", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2)
    nitendo_topic2_button.grid(column=2,row=0,sticky = E+W,padx=5)

    nitendo_topic3_button = Button(A1,font = ("Inter",18), text="周邊商品", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
    nitendo_topic3_button.grid(column=3,row=0,sticky = E+W,padx=5)


    #row=1
    nitendo_topic_img= Image.open("./project/img/topic2.png")
    nitendo_topic_img = nitendo_topic_img.resize((900,298))
    nitendo_topic_img = ImageTk.PhotoImage(nitendo_topic_img)
    nitendo_topic_label = Label(A1, image = nitendo_topic_img)
    nitendo_topic_label.grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

    #row=2
    nitendo_game1_img= Image.open("./project/img/switch_game4.png")
    nitendo_game1_img = nitendo_game1_img.resize((220,290))
    nitendo_game1_img = ImageTk.PhotoImage(nitendo_game1_img)
    nitendo_game1_label = Label(A1, image = nitendo_game1_img).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

    nitendo_game2_img = Image.open("./project/img/switch_game5.png")
    nitendo_game2_img = nitendo_game2_img.resize((220,290))
    nitendo_game2_img = ImageTk.PhotoImage(nitendo_game2_img)
    nitendo_game2_label = Label(A1, image = nitendo_game2_img).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

    nitendo_game3_img = Image.open("./project/img/switch_game6.png")
    nitendo_game3_img = nitendo_game3_img.resize((220,290))
    nitendo_game3_img = ImageTk.PhotoImage(nitendo_game3_img)
    nitendo_game3_label = Label(A1, image = nitendo_game3_img).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

    nitendo_game4_img = Image.open("./project/img/switch_game7.png")
    nitendo_game4_img = nitendo_game4_img.resize((220,290))
    nitendo_game4_img = ImageTk.PhotoImage(nitendo_game4_img)
    nitendo_game4_label = Label(A1, image = nitendo_game4_img).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

    #row=3
    nitendo_game1_name1 = Label(A1,font = ("Inter",11), text="馬力歐賽車8 豪華版", fg = "#000000",bg = "#ECE8E7")
    nitendo_game1_name1.grid(column=0,row=3,columnspan=2 ,padx=5)

    nitendo_game2_name2 = Label(A1,font = ("Inter",11), text="瑪利歐高爾夫 超級衝衝", fg = "#000000",bg = "#ECE8E7")
    nitendo_game2_name2.grid(column=2,row=3,columnspan=2,padx=5)

    nitendo_game3_name3 = Label(A1,font = ("Inter",11), text="瑪利歐兄弟U 豪華版", fg = "#000000",bg = "#ECE8E7")
    nitendo_game3_name3.grid(column=4,row=3,columnspan=2,padx=5)

    nitendo_game4_name4 = Label(A1,font = ("Inter",11), text="寶可夢 朱", fg = "#000000",bg = "#ECE8E7")
    nitendo_game4_name4.grid(column=6,row=3,columnspan=2,padx=5)

    #row=4
    nitendo_game1_price1 = Label(A1,font = ("Inter",10), text="NT.1,346", fg = "#000000",bg = "#ECE8E7")
    nitendo_game1_price1.grid(column=0,row=4 ,padx=5,sticky=W)

    nitendo_game2_price2 = Label(A1,font = ("Inter",10), text="NT.1,229", fg = "#000000",bg = "#ECE8E7")
    nitendo_game2_price2.grid(column=2,row=4 ,padx=5, sticky=W)

    nitendo_game3_price3 = Label(A1,font = ("Inter",10), text="NT.1,085", fg = "#000000",bg = "#ECE8E7")
    nitendo_game3_price3.grid(column=4,row=4 ,padx=5, sticky=W)

    nitendo_game4_price4 = Label(A1,font = ("Inter",10), text="NT.1,159", fg = "#000000",bg = "#ECE8E7")
    nitendo_game4_price4.grid(column=6,row=4 ,padx=5, sticky=W)

    nitendo_game1_number1 = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    nitendo_game1_number1.grid(column=1,row=4)

    nitendo_game2_number2 = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    nitendo_game2_number2.grid(column=3,row=4)

    nitendo_game3_number3 = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    nitendo_game3_number3.grid(column=5,row=4)

    nitendo_game4_number4 = Label(A1,width = 10,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    nitendo_game4_number4.grid(column=7,row=4)

    nitendo_game1_addbutton1 = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(nitendo_game1_number1,nitendo_game1_price1))
    nitendo_game1_addbutton1.grid(column=1,row=4 ,sticky=E)

    nitendo_game2_addbutton2 = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(nitendo_game2_number2,nitendo_game2_price2))
    nitendo_game2_addbutton2.grid(column=3,row=4 ,sticky=E)

    nitendo_game3_addbutton3 = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add( nitendo_game3_number3,nitendo_game3_price3))
    nitendo_game3_addbutton3.grid(column=5,row=4 ,sticky=E)

    nitendo_game4_addbutton4 = Button(A1,font = ("Inter",10), text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(nitendo_game4_number4,nitendo_game4_price4))
    nitendo_game4_addbutton4.grid(column=7,row=4 ,sticky=E)

    nitendo_game1_minusbutton1 = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(nitendo_game1_number1,nitendo_game1_price1))
    nitendo_game1_minusbutton1.grid(column=1,row=4 ,sticky=W)

    nitendo_game2_minusbutton2 = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(nitendo_game2_number2,nitendo_game2_price2))
    nitendo_game2_minusbutton2.grid(column=3,row=4 ,sticky=W)

    nitendo_game3_minusbutton3 = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(nitendo_game3_number3,nitendo_game3_price3))
    nitendo_game3_minusbutton3.grid(column=5,row=4 ,sticky=W)

    nitendo_game4_minusbutton4 = Button(A1,font = ("Inter",10), text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(nitendo_game4_number4,nitendo_game4_name4))
    nitendo_game4_minusbutton4.grid(column=7,row=4 ,sticky=W)


    ShoppingCartA = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/Shopping Cart.png")
    ShoppingCartA = ShoppingCartA.resize((30,30))
    ShoppingCartA = ImageTk.PhotoImage(ShoppingCartA)
    CartlabelA = Label(A1, image = ShoppingCartA,width = 30,height = 30)
    CartlabelA.grid(column = 5,row = 5,sticky=E+S)

    totalvalA = StringVar()
    totalvalA.set("共消費:0元")
    totallabelA = Label(A1,textvariable=totalval,font=("Inter",18),fg="#000000")
    totallabelA.grid(row = 5, column= 6,columnspan= 2, sticky = W+S)

    checkoutbuttonA = Button(A1,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2",command = checkout)
    checkoutbuttonA.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )
    A1.mainloop()














    #PlatStation頁面

#基本設定
def playstation():
    B2 = Toplevel(root)
    B2.title("KubeTech Shop2")
    B2.geometry("950x750")

    #row 0
    playstation_titleimg = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/logo_tree.png")
    playstation_titleimg = playstation_titleimg.resize((32,32))
    playstation_titleimg = ImageTk.PhotoImage(playstation_titleimg)
    playstation_titleimg = Label(B2, image = playstation_titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

    playstation_topic1_button1 = Button(B2,font = ("Inter",18), text="熱門遊戲", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2)
    playstation_topic1_button1.grid(column=2,row=0,sticky = E+W,padx=5)

    playstation_topic2_button2 = Button(B2,font = ("Inter",18), text="折價區", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2)
    playstation_topic2_button2.grid(column=1,row=0,sticky = E+W,padx=5)

    playstation_topic3_button3 = Button(B2,font = ("Inter",18), text="周邊商品", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,)
    playstation_topic3_button3.grid(column=3,row=0,sticky = E+W,padx=5)


    #row=1
    playstation_topic_img = Image.open("./project/img/topic3.png")
    playstation_topic_img= playstation_topic_img.resize((900,298))
    playstation_topic_img = ImageTk.PhotoImage(playstation_topic_img)
    playstation_topic_lable = Label(B2, image = playstation_topic_img).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

    #row=2
    playstation_game1_img = Image.open("./project/img/PlayStation_game7.png")
    playstation_game1_img =  playstation_game1_img.resize((220,290))
    playstation_game1_img = ImageTk.PhotoImage( playstation_game1_img)
    playstation_game1_lable = Label(B2, image =  playstation_game1_img).grid(column = 0,row = 2,columnspan=2,sticky=W,padx = 5)

    playstation_game2_img = Image.open("./project/img/PlayStation_game4.png")
    playstation_game2_img = playstation_game2_img.resize((220,290))
    playstation_game2_img = ImageTk.PhotoImage(playstation_game2_img)
    playstation_game2_lable = Label(B2, image = playstation_game2_img).grid(column = 2,row = 2,columnspan=2,sticky=W,padx = 5)

    playstation_game3_img = Image.open("./project/img/PlayStation_game5.png")
    playstation_game3_img = playstation_game3_img.resize((220,290))
    playstation_game3_img = ImageTk.PhotoImage(playstation_game3_img)
    playstation_game3_lable = Label(B2, image = playstation_game3_img).grid(column = 4,row = 2,columnspan=2,sticky=W,padx = 5)

    playstation_game4_img = Image.open("./project/img/PlayStation_game6.png")
    playstation_game4_img = playstation_game4_img.resize((220,290))
    playstation_game4_img = ImageTk.PhotoImage(playstation_game4_img)
    playstation_game4_lable = Label(B2, image = playstation_game4_img).grid(column = 6,row = 2,columnspan=2,sticky=W,padx = 5)

    #row=3
    playstation_game1_name1 = Label(B2,font = ("Inter",11), text="Cyberpunk 2077", fg = "#000000",bg = "#ECE8E7")
    playstation_game1_name1.grid(column=0,row=3,columnspan=2)

    playstation_game2_name2 = Label(B2,font = ("Inter",11), text="鬼滅之刃 火之神血風譚", fg = "#000000",bg = "#ECE8E7")
    playstation_game2_name2.grid(column=2,row=3,columnspan=2)

    playstation_game3_name3 = Label(B2,font = ("Inter",11), text="俠盜獵車手Ｖ", fg = "#000000",bg = "#ECE8E7")
    playstation_game3_name3.grid(column=4,row=3,columnspan=2)

    playstation_game4_name4 = Label(B2,font = ("Inter",11), text="Final Fantasy xvi", fg = "#000000",bg = "#ECE8E7")
    playstation_game4_name4.grid(column=6,row=3,columnspan=2)

    #row=4
    playstation_game1_price1 = Label(B2,font = ("Inter",10), text="NT.1,346", fg = "#000000",bg = "#ECE8E7")
    playstation_game1_price1.grid(column=0,row=4 ,padx=5,sticky=W)

    playstation_game2_price2 = Label(B2,font = ("Inter",10), text="NT.1,029", fg = "#000000",bg = "#ECE8E7")
    playstation_game2_price2.grid(column=2,row=4 ,padx=5, sticky=W)

    playstation_game3_price3 = Label(B2,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
    playstation_game3_price3.grid(column=4,row=4 ,padx=5, sticky=W)

    playstation_game4_price4 = Label(B2,font = ("Inter",10), text="NT.1,159", fg = "#000000",bg = "#ECE8E7")
    playstation_game4_price4.grid(column=6,row=4 ,padx=5, sticky=W)

    playstation_game1_number1 = Label(B2,width = 3 ,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    playstation_game1_number1.grid(column=1,row=4)

    playstation_game2_number2 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    playstation_game2_number2.grid(column=3,row=4)

    playstation_game3_number3 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    playstation_game3_number3.grid(column=5,row=4)

    playstation_game4_number4 = Label(B2,width = 3,font = ("Inter",12), text="0", fg = "#000000",bg = "#ECE8E7")
    playstation_game4_number4.grid(column=7,row=4)

    playstation_game1_addbutton1 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(playstation_game1_number1,playstation_game1_price1))
    playstation_game1_addbutton1.grid(column=1,row=4 ,sticky=E)

    playstation_game2_addbutton2 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(playstation_game2_number2,playstation_game2_price2))
    playstation_game2_addbutton2.grid(column=3,row=4 ,sticky=E)

    playstation_game3_addbutton3 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(playstation_game3_number3,playstation_game3_price3))
    playstation_game3_addbutton3.grid(column=5,row=4 ,sticky=E)

    playstation_game4_addbutton4 = Button(B2,font = ("Inter",10),width = 2, text="+", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda: add(playstation_game4_number4,playstation_game4_price4))
    playstation_game4_addbutton4.grid(column=7,row=4 ,sticky=E)

    playstation_game1_minusbutton1 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(playstation_game1_number1,playstation_game1_price1))
    playstation_game1_minusbutton1.grid(column=1,row=4 ,sticky=W)

    playstation_game2_minusbutton2 = Button(root,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(playstation_game2_number2,playstation_game2_price2))
    playstation_game2_minusbutton2.grid(column=3,row=4 ,sticky=W)

    playstation_game3_minusbutton3 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(playstation_game3_number3,playstation_game3_price3))
    playstation_game3_minusbutton3.grid(column=5,row=4 ,sticky=W)

    playstation_game4_minusbutton4 = Button(B2,font = ("Inter",10),width = 2, text="-", fg = "#1E1E1E",bg = "#E7E2E2",command = lambda:minus(playstation_game4_number4,playstation_game4_price4))
    playstation_game4_minusbutton4.grid(column=7,row=4 ,sticky=W)


    ShoppingCart2 = Image.open("/Users/silvia/Documents/Python_2022Autumn/class10/image/Shopping Cart.png")
    ShoppingCart2 = ShoppingCart2.resize((30,30))
    ShoppingCart2 = ImageTk.PhotoImage(ShoppingCart2)
    Cartlabel2 = Label(B2, image = ShoppingCart2,width = 30,height = 30)
    Cartlabel2.grid(column = 5,row = 5,sticky=E+S)

    totalval2 = StringVar()
    totalval2.set("共消費:0元")
    totallabel2 = Label(B2,textvariable=totalval,font=("Inter",18),fg="#000000")
    totallabel2.grid(row = 5, column= 6,columnspan= 2, sticky = W+S)

    checkoutbutton2 = Button(B2,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2",command = checkout)
    checkoutbutton2.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )
    B2.mainloop()
























#主頁面

#基本設定for title




#row 0
titleimg = Image.open("project/img/logo_tree.png")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image = titleimg,width = 32,height = 32).grid(column = 0,row = 0,sticky=W)

mainpage_topicbutton1 = Button(root,font = ("Inter",18), text="PlayStayion", fg = "#1E1E1E",bg = "#ECE8E7", width = 5,pady=2,command = playstation)
mainpage_topicbutton1.grid(column=2,row=0,sticky = E+W,padx=5)

mainpage_topicbutton2 = Button(root,font = ("Inter",18), text="任天堂Nintendo", fg = "#1E1E1E",bg = "#ECE8E7", width = 10,pady=2,command= nitendo)
mainpage_topicbutton2.grid(column=1,row=0,sticky = E+W,padx=5)

mainpage_loginbutton = Button(root,font = ("Inter",18), text="會員登入", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,command= login_page)
mainpage_loginbutton.grid(column=5,row=0,sticky = E+W,padx=5)

mainpage_loginbutton2 = Button(root,font = ("Inter",18), text="會員註冊", fg = "#1E1E1E",bg = "#ECE8E7",padx=5,command= register_page)
mainpage_loginbutton2.grid(column=6,row=0,sticky = E+W,padx=5)

mainpage_loginbutton3 = Button(root,font = ("Inter",18), text="會員資料", fg = "#1E1E1E",bg = "#ECE8E7",padx=5)
mainpage_loginbutton3.grid(column=7,row=0,sticky = E+W,padx=5)

#row=1
bannerimg = Image.open("./project/img/topic.png")
bannerimg = bannerimg.resize((900,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image = bannerimg).grid(column = 0, row= 1,columnspan=8,sticky=W,padx = 5)

#row=2
sofa1img = Image.open("./project/img/switch_game1.png")
sofa1img = sofa1img.resize((220,290))
sofa1img = ImageTk.PhotoImage(sofa1img)
sofa1label = Button(root, image = sofa1img, command= detailWindow1)
sofa1label.grid(column = 0,row = 2,columnspan=2)


sofa2img = Image.open("./project/img/PlayStation_game2.png")
sofa2img = sofa2img.resize((220,290))
sofa2img = ImageTk.PhotoImage(sofa2img)
sofa2label = Button(root, image = sofa2img,command = detailWindow2)
sofa2label.grid(column = 2,row = 2,columnspan=2)

sofa3img = Image.open("./project/img/switch_game2.png")
sofa3img = sofa3img.resize((220,290))
sofa3img = ImageTk.PhotoImage(sofa3img)
sofa3label = Button(root, image = sofa3img, command= detailWindow3)
sofa3label.grid(column = 4,row = 2,columnspan=2)

sofa4img = Image.open("./project/img/PlayStation_game1.png")
sofa4img = sofa4img.resize((220,290))
sofa4img = ImageTk.PhotoImage(sofa4img)
sofa4label = Button(root, image = sofa4img,command = detailWindow4)
sofa4label.grid(column = 6,row = 2,columnspan=2)

#row=3
productname1 = Label(root,font = ("Inter",11),text="星之卡比 豪華版 Wii", fg = "#000000",bg = "#ECE8E7")
productname1.grid(column=0,row=3,columnspan=2 ,padx=5)

productname2 = Label(root,font = ("Inter",11), text="霍格華滋的傳承", fg = "#000000",bg = "#ECE8E7")
productname2.grid(column=2,row=3,columnspan=2,padx=5)

productname3 = Label(root,font = ("Inter",11), text="世界遊戲大全51", fg = "#000000",bg = "#ECE8E7")
productname3.grid(column=4,row=3,columnspan=2,padx=5)

productname4 = Label(root,font = ("Inter",11), text="SPIDER-MAN Miles Morales", fg = "#000000",bg = "#ECE8E7")
productname4.grid(column=6,row=3,columnspan=2,padx=5)

#row=4
product1price = Label(root,font = ("Inter",10), text="NT.1,246", fg = "#000000",bg = "#ECE8E7")
product1price.grid(column=0,row=4 ,sticky=W)

product2price = Label(root,font = ("Inter",10), text="NT.1,129", fg = "#000000",bg = "#ECE8E7")
product2price.grid(column=2,row=4 , sticky=W)

product3price = Label(root,font = ("Inter",10), text="NT.0,985", fg = "#000000",bg = "#ECE8E7")
product3price.grid(column=4,row=4 , sticky=W)

product4price = Label(root,font = ("Inter",10), text="NT.1,229", fg = "#000000",bg = "#ECE8E7")
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

checkoutbutton = Button(root,font = ("Inter",10), text="結帳", fg = "#1E1E1E",bg = "#E7E2E2",command = checkout)
checkoutbutton.grid(row=5, column = 7, sticky = E+S, padx = 5, pady =1 )

root.mainloop()






















