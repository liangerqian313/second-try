# @Time : 2022/3/20 22:15
# @Author : Liang er qian
# @File : all.py


import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')
    """
    ./temp  临时的json格式报告的路径
    -o  输出的output
    ./report  生成的allure报告的路径
    --clean  清空 ./report路径原来的报告
    """