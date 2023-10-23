import pymysql
from prettytable import PrettyTable


class DAO_recruit_page:
    def __init__(self):
        pass

    # 与本机的数据库建立连接
    def get_conn(self):
        conn = pymysql.connect(
            host='sh-cdb-2uazarja.sql.tencentcdb.com',
            port=59210,
            user='testuser',
            passwd='rsKNp7y89dLhhJKOSmU8',
            db='hjianzhu_test',
            charset='utf8'
        )

        return conn

    # 查询并输出所有数据
    def sel_all(self):
        cursor = self.get_conn().cursor()
        sql = 'select * from sys_user where id = 457'
        rows = cursor.execute(sql)
        res = cursor.fetchall()
        des = cursor.description
        print('共有', rows, '条数据')
        for re in res:
            table = (",".join([item[0] for item in des]))
            # print(type(table))
            table2 = table.split(',')
            # print(table2)
            # print(list(re))
            tb = PrettyTable()  # 生成表格对象
            tb.field_names = table2  # 定义表头
            tb.add_row(list(re))  # 添加一行
            print(tb)
        print('共有', rows, '条数据')


DAO_recruit_page().sel_all()
