import requests
import pytz
from datetime import datetime
from time import gmtime, strftime
from pytz import all_timezones
print(all_timezones)
DEM_TIN = 0
btc = ""
numer = open("stt.txt","r")
a = numer.read()
DEM_TIN = int(a)
DEM_TIN_CU = DEM_TIN
while True:
    now = datetime.now(pytz.timezone('Asia/Saigon'))
    current_time = now.strftime("%m/%d/%Y, %H:%M")
    payload = {
        'content': current_time
    }
    header = {
        "authorization": "ODg0MDUzODM4MjM4MjE2MjM1.GwbwK7.v4l9pHYd8uvsZxIpi1wKE1hY8CLvruEwZ4414M"
    }
    if btc != current_time:
        requests.post("https://discord.com/api/v9/channels/1154788744143056986/messages",json=payload,headers=header)
        btc = current_time
        print(current_time)
        DEM_TIN = DEM_TIN + 1
        print(DEM_TIN)
        if (DEM_TIN % 50)==0:
            payloadss = {
                'content': f"Tin Nhắn Thứ: **{DEM_TIN}** "
            }
            requests.post("https://discord.com/api/v9/channels/1154788744143056986/messages",json=payloadss,headers=header)
    if DEM_TIN != DEM_TIN_CU:
        with open("stt.txt", "w") as file:
            file.write(str(DEM_TIN))  # Ghi nội dung trống vào tệp
        DEM_TIN_CU = DEM_TIN


