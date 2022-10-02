# _*_ coding: utf-8 _*_
# @Time: 2022/10/2 9:17
# @Author: lemon
# @File: 多进程
# @Project: learning

import os
import random
import time

"""
    fork():
        由在Unix/Linux系统提供;
        调用时操作系统为当前进程创建一个子进程,在父进程和子进程内分别返回;
        子进程返回0,父进程返回子进程的id,子进程调用getppid()获取父进程id;
"""
# 以下代码仅能在Unix/Linux/Mac系统下运行
# print('Process (%s) start...' % os.getpid())
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

"""
    multiprocessing:跨平台的多进程模块
"""
from multiprocessing import Process


# 子进程要执行的代码
def run(name):
    print(f'子进程名:{name}, pid:{os.getpid()}')


# if __name__ == '__main__':
#     # 创建进程实例,传入执行函数名和函数参数
#     p = Process(target=run, args=('test',))
#     print('子进程准备执行...')
#     p.start()
#     p.join()
#     print('子进程执行完毕.')

"""
    Pool:进程池
"""


# 定义进程执行函数
def long_time_task(name):
    print(f'子进程名:{name}, pid:{os.getpid()} 执行...')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'子进程 {name} 执行时间:{(end - start):0.2f}s.')


# if __name__ == '__main__':
#     # 最多同时执行三个进程，因此之后进程名为3的进程须等待此前一个进程执行完后才能开始执行
#     p = Pool(3)
#     start = time.time()
#     print('子进程准备执行...')
#     for i in range(4):
#         p.apply_async(long_time_task, args=(i, ))
#     print('等待子进程执行...')
#     # 调用join()之前必须先调用close(),此后不能再添加新的Process
#     p.close()
#     # 等待所有子进程执行完毕
#     p.join()
#     end = time.time()
#     print(f'子进程执行完毕 总用时:{(end - start):0.2f}s')

"""
    进程间通信
"""
from multiprocessing import Queue


# 写数据进程执行函数
def write(q):
    print(f'写进程pid:{os.getpid()}')
    for value in ['A', 'B', 'C']:
        print(f'写入数据:{value}')
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行函数
def read(q):
    print(f'读进程pid:{os.getpid()}')
    while True:
        value = q.get(True)
        print(f'读取到数据:{value}')


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # 强行终止进程
    pr.terminate()
