# _*_ coding: utf-8 _*_
# @Time: 2022/11/18 10:34
# @Author: lemon
# @File: asyncio库
# @Project: learning
import asyncio
import time

import requests

"""
异步函数不同于普通函数，调用普通函数会得到返回值，而调用异步函数会得到一个协程对象。
我们需要将协程对象放到一个事件循环中才能达到与其他协程对象协作的效果，因为【事件循环会负责处理子程序切换的操作】，简单的说就是让阻塞的子程序让出CPU给可以执行的子程序。


async:
    声明一个函数为异步函数，使其能够在函数执行过程中挂起去执行其他异步函数，直到挂起条件消失时再回来执行。
await:
    声明程序挂起，await后面只能跟异步程序函数或有__await__属性的awaitable对象。
awaitable对象必须满足以下条件之一：
    * 原生协程对象
    * types.coroutine()修饰的基于生成器的协程对象
    * 实现了await method并返回了iterator的对象
仅仅把涉及I/O操作的代码封装到async中并不能实现异步执行，必须使用支持异步操作的非阻塞代码(aiohttp)才能实现真正的异步。
"""


def example1():
    async def funcA():
        await asyncio.sleep(4)
        print('A 函数执行完毕')

    async def funcB():
        await asyncio.sleep(2)
        print('B 函数执行完毕')

    async def funcC():
        await asyncio.sleep(8)
        print('C 函数执行完毕')

    loop = asyncio.get_event_loop()
    tasks = [funcA(), funcB(), funcC()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


#
# start = time.time()
# example1()
# end = time.time()
# print(f'总耗时：{str(end - start)}')


def example2():
    async def download(url):
        print(f'get {url}')
        response = requests.get(url)
        print(response.status_code)

    async def wait_download(url):
        await download(url)
        print(f'get {url} data complete.')

    loop = asyncio.get_event_loop()
    start = time.time()
    tasks = [wait_download(url) for url in ['http://www.163.com', 'http://www.mi.com', 'http://www.baidu.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(f'Complete in {str(end - start)} seconds.')


# 程序并未异步执行
example2()
