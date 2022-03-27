# @Time : 2022/3/14 22:37
# @Author : Liang er qian
# @File : test_02.py
# @Software: PyCharm


import pytest
from comm.constants import BASE_DIR
import os

class TestQuite:
    def setup_class(self):
        print('测试夹具开始')

    def teardown_class(self):
        print('测试夹具结束')

    @pytest.mark.run(order=2)
    def test01(self):
        print('退出第一步')

    @pytest.mark.run(order=1)
    def test02(self):
        print('退出第二步')

    @pytest.mark.run(order=3)
    def test03(self):
        print('退出第三步')

    def test04(self):
        print('退出第四步')

    def test05(self):
        print('退出第五步')

if __name__ == '__main__':
    pytest.main(["-sv", "test_02.py"])
    os.system('allure generate ../temp -o ../report --clean')
