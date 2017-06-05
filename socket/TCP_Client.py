#coding=utf-8
import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 1235
s.connect((host, port))
while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    elif msg == 'exit':
        break
    s.send(msg.encode())
    #data = s.recv(1024)
    #print('Reply from server ----%s' %data)
s.close()