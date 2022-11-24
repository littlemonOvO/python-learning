# _*_ coding: utf-8 _*_
# @Time: 2022/11/24 15:19
# @Author: lemon
# @File: aiohttp爬虫
# @Project: learning
import asyncio
import time

import aiohttp


async def download(url):
    print(f'get: {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)


async def main():
    start = time.time()
    tasks = [download(url) for url in ['http://www.163.com', 'http://www.mi.com', 'http://www.baidu.com']]
    await asyncio.wait(tasks)
    end = time.time()
    print(f'Complete in {end - start} seconds')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
