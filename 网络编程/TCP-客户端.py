# _*_ coding: utf-8 _*_
# @Time: 2022/11/1 10:34
# @Author: lemon
# @File: TCP-客户端
# @Project: learning
import socket

print('客户端启动')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 7777))

print(s.recv(1024).decode('utf-8'))

for data in [b'Alice', b'Bob', b'Camille']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
