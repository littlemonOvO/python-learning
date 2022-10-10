# _*_ coding: utf-8 _*_
# @Time: 2022/10/2 14:13
# @Author: lemon
# @File: 多线程
# @Project: learning
import threading
import time


def loop():
    print(f'线程{threading.current_thread().name}执行中...')
    n = 0
    while n < 5:
        n += 1
        print(f'线程{threading.current_thread().name} => {n}')
        time.sleep(1)
    print(f'线程{threading.current_thread().name}执行完毕.')


# if __name__ == '__main__':
#     print(f'主线程{threading.current_thread().name}执行中...')
#     t = threading.Thread(target=loop, name='LoopThread')
#     t.start()
#     t.join()
#     print(f'主线程{threading.current_thread().name}执行完毕')


"""
    系统分配资源的最小单位是进程，一个进程中可能有多个线程，在多线程中，
进程中的变量由所有线程共享，因此需要引入锁。
    创建锁由threading.Lock()实现。
"""

balance = 0
lock = threading.Lock()


# 操作进程内变量
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        # 修改前加锁
        lock.acquire()
        try:
            change_it(n)
        # 修改结束后释放锁
        finally:
            lock.release()
            pass


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f'balance = {balance}')

"""
    
"""
