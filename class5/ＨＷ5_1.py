from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.multipart import MIMEMultipart
import smtplib

text = MIMEText("2023 春季班 簡愷宸")

image = MIMEImage(Path("/Users/silvia/Documents/python_2023spring/A20484E7-04AB-4D28-9907-A5BF8F06E305.jpeg").read_bytes())

content = MIMEMultipart()
content["subject"] = "我是簡愷宸 是個學生"
content["from"] = "bowding99@gmail.com"
content["to"] = "kubetech.academy0524@gmail.com"

content.attach(text)
content.attach(image)


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