# _*_ coding: utf-8 _*_
# @Time: 2022/10/31 14:28
# @Author: lemon
# @File: itertools
# @Project: learning
import itertools

"""
itertools:
    提供各种操作迭代对象的函数的内建模块
    1. 无限迭代器
    2. 组合迭代器
    
"""
# 无限迭代器
# count([start=0, step=1])
# 生成从start开始，步长为step的整数序列无限迭代器
# for i in itertools.count(3, 2):
#     print(i)
#     if i > 20:
#         break

# cycle(iterable)
# 将可迭代对象中的元素无限重复
# for i in itertools.cycle('ABC'):
#     print(i)

# repeat(elem, [,n])
# 将一个元素重复n遍或无穷遍，兵返回一个迭代器
# for i in itertools.repeat('abcd', 5):
#     print(i)


# 组合迭代器
# product(*iterable, repeat=1)
# 得到可迭代对象的笛卡尔积, repeat为可迭代序列的重复次数
for i in itertools.product(['A', 'B', 'C'], ['D', 'E', 'F']):
    print(i)

# permutations(iterable, r=None)
# 返回可迭代对象中元素的排列，按序返回且不包含重复
for i in itertools.permutations('abc'):
    print(i)

# combinations(iterable, r)
# 返回可迭代对象元素中所有长度为r的元素组合
for i in itertools.combinations('1234', 2):
    print(i)

# combinations_with_replacement(iterable, r)
# 返回一个可与自身重复的元素组合
for i in itertools.combinations_with_replacement('1234', 2):
    print(i)

# 有限迭代器
# chain(*iterable)
# 将多个迭代对象组合成一个更大的迭代器
for i in itertools.chain('hello', 'world'):
    print(i)

# groupby(iterable, key=None)
# 将相邻元素按key函数分组，返回相应的key和group。key为None时只有相同元素才能放在一组
for key, group in itertools.groupby('AbbCCCAAb'):
    print(key, list(group))

for key, group in itertools.groupby('AaBbBCCcDd', lambda x: x.upper()):
    print(key, list(group))

# accumulate(iterable, [, func])
# 生成一个由指定二元函数对指定迭代器中的元素进行累计计算生成的迭代器，默认二元函数为求和函数
for i in itertools.accumulate([j for j in range(0, 10)]):
    print(i)

for i in itertools.accumulate('Hello!', lambda x, y: x + y):
    print(i)
