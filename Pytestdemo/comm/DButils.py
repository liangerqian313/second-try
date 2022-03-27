# @Time : 2022/3/16 13:41
# @Author : Liang er qian
# @File : DButils.py

import cx_Oracle
from configparser import ConfigParser


class DBUtils:
    # 封装连接数据库对象和游标
    def __init__(self):
        try:
            cnp = ConfigParser()
            cnp.read("D:\Casedemo\Pytestdemo\config\config.ini", encoding='utf-8')
            host = cnp.get("plsql", "host")
            port = cnp.get('plsql', 'port')
            user = cnp.get('plsql', 'user')
            password = cnp.get('plsql', 'password')
            db = cnp.get('plsql', 'db')
            self.conn = cx_Oracle.connect(host=host, port=port, user=user, password=password, db=db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('数据连接异常', e)

    # 封装 关闭游标和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装 结果集有多少条数据
    # 如果execute中只传一个参数，我们需要运行 cursor.execute(sql)
    # 如果execute中传2个参数，我们需要运行 cursor.execute(sql,占位符数据)

    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
                return self.count
            elif params is not None:
                return self.cursor.execute(sql, params)
        except cx_Oracle.Error as e:
            print('查询条目数失败', e)

    # 封装查询一条数据
    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
                return self.cursor.fetchone()
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchone()
        except cx_Oracle.Error as e:
            print('查询单条用例失败', e)

    # 封装查询所有数据
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)
                return self.cursor.fetchall()
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchall()
        except cx_Oracle.Error as e:
            print('查询多条用例失败', e)

    # 封装增删该
    def cud(self, sql, params):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except cx_Oracle.DatabaseError as e:
            self.conn.rollback()
            print('操作失败', e)


if __name__ == '__main__':
    db = DBUtils()
    data = db.find_count("select count(1) from bp_group_info where group_code ='GT003'")
    print(data)
