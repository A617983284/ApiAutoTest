'''
获取cookie：服务的响应中如果带了set-cookie,可以通过r.cookies获取
'''
import requests

headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
r = requests.get("http://www.baidu.com",headers=headers)  # headers是字典
c = r.cookies
print(type(c)) # <class 'requests.cookies.RequestsCookieJar'>
# RequestsCookieJar转为字典
cookies_dict = requests.utils.dict_from_cookiejar(c)
# 遍历字典
for key,value in cookies_dict.items():
    print(key,value)

# 发送百度搜索的请求，将上一步百度首页获取到的cookies带上
# wd=requests，这个是搜索的内容
# headers加上一定可以，不加有时候就不可以
# 如果wd是中文，那就得成编码后的
r = requests.get("http://www.baidu.com/s?wd=requests",headers=headers,cookies = cookies_dict)
print("简书" in r.text)
assert  "简书" in r.text


# r = requests.get("http://www.baidu.com/s",params={"wd":"ç¾åº¦å®å¨éªè¯"},headers=headers,cookies = cookies_dict)
# print("<title>协议_百度搜索</title>" in r.text)
# assert  "ç¾åº¦å®å¨éªè¯" in r.text
# print(r.text)