'''
两种超时的场景：
1.接口耗时比较久，设置耗时时间，避免还没有执行完，超时退出了
2.接口性能，比如接口要求在500ms执行完成
如果耗时比较久，就有问题
'''

import requests
for i in range(10):
    try:
        url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13227011051"
        r = requests.get(url,timeout = 0.3)
        print(r.status_code)
    except Exception as e:
        print(e)
