'''
断言公共方法
'''
import pytest_check as check

class Assert:
    #  Assert().equal(fail_data['expect'],r.json(),"msg,status,code")
    def equal(self,expect,response, key_str):
        '''
        Assert().equal(fail_data['expect'],r.json(),"msg,status,code")
        :param expect:
        :param response:
        :param key_str:
        :return:
        '''
        try:
            keys = key_str.split(",")
            for key in keys:
                r = str(response[key])
                e = str(expect[key])
                check.equal(r,e)
                print(f"响应信息为：{response}，预期结果为{expect}，校验字段为：{key},实际结果为{r},预期结果为{e}")
        except Exception as e:
            print(f"响应信息为：{response}，预期结果为{expect}，校验字段为：{key},实际结果为{r},预期结果为{e}")

        # assert str(fail_data["expect"]["msg"]) == str(r.json()["msg"])
        # assert str(fail_data["expect"]["code"]) == str(r.json()["code"])
        # assert str(fail_data["expect"]["status"]) == str(r.json()["status"])