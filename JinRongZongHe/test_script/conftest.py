'''
脚本层的公共方法
'''
import pytest

#读取环境文件，获取url
from JinRongZongHe.baw.DbOp import DbOp
from JinRongZongHe.baw.Member import Member
from JinRongZongHe.caw.BaseRequests import BaseRequests
from JinRongZongHe.caw.DataRead import DataRead


ENVPATH=r"data_env/env.ini"
@pytest.fixture(scope="session")
def url():
    return DataRead().read_ini(ENVPATH,"url")

@pytest.fixture(scope="session")
def db():
    return eval(DataRead().read_ini(ENVPATH,"db"))

# BaseRequests实例化，整个执行过程实例化一次
@pytest.fixture(scope="session")
def base_requests():
    return BaseRequests()

@pytest.fixture(params=DataRead().read_yaml(r"data_case/login_setup.yaml"))
def setup_data(request):
    return request.param

# 用session保证先执行这个
@pytest.fixture()
def register(setup_data,db,url,base_requests):
    # 注册用户
    r = Member().register(url, base_requests, setup_data["data"])
    yield
    # 删除注册用户
    DbOp().delete_user(db, setup_data["data"]["mobilephone"])
