'''
fixture 嵌套
'''
import faker
import pytest

f= faker.Faker()
@pytest.fixture()
def username():
    return f.user_name()  # 随机的用户名

@pytest.fixture()
def pwd():
    return  f.password()  # 随机的密码

@pytest.fixture()
def get_user_pwd(username,pwd):
    return {"username":username,"pwd":pwd}
def test_login(get_user_pwd):
    print(f"测试登录功能，登录的用户名：{get_user_pwd['username']}")