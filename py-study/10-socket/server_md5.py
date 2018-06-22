import socket
import os,time,hashlib

server =socket.socket()
server.bind(('0.0.0.0', 9998))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn....", addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)

            for line in f:
                m.update(line)
                conn.send(line)
            print("file md5", m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        else:
            conn.send(b'404')
            break
        print("send done.")
    conn.close()




