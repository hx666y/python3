
# 使用requests保存远程图片（或文件）
import requests
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR,'static')
if not os.path.isdir(STATIC_DIR):
    os.mkdir(STATIC_DIR)
else:
    pass

def saveRemoteImage():
    imgurl = 'https://cdn.pixabay.com/photo/2018/05/11/17/52/blue-tit-3391158__340.jpg'
    filename = imgurl.split('/')[-1]
    path = os.path.join(STATIC_DIR,filename)
    if not os.path.exists(path):
        r = requests.get(imgurl)
        with open(path, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)
            #f.write(r.content)
            print('OK')
    else:
        print('Already Exists.')


saveRemoteImage()