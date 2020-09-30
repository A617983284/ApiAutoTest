'''
fixture带参数
'''

import pytest
import requests

# 测试数据，可以从CSV读取，也可以从xml读取，也可以从yaml文件中读取
data = [{"data":{"mobilephone":"15891113333","pwd":"abcdef"},
         "expect": {"msg": "登录成功", "code": "10001", "status": "1"}},
        {"data":{"mobilephone":"15891113345","pwd":"abcdefabcdefabcdef"},
         "expect": {"msg": "登录成功", "code": "10001", "status": "1"}},

        {"data": {"mobilephone": "13901116694", "pwd": "1234"},
         "expect": {"msg": "用户名或密码错误", "code": "20111", "status": "0"}},
        {"data": {"mobilephone": "13901116695", "pwd": "1234"},
         "expect": {"msg": "用户名或密码错误", "code": "20111", "status": "0"}},
        ]


@pytest.fixture(params=data)
def register_data(request):  # request是fixture中的关键字
    return request.param  # 通过request.param获取每一组测试数据


def test_register(register_data):
    print(register_data)
    ret = requests.post("http://192.168.150.222:8081/futureloan/mvc/api/member/login", register_data['data'])
    # assert ret.json()['msg']==register_data['expect']['msg'] # 某些接口可能返回一些动态的数据，比如时间戳，比如ID
    assert str(ret.json()['msg']) == register_data['expect']['msg']
    assert str(ret.json()['code']) == register_data['expect']['code']
    assert str(ret.json()['status']) == register_data['expect']['status']


# def test_list():
#     ret = requests.get("http://192.168.150.52:8089/futureloan/mvc/api/member/register", register_data['data'])
#     print(ret.text)