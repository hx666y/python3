import requests

login_url = "http://www.xiaojike.cn/sign_in/"

data = {'username':'hx666y',
        'password':'hongxuan1992',
        }

response = requests.post(url=login_url,data=data,)


print(response.status_code)
print(response.url)
print(response.headers)