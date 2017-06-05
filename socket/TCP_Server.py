#coding=utf-8
import socket
from _thread import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1235

s.bind((host, port))
s.listen(3)
def thread(client):
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            print('receive data:%s' %data)
            msg = input('>>:').strip()
            if len(msg) == 0:
                continue
        except ConnectionError as con:
            print('error:', data)
        client.sendall(msg.encode())
    #client.close()
    
while 1:
    client, ipaddr = s.accept()
    print('connected with:' + ipaddr[0] + ':' + str(ipaddr[1]))
    start_new_thread(thread, (client, ))
s.close()
