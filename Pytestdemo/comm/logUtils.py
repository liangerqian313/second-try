# @Time : 2022/3/19 14:05
# @Author : Liang er qian
# @File : logUtils.py

"""
封装log工具
"""

import logging
from comm.constants import INFO_FILE,ERROR_FILE

def get_logger():
    # 第二步:创建日志对象
    logger = logging.getLogger()  # 获取logger对象
    logger.setLevel('DEBUG')  # 设置默认的日志级别  接收DEBUG及以上的级别日志

    # 第三步:设置输出方向
    # 输出到控制台，并且级别为INFO，代表把INFO及INFO以后的内容打印到控制台
    sh1 = logging.StreamHandler()
    sh1.setLevel("INFO")

    # 输出到 ./info.log 文件中，并且内容为追加写入，级别为INFO及INFO以后级别的内容
    sh2 = logging.FileHandler(filename=INFO_FILE, mode='a', encoding='utf-8')
    sh2.setLevel("INFO")

    # 输出到 ./error.log文件中，并且内容为追加写入,级别为ERROR及ERROR以后的内容
    sh3 = logging.FileHandler(filename=ERROR_FILE, mode='a', encoding='utf-8')
    sh3.setLevel('ERROR')

    # 第四步:添加输出方向到logger中
    logger.addHandler(sh1)
    logger.addHandler(sh2)
    logger.addHandler(sh3)

    # 第五步:指定通道日志输出的格式
    fmt = '%(asctime)s - [%(filename)s ->%(lineno)d] - %(levelname)s:%(message)s'
    my_fmt = logging.Formatter(fmt)
    sh1.setFormatter(my_fmt)
    sh2.setFormatter(my_fmt)
    sh3.setFormatter(my_fmt)

    return logger


logger = get_logger()