import socket
import json,os,sys
import hashlib

class TCPClient(object):
    def __init__(self):
        self.client = socket.socket()

    def help(self):
        msg = '''
        get filename
        put filename
        '''
        print(msg)

    def connect(self,ip,port):
        self.client.connect((ip,port))

    def interactive(self):
        while True:
            cmd = input(">>").strip()
            if len(cmd) == 0: continue
            cmd_str = cmd.split()[0]
            if hasattr(self,"cmd_%s"% cmd_str):
                func = getattr(self,"cmd_%s"% cmd_str)
                func(cmd)
            else:
                self.help()

    def cmd_get(self, *args):
        #print(args[0].split())
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            msg_dict = {
                "action":"get",
                "filename":filename
            }
            self.client.send(json.dumps(msg_dict).encode('utf-8'))
            #print("send",json.dumps(msg_dict))
            server_reponse = self.client.recv(1024)
            if server_reponse.decode() == '200':
                self.client.send(b'ready to receive')
                file_total_size = int(self.client.recv(1024).decode())
                self.client.send(b'filesize confirm')
                print("Receiving file...")
                received_size = 0
                if os.path.isfile(filename):
                    f = open(filename + ".new", 'wb')
                else:
                    f = open(filename, 'wb')
                m = hashlib.md5()

                while received_size < file_total_size:
                    if file_total_size - received_size > 1024:
                        size = 1024
                    else:
                        size = file_total_size - received_size
                    data = self.client.recv(size)
                    received_size += len(data)
                    m.update(data)
                    f.write(data)
                else:
                    print("file [%s] download finished, size in server is [%s], download size is [%s]"% (filename,file_total_size,received_size))
                    new_file_md5 = m.hexdigest()
                    f.close()
                server_file_md5 = self.client.recv(1024).decode()
                if new_file_md5 == server_file_md5:
                    print("md5 check is ok",new_file_md5)
                else:
                    print("md5 check is wrong, md5 in server is [%s], md5 in client is [%s]"%(server_file_md5,new_file_md5))

            else:
                print("file is not exist or is a directory!")


if __name__ == '__main__':
    client = TCPClient()
    client.connect("localhost",9999)
    client.interactive()