import socket
import sys

# 创建socket对象
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('失败连接' + str(msg[0]) + 'Error msg:' + msg[1])
    sys.exit()

print('Socket Created')

host = 'baidu.com'
port = 80

# 获取ip 连接服务端
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror as msg:
    print(msg[0])
    sys.exit()

print('ip address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip, port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# 发送请求
message = b'GET / HTTP/1.1\r\n\n'

try:
    s.sendall(message)
except socket.error:
    print('Send failed')
    sys.exit()
print('Message send successfully')

# 接收数据
reply = s.recv(4096)
print(reply)

s.close()