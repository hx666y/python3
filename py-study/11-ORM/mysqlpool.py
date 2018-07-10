import pymysql
from queue import Queue
import threading

class ConnPool:
    def __init__(self,size,*args,**kwargs):
        self._size = size
        self._pool = Queue(size)
        self.local = threading.local()

        for i in range(size):
            conn = pymysql.connect(*args,**kwargs)
            self._pool.put(conn)

    def get_conn(self):
        conn = self._pool.get()
        self.local.conn = conn
        return conn

    def return_conn(self,conn:pymysql.connections.Connection):
        if isinstance(conn, pymysql.connections.Connection):
            self._pool.put(conn)
            self.local.conn = None

    @property
    def size(self):
        return self._pool.qsize()

    def __enter__(self):
        self.local.conn = self.get_conn()
        return self.local.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.local.conn.rollback()
        else:
            self.local.conn.commit()
        self.return_conn(self.local.conn)
        self.local.conn = None


pool = ConnPool(5,"10.10.1.105","root","123456","test")

with pool as cursor:
    with cursor:
        sql = "select * from t"
        cursor.execute(sql)
        print(cursor.fetchone())

        sql = "show processlist"
        cursor.execute(sql)
        for x in cursor:
            print(x)