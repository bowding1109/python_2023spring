from pathlib import Path

# from twilio.rest import Client

# account_sid = 'ACb2b8e0ef4d74e8929e6f53909dec9c5c'
# auth_token = '88b87736d4acf806bdee2f9b5b19d288'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_='+15075745394',
#     body='test',
#     to='+886903306738'
# )

# print(message.sid)
##引數傳入你要指向的位置，此例指向桌布
p = Path("./Desktop")
##若沒有傳入引數，預設指向開啟Python的位置
p = Path()
##resolve()絕對路徑
print(p.resolve())