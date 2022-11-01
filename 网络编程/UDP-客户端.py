# _*_ coding: utf-8 _*_
# @Time: 2022/11/1 10:59
# @Author: lemon
# @File: UDP-客户端
# @Project: learning
import socket

# 客户端
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Alice', b'Bob', b'Camille']:
    s.sendto(data, ('127.0.0.1', 7777))
    print(s.recv(1024).decode('utf-8'))

s.close()
