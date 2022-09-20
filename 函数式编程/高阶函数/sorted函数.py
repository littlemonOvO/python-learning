# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 10:26
# @Author: lemon
# @File: sorted函数
# @Project: learning

"""
sorted(Iterable, key=func):
    将key指定的函数作用在序列的每一个元素上,根据函数返回结果进行排序
"""

# 按绝对值排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 根据分数降序排列
persons = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(persons, key=lambda x: x[1], reverse=True))
