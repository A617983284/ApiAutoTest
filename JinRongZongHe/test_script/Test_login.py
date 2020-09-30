'''
登录接口的脚本
'''
import pytest

from JinRongZongHe.baw.DbOp import DbOp
from JinRongZongHe.baw.Member import Member
from JinRongZongHe.caw.DataRead import DataRead
from JinRongZongHe.test_script.conftest import db, BaseRequests
from JinRongZongHe.caw.Assert import Assert

@pytest.fixture(params=DataRead().read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param

# 登录的逻辑
def test_login(register, url, base_requests,login_data):
    # print(f"执行登录失败的用例，测试数据为：{login_data}")
    r = Member().login(url, base_requests, login_data["data"])
    Assert().equal(login_data['expect'], r.json(), "msg,status,code")


# #登录失败的逻辑
# def test_login_fail(fail_data,url,base_requests):
#     print(f"执行登录失败的用例，测试数据为：{fail_data}")
#     r=Member().login(url,base_requests,fail_data["data"])
#     Assert().equal(fail_data['expect'], r.json(), "msg,status,code")
#
# # 登录成功的逻辑
# def test_login_success(success_data,url,db,base_requests):
#     print(f"执行登录成功的用例，测试数据为：{success_data}")
#     # DbOp().delete_user(db, success_data["data"]["mobilephone"])
#     r=Member().login(url,base_requests,success_data["data"])
#     # assert str(success_data["expect"]["msg"])==str(r.json()["msg"])
#     # assert str(success_data["expect"]["code"]) == str(r.json()["code"])
#     # assert str(success_data["expect"]["status"]) == str(r.json()["status"])
#     Assert().equal(success_data['expect'], r.json(), "msg,status,code")
#     # 清理环境
#     # DbOp().delete_user(db,success_data["data"]["mobilephone"])
