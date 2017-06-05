#coding=utf-8
import socket,sys
from _thread import *

host = ''
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

try:
    s.bind((host, port))
except socket.error as msg:
    print(b'bind failed.Error code:' + str(msg[0]) + 'Message' + msg[1])
    sys.exit()
    
print('socket bind complete')

s.listen(10)
print('socket now listening')

def clientthread(conn):
    conn.send(b'welcome to the server\n')

    # 等待接受连接,阻塞调用
    while True:
        pass
        # data = conn.recv(1024)
        # reply = b'OK...' + data
        # if not data:
        #     break
        #
        # conn.sendall(reply)
            

    #conn.close()

while 1:
    conn, addr = s.accept()
    
    print('connected with ' + addr[0] + ':' + str(addr[1]))
    
    start_new_thread(clientthread, (conn,))

s.close()