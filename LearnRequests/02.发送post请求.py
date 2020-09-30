'''
发送post请求
1.使用data传参
2.使用json传参
'''

import requests
url = 'http://www.httpbin.org/post'
canshu = {"username":"amyLi","password":"123456"}
r = requests.post(url, data=canshu)  # 使用data传参"Content-Type": "application/x-www-form-urlencoded"
print(r.text)

r = requests.post(url, json=canshu)
print(r.text)  # 使用json传参"Content-Type": "application/json"
# post接口具体用data还是json传参，是后台实现决定的

# 金融项目，登录接口，post
url = 'http://192.168.150.52:8089/futureloan/mvc/api/member/login'
canshu = {"mobilephone":"13772257670","pwd":"123456"}
r = requests.get(url,params=canshu)
print(r.json())

