__author__ = 'Administrator'

import pymysql

connection = pymysql.connect(host='127.0.0.1',
                             port=12065,
                             user='DnSnsUser',
                             password='DnSnsUser',
                             db='accountTradeCenter',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
       # sql = 'INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)'
        #cursor.execute(sql, ('Robin', 'Zhyea', tomorrow, 'M', date(1989, 6, 14)));
        #sql = 'select book_id from tProduct'

        with open('sql.txt', 'r') as f:
            for i in f:
                temp_sql = 'insert into tProductLog (book_id) VALUES (%s)'
                cursor.execute(temp_sql,i)
                connection.commit()
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句


finally:
    connection.close();
