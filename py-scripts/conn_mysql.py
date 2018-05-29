#!/usr/bin/python3
import pymysql

#打开数据库连接
db = pymysql.connect("localhost","root","123456","mycat")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("select version()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s "% data)

def echo():
    sql = "select * from employee" 
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print("fname=%s,lname=%s,age=%d,sex=%s,income=%d"%(fname,lname,age,sex,income))
    except:
        print("Error: unable to fetch data")

cursor.execute("drop table if exists employee")
sql = """create table employee(
         first_name char(20) not null,
         last_name char(20),
         age int,
         sex char(1),
         income float )"""
cursor.execute(sql)

# SQL 插入语句
sql_1 = """insert into employee values ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql_1)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
echo()
sql_3 = "update employee set age = age + 1 where sex = '%c'"%('M')
try:
    cursor.execute(sql_3)
    db.commit()
except:
    db.rollback()
echo()
# 关闭数据库连接
db.close()
