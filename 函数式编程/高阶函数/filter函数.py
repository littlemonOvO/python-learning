# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 10:06
# @Author: lemon
# @File: filter函数
# @Project: learning

"""
filter(func, Iterable):
    将传入的函数依次作用于序列中的每个元素,根据函数返回的bool值决定保留或丢弃该元素
"""

"""
    埃氏筛法: 
        1. 构造从2开始的自然数序列
        2. 取序列第一个数n加入素数序列
        3. 去除序列中所有n的倍数，重复2-3步获得全部素数
"""


# 利用filter()和埃氏筛法输出素数序列

# 构造从3开始的奇数序列
def odds():
    i = 1
    while True:
        i += 2
        yield i


# 构造用于判断数num是否是数n的倍数的函数
def is_not_divisible(n):
    return lambda x: x % n != 0


# 构造素数序列
def primes():
    yield 2
    nums = odds()
    while True:
        # 取序列的第一个数
        num = next(nums)
        yield num
        # 过滤num的倍数生成新的数字序列
        nums = filter(is_not_divisible(num), nums)


prime = primes()
for p in prime:
    if p > 1000:
        break
    print(p, end=' ')
