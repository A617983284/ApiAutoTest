'''
自动管理cookie
'''

import requests

# 新建一个session，通过session自动管理Cookie
s = requests.Session()

# 访问百格的首页
s.get("http://www.bagevent.com")
print(s.cookies)
print(requests.utils.dict_from_cookiejar(s.cookies))

# 调login接口
param = {
"access_type":1,
"loginType":1,
"emailLoginWay":0,
"account":"2780487875@qq.com",
"password":"qq2780487875",
"remindmeBox":"on",
"remindme":1
}
r = s.post("https://www.bagevent.com/user/login",data=param)
print(s.cookies)
print(requests.utils.dict_from_cookiejar(s.cookies))

r=s.get('https://www.bagevent.com/vlist/common/surveyList')
print(r.json())
print(r.json()["list"][0]["survey_id"])