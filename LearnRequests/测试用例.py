import requests

# 注册
url = 'http://192.168.150.222:8081/futureloan/mvc/api/member/register'
canshu = {"mobilephone":"13909116693","pwd":"123456"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116694","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116695","pwd":"12345678","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116696","pwd":"123456789012345678","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116697","pwd":"","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"","pwd":"","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116698","pwd":"12345","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116699","pwd":"1234567890123456789","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"1390911669","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"1390911669890","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13#09116698","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13909116694","pwd":"123456","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"11109116698","pwd":"12345","regname":"Amy"}
r = requests.get(url,params=canshu)
print(r.text)

# 登录
url = 'http://192.168.150.222:8081/futureloan/mvc/api/member/login'
canshu = {"mobilephone":"13227011051","pwd":"123456"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13227011052","pwd":"12345678"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13227011053","pwd":"123456789012345678"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"","pwd":"123456"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13227011051","pwd":""}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"","pwd":""}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13#27011051","pwd":"123456"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13227011051","pwd":"12345"}
r = requests.get(url,params=canshu)
print(r.text)

canshu = {"mobilephone":"13#27011051","pwd":"12345"}
r = requests.get(url,params=canshu)
print(r.text)

# 获取用户列表
url = 'http://192.168.150.222:8081/futureloan/mvc/api/member/list'
r = requests.get(url)
print(r.text)
