import pymysql

conn = None
try:
    # 打开数据库连接
    conn = pymysql.connect("10.10.1.105","root","123456","test")

    with conn as cursor:    # cursor = conn.cursor()
        with cursor:
            sql = "update t set name='efadsfa' where id=3"
            cursor.execute(sql)
            sql = "update t set name='dsafasfda' where id=4"
            cursor.execute(sql)
        cursor.close()
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()


