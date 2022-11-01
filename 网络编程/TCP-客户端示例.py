# _*_ coding: utf-8 _*_
# @Time: 2022/11/1 9:58
# @Author: lemon
# @File: TCP编程
# @Project: learning
import socket

# 创建socket
# AF_INET指定使用IPv4协议 SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))

# 发送http请求
request = b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n'
s.send(request)

# 接收数据
buffer = []

while True:
    # 每次最多接收1024字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接
s.close()

# 分离出响应头和主体部分
header, html = data.split(b'\r\n\r\n', 1)
print('-' * 8)
print(header.decode('utf-8'))
print('-' * 8)
print(html.decode('utf-8'))
print('-' * 8)
