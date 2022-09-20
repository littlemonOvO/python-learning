# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 9:37
# @Author: lemon
# @File: 偏函数
# @Project: learning

"""
偏函数: 为一个函数的某些参数设置默认值,并返回一个新函数,使调动带这些默认参数的函数更简单
eg: 创建一个按二进制转换、将字符串转换成整数的函数int(2)
    int('12345', base=2) ==> int2 = functools.partial(int, base=2)

    new_func = functools.partial(func, *args, **kwargs)
"""
import functools

# 返回10和传入参数中最大的数
max = functools.partial(max, 10)

print(max(1, 2, 3))  # 10
