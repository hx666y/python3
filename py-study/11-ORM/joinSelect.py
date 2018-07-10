import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, and_, or_, not_
from sqlalchemy.orm import sessionmaker, relationship
import enum

# 实体基类
Base = declarative_base()

def show(emps):
    for x in emps:
        print(x)
    print('~~~~~~~~~', end='\n\n')

# 实体类
class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'

class Employee(Base):
    __tablename__ = 'employees'

    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    # 多表关联 join查询
    depts = relationship('Dept_emp')

    def __repr__(self):
        return "<{} emp_no:{} name:{}.{}>".format(self.__class__.__name__, self.emp_no, self.first_name, self.last_name)

    __str__ = __repr__

class Department(Base):
    __tablename__ = 'departments'

    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), unique=True, nullable=False)

    def __repr__(self):
        return "<{} dept_no:{} dept_name:{}>".format(self.__class__.__name__, self.dept_no, self.dept_name)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4), ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<{} emp_no:{} dept_no:{}>".format(self.__class__.__name__, self.emp_no, self.dept_no)

#引擎，管理连接池
host = '10.10.1.105'
port = 3306
user = 'root'
password = '123456'
database = 'test'

#engine = create_engine('mysql+pymysql://user:password@hostname:port/dbname')
conn_str = "mysql+pymysql://{}:{}@{}:{}/{}".format(user, password, host, port, database)
engine = sqlalchemy.create_engine(conn_str, echo=True)

Session = sessionmaker()
session = Session(bind=engine)


emps = session.query(Employee).filter(Employee.emp_no > 10035).order_by(Employee.emp_no.desc())
show(emps)


































