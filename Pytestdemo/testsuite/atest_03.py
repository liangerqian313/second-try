# @Time : 2022/3/16 22:32
# @Author : Liang er qian
# @File : atest_03.py
import allure
import pytest
import requests
from comm.DButils import DBUtils
from comm.excel_Utils import ReadExcel
from comm.constants import DATA_FILE
import openpyxl
import json
from comm.logUtils import logger

@allure.feature("用户登录模块")
class TestDemo:
    @pytest.fixture(autouse=True)
    def star_prepare(self):
        self.db = DBUtils()
        yield
        self.db.close()

    cases = ReadExcel.read_data_all(DATA_FILE, "login")

    @allure.Severity("critical")
    @allure.description("用户登录接口")
    @pytest.mark.parametrize('case', cases)
    def test_login(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url, name='接口路径')
        allure.attach(body=case.case_data, name='请求参数')
        respons = requests.post(url=case.url, data=eval(case.case_data))
        res_body = respons.json()
        print(res_body)
        allure.attach(body=str(res_body), name='响应结果')

        try:
            if case.case_id==1:
                assert case.expct in res_body
            else:
                assert eval(case.expet) == res_body

        except AssertionError as e:
            ReadExcel.wirte_data(DATA_FILE,'login',case.case_id,7,'失败')
            logger.error('测试编号{},测试标题{},执行失败,实际结果为{}'.format(case.case_id,case.case_title,res_body))
            logger.exception(e)
            raise e
        else:
            ReadExcel.wirte_data(DATA_FILE,'login',case.cae_id,7,'成功')
            logger.info('测试编号{},测试标题{},执行成功。'.format(case.case_id,case.case_title))


if __name__ == '__main__':
    pytest.main(["-vs", "./testsuite/atest_03.py"])
