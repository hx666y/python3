import socket

client = socket.socket()
client.connect(('localhost', 7788))

while True:
    cmd = input(">>").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))