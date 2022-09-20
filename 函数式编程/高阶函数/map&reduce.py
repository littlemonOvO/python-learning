# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 9:52
# @Author: lemon
# @File: map&reduce
# @Project: learning

"""
map(func, Iterable): 接收两个参数,一个是函数,一个是 Iterable,
    map将传入的函数依次作用到序列的每个元素,并把结果作为新的 Iterable 返回。

reduce(func, Iterable): 把一个函数作用在一个序列上,这个函数接收两个参数,
    函数的返回结果和序列的下一个元素继续传入函数中做累积计算。
    reduce(func, [x1, x2, x3, x4]) = func(func(func(x1, x2), x3), x4)
"""

# 使用map和reduce实现将字符串转换成浮点数
from functools import reduce


# 使用map()和reduce()实现将字符串转换成浮点数
def str2float(s):
    # 确定小数点位置
    i = s[::-1].find('.')

    # 字符转数字, 利用map将字符串转成整数列表
    def char2num(c):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[c]

    # 对整数列表做累积计算
    return reduce(lambda x, y: x * 10 + y, map(char2num, s.replace('.', ''))) / 10 ** i


print(str2float('123.456'))  # 123.456
