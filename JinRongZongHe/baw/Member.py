'''
业务AW：按模块划分
'''
from JinRongZongHe.caw.BaseRequests import BaseRequests

REGISTER="futureloan/mvc/api/member/register"
LOGIN="futureloan/mvc/api/member/login"
class Member:
    def register(self,url,base_requests,data):
        '''
        用户注册的接口
        :param url: 环境信息
        :param base_requests:
        :param data: 数据
        :return: 响应信息
        '''
        real_url=url+REGISTER
        r=base_requests.post(real_url,data=data)
        return r

    def login(self,url,base_requests,data):
        real_url =url+LOGIN
        r =base_requests.post(real_url, data=data)
        return r

if __name__ == '__main__':
    r=Member().register("http://192.168.150.222:8081/",BaseRequests(),
                        {"mobilephone":"123456678","pwd":"123456","regname":"ads"})
    print(r.text)