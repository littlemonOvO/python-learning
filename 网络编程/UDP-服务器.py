# _*_ coding: utf-8 _*_
# @Time: 2022/11/1 10:55
# @Author: lemon
# @File: UDP编程
# @Project: learning
import socket

# 指定类型为UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(('127.0.0.1', 7777))
print('Bind UDP on port 7777...')

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print(f'Received from {addr}')
    s.sendto(b'Hello, %s!' % data, addr)
