import requests
import time
import os


vk_group = "writehere"
vk_token = "writehere"
bot_token = "writehere"
channel = "@channel"



lastpost = ""
while True:
    try:
        r = requests.get("https://api.vk.com/method/wall.get", params={"access_token":vk_token,"domain":vk_group,"v":"5.92","count":"1"}).json()["response"]["items"][0]["attachments"]
        picUrl= r[0]['photo']['sizes'][-1]['url']
        if r[0]['photo']['post_id'] == lastpost:
            print("Нет новых публикаций")
            time.sleep(300)
        else:
            lastpost = r[0]['photo']['post_id']
            print("Появилась новая публикация")
            r = requests.get(picUrl)
            inp = open('pic/1.jpg', "wb")
            inp.write(r.content)
            inp.close()
            out = {'photo': open('pic/1.jpg', 'rb')}
            data = {'chat_id': channel}
            r = requests.post("https://api.telegram.org/bot"+bot_token+"/sendPhoto", files=out, data=data)
            out['photo'].close()
            os.remove("pic/1.jpg")
            print("Отправлено")
            time.sleep(300)
    except LookupError:
        print("Пустая публикация/нет картинок/пересылка")
        print("жду час...")
        time.sleep(3600)
