from pathlib import Path
# 引進pygsheets套件
import pygsheets

import pandas as pd

import requests

# # from twilio.rest import Client

# # account_sid = 'ACb2b8e0ef4d74e8929e6f53909dec9c5c'
# # auth_token = '88b87736d4acf806bdee2f9b5b19d288'
# # client = Client(account_sid, auth_token)

# # message = client.messages.create(
# #     from_='+15075745394',
# #     body='test',
# #     to='+886903306738'
# # )

# # print(message.sid)
# ##引數傳入你要指向的位置，此例指向桌布
# p = Path("./Desktop")
# ##若沒有傳入引數，預設指向開啟Python的位置
# p = Path()
# ##resolve()絕對路徑
# print(p.resolve())




#設定 google cloud 用戶:讓 gooogle sheets 知道你的生份
gc = pygsheets.authorize(service_file=("/Users/silvia/Documents/python_2023spring/class7/dark-gateway-384601-9e775e0c520f.json"))
#連續試算表:讓 google sheets 知道要更改哪個試算表
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1qRmlfNZCPAUgVHKOCIr7TeDoov1Bw49UrzCJzlUPmTA/edit#gid=0")

#利用Index選取工作表
ws = sht[0]
#利用名字選取工作表
# ws = sht.worksheet_by_title("工作表1")

#更改表中內容
# ws.update_value("A1","test")

#讀取表中內容
# value = ws.get_value("A1")
# print("A1's value: "+ value)

# # A1 = ws.cell("A1")
# # print("A1's value: "+ A1.value)

# #刪除所有表中內容
# ws.clear()

# ws.update_value("A1","Name")
# ws.update_value("B1","Age")
# ws.update_value("B2","Age")
# ws.update_value("A2","Amy")
# ws.update_value("B2","18")
# ws.update_value("A3","Peter")
# ws.update_value("B3","15")

# #讀取表中內容並存入DataFrame，便可利用pandas套件進行表格內容操作
# df = pd.DataFrame(ws.get_all_records())
# print(df)
# #使用時機:更改內容很大量 
# ws.set_dataframe(df,"A1")


#不帶條件
# r = requests.get("https://www.google.com/")
# #有帶條件
# # payload = {"key1": "value1", "key2": "value2"}
# # r = requests.get("https://www.google.com/")

# r = requests.post("https://www.google.com/", data = {"key":"value"})

# print(r.text)#列出文字
# print(r.encoding)#列出編碼
# print(r.status_code)#列出HTTP狀態碼
# print(r.headers)#列出HTTP Response Headers
# print(r.headers["Content-Type"])#印出Header中的Content-Type
# print(r.json)#如果取得的是json格式資料，requests有內建解析函式

url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("日幣對台幣的匯率為"+str(data["rates"]["JPY"]))
