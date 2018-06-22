import socketserver
import json,os,sys
import hashlib

class MyTCPHandler(socketserver.StreamRequestHandler):
    def put(self,*args):
        cmd_dict = args[0]
        filename = cmd_dict['filename']
        filesize = cmd_dict['size']
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename,"wb")
        m = hashlib.md5()
        self.request.send(b"200")
        received_size = 0
        while received_size < filesize:
            if filesize - received_size > 1024:
                size = 1024
            else:
                size = filesize - received_size
            data = self.request.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            print("file [%s] download finished, size in server is [%s], download size is [%s]" % (
            filename, filesize, received_size))
            new_file_md5 = m.hexdigest()
            f.close()
        client_file_md5 = self.request.recv(1024).decode()
        if new_file_md5 == client_file_md5:
            print("md5 check is ok", new_file_md5)
        else:
            print("md5 check is wrong, md5 in server is [%s], md5 in client is [%s]" % (new_file_md5, client_file_md5))

    def get(self,*args):
        #print(args)
        cmd_dict = args[0]
        filename = cmd_dict['filename']
        if os.path.isfile(filename):
            self.request.send(b'200')
            self.request.recv(1024)
            print("Found file " + filename + ", starting send file now...")
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            self.request.send(str(file_size).encode('utf-8'))
            self.request.recv(1024)
            for line in f:
                m.update(line)
                self.request.send(line)
            print("file md5:", m.hexdigest())
            f.close()
            self.request.send(m.hexdigest().encode('utf-8'))
            print("file send finished.")
        else:
            print("No found file",filename)
            self.request.send(b'404')

    def handle(self,*args):
        print(self.request)
        while True:
            try:
                self.data = self.request.recv(1024).strip()
            except ConnectionResetError as e:
                print(e)
                break
            print("{} wrote:".format(self.client_address))
            #print(self.data.decode())
            cmd_dict = json.loads(self.data.decode())
            action = cmd_dict['action']
            if hasattr(self,action):
                func = getattr(self,action)
                func(cmd_dict)
            else:
                print("no function...")

if __name__ == '__main__':
    HOST, PORT = "0.0.0.0", 9999

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

