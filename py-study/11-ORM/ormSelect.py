import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import sessionmaker

# 实体基类
Base = declarative_base()

# 实体类
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<{} id:{} name:{} age:{}>".format(self.__class__.__name__, self.id, self.name, self.age)

    __str__ = __repr__

#引擎，管理连接池
host = '10.10.1.105'
port = 3306
user = 'root'
password = '123456'
database = 'test'

#engine = create_engine('mysql+pymysql://user:password@hostname:port/dbname')
conn_str = "mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, host, port, database)
engine = sqlalchemy.create_engine(conn_str, echo=True)

# 创建表
#Base.metadata.create_all(engine)
# 删除
#Base.metadata.drop_all(engine)

Session = sessionmaker()
session = Session(bind=engine)

try:
    # 新增
    '''
    lst = []
    for i in range(5):
        student = Student()
        student.name = 'tom' + str(i)
        student.age = 20 + i
        lst.append(student)

        session.add_all(lst)
        session.commit()    
    '''
    # 修改
    '''
    student = session.query(Student).get(2)
    student.age = 80
    session.add(student)
    session.commit()
    '''
    # 删除
    '''
    student = session.query(Student).get(2)
    session.delete(student)
    session.commit()
    '''
    # 查询删除
    queryjob = session.query(Student).filter(Student.id >= 2)
    for x in queryjob:
        session.delete(x)
    session.commit()

except Exception as e:
    print("~~~~~~~~~~")
    print(e)
    session.rollback()
finally:
    pass




























