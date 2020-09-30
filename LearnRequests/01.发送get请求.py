'''
发送get请求：
1.get不带参数
2.get带参数
'''

# 导入包
import requests
# url = "http://www.baidu.com"
# response = requests.get(url)  # 发送get请求，使用变量接收相应
# print(response.text)  # 文本类型的结果
# print(response.status_code)  # 状态码
# print(response.reason)  # 状态原因
# print(response.cookies)  # 响应信息的cookies
# print(response.headers)  # 响应的头部信息
# print(response.raw)  # 原始格式的，是个对象
# print(response.raw.read(10))

# 金融项目注册
url = 'http://192.168.150.52:8089/futureloan/mvc/api/member/register?mobilephone=13227011051&pwd=123456&regname=auto'
r = requests.get(url)
print(r.text)
print(r.json())
print(type(r.json()))

#
url = 'http://192.168.150.52:8089/futureloan/mvc/api/member/register'
canshu = {"mobilephone":"13772257670","pwd":"123456","regname":"test"}
r = requests.get(url,params=canshu)
print(r.json())

# httpbin,一个测试网站，有get/post接口，参数任意构造，服务器将发送的请求转成json格式的返回
r = requests.get('http://www.httpbin.org/get?username=123456&pwd=456&email=123456@qq.com')
print(r.text)

# 某宝提供了一个查询手机号码归属地的接口。
r = requests.get('https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13227011051')
print(r.text)

# 发送的请求带请求头
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
r = requests.get('http://www.httpbin.org/get?username=123456&pwd=456&email=123456@qq.com',headers = headers)
print(r.text)

# 既带参数，又带请求头
# requests.get(url,params=,headers=)
