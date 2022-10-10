# _*_ coding: utf-8 _*_
# @Time: 2022/10/4 10:06
# @Author: lemon
# @File: ThreadLocal的使用
# @Project: learning

import threading

# 创建全局ThreadLocal对象
local_school = threading.local()


def process_stud():
    # 获取当前线程的student
    std = local_school.student
    print(f'{threading.current_thread().name} - Hello, {std}')


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_stud()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

"""
    ThreadLocal可以被看作是一个全局dict, key值为进程内各线程的唯一标识, value值为线程内的局部变量
    每个线程只能读写自己的线程的独立副本而互不干扰, ThreadLocal解决了参数在一个线程中哥哥函数之间互相传递的问题
"""
