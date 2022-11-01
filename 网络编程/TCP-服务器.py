# _*_ coding: utf-8 _*_
# @Time: 2022/11/1 10:23
# @Author: lemon
# @File: TCP-服务器
# @Project: learning
import socket

# 创建基于IPv4和TCP的socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听本地端口
s.bind(('127.0.0.1', 7777))

# 开始监听，最大连接数为5
s.listen(5)
print('Waiting for connection...')


# 线程处理TCP函数
def tcplink(socket, addr):
    print(f'Accept new connection from {addr}')
    socket.send(b'Welcome!')
    while True:
        # 接收客户端发送的信息
        data = socket.recv(1024)
        time.sleep(1)
        # 退出条件
        if not data or data.decode('utf-8') == 'exit':
            break
        socket.send(f"Hello, {data.decode('utf-8')}!".encode('utf-8'))
    socket.close()
    print(f'Connection from {addr} closed.')


while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
