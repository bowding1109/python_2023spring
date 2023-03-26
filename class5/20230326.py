#引入MIMEText物件
from email.mime.text import MIMEText
#如果想要在電子郵件中加入圖片，則需在Python專案中引用MIMEImage類別，並引用pathlib函式庫來讀取圖片
from email.mime.image import MIMEImage
from pathlib import Path
#引入MIMEMultipart物件
from email.mime.multipart import MIMEMultipart
#Python專案中的電子郵件內容完成後，接下來就要設定Gmmail的SMTP伺服器來寄送
import smtplib
#建立MIMEText物件
text = MIMEText("Demo-using python send emai-我是一封由Python程式碼建立的信")
#用read_bytes是為了以bytes的形式讀取圖片內容
image = MIMEImage(Path("/Users/silvia/Documents/python_2023spring/logo_tree (1).png").read_bytes())

content = MIMEMultipart()#建立 MIMEMultipart
content["subject"] = "ㄔㄐㄐ"#郵件標題
content["from"] = "bowding99@gmail.com"#寄件者
content["to"] = "lj10218@stu.kcislk.ntpc.edu.tw"#收件者
#郵件內容使用MIMEMultipart物件的attach方法(Method)進行設定
content.attach(text)#郵件內容
content.attach(image)#郵件圖片內容

#建立smtplib物件(host:伺服器位置,port:連接埠號)
smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")

#利用 with 來自動釋放資源
with open("class5/password.txt","r") as f: 
    mailToken = f.read()

with smtp: #利用with來自動釋放資源
    try:
        smtp.ehlo()#驗證SMTP伺服器
        smtp.starttls()#建立加密傳輸
        smtp.login("bowding99@gmail.com",mailToken)
        smtp.send_message(content)#寄送郵件
        print("Email is Sended completely")
        smtp.quit()
    except Exception as e:
        print("Error message: ", e)
















