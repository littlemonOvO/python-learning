# _*_ coding: utf-8 _*_
# @Time: 2022/11/24 15:36
# @Author: lemon
# @File: 多线程与多进程爬虫
# @Project: learning

import concurrent.futures
import re
import time

import requests


def get_index():
    response = requests.get('http://www.shuquge.com/txt/8659/index.html')
    response.encoding = response.apparent_encoding
    html = response.text
    result = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', html)
    return result


# 多线程
def thread_download_ebook(url, name):
    print(name, url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
    }
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    html = response.text
    result = re.findall('<div id="content" class="showtxt">(.*?)</div>', html, re.S)
    with open(name + '.txt', mode='w', encoding='utf-8') as f:
        f.write(result[0].replace('<br/>&nbsp;&nbsp;&nbsp;&nbsp;', "").replace('<br/>', ""))


# 多进程
def process_download_ebook(urls):
    # 每个进程启动5个线程
    thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    for url, name in urls:
        # 往线程池里放任务
        thread_pool.submit(thread_download_ebook, 'http://www.shuquge.com/txt/8659/' + url, name)
    # 等待线程池关闭
    thread_pool.shutdown()


if __name__ == '__main__':
    content_list = get_index()[:20]
    # 将任务分成5份
    length = int(len(content_list) / 5)
    start_time = time.time()
    # 启动5个进程
    # 进程间通信不共享数据
    process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    for i in range(length):
        if i == length:
            i += 1
        # 向进程池添加任务
        process_pool.submit(process_download_ebook, content_list[i * length:(i + 1) * length])
    # 等待任务结束
    process_pool.shutdown()
    print(f'cost time: {time.time() - start_time}s.')
