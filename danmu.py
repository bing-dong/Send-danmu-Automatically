# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome()
# driver.get('https://live.bilibili.com/2233')

# while(1):
#     try:
#         driver.find_element_by_class_name('top-nav-btn dp-i-block v-top pointer border-box').click()
#         break
#     except Exception:
#         pass

# text = driver.find_element_by_class_name('chat-input border-box')

import requests
import time
import random

url = "https://api.live.bilibili.com/msg/send"
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Content-Length": "160",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_uuid=1C6EE4E5-F284-F67D-E08E-7D9C82DE88FD32619infoc; buvid3=A7A5456E-AE55-4A8B-88AF-A6DF021BD37953917infoc; sid=bk3g6lop; DedeUserID=94720529; DedeUserID__ckMd5=e53dd44b4c47c62d; SESSDATA=1f954f39%2C1583923959%2C1ddfa721; bili_jct=d3fbdd978b4a4832e09cbf16f54737c8; LIVE_BUVID=AUTO7615813347532453; CURRENT_FNVAL=16; rpdid=|(u~~)l~YkRm0J'ul)uJJlJm~; LIVE_PLAYER_TYPE=2; INTVER=1; stardustpgcv=0606; CURRENT_QUALITY=80; bp_t_offset_94720529=354973923126390377; _dfcaptcha=b2aaf41c54ac172d599f51c4e443b994",
    "Host": "api.live.bilibili.com",
    "Origin": "https://live.bilibili.com",
    "Pragma": "no-cache",
    "Referer": "https://live.bilibili.com/2233",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36"
}
data = {
    "color": "16777215",
    "fontsize": "25",
    "mode": "1",
    "msg": "休想打败我的生活",
    "rnd": "1581491233",
    "roomid": "544641",
    # "roomid": "13488594",
    "bubble": "0",
    "csrf_token": "d3fbdd978b4a4832e09cbf16f54737c8",
    "csrf": "d3fbdd978b4a4832e09cbf16f54737c8"
}

cnt = 0       
while 1:
    # 延时发送
    sec = random.uniform(4,13)
    # 打印发送数量
    cnt = cnt + 1
    print("sec:",sec,"cnt:",cnt)
    time.sleep(sec)
    r = requests.post(url, headers = headers, data = data)
    # 打印发送状态
    print(r.text)

