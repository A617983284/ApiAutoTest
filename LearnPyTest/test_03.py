'''
1.测试前置和后置
2.类级别和方法级别
'''

# 测试类使用Test开头，里面不能有_init_方法
class TestClass:
    def setup_class(self):
        print("测试前置，类里所有用例开始前执行")

    def teardown_class(self):
        print("测试后置，类里所有用例结束前执行")

    def setup(self):
        print("测试前置，每个方法前执行")

    def teardown(self):
        print("测试后置，每个方法后执行")

    def test_case01(self):
        print("测试用例1")

    def test_case02(self):
        print("测试用例2")