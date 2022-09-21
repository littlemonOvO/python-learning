# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 15:23
# @Author: lemon
# @File: 使用__slots__
# @Project: learning
from types import MethodType

"""
动态语言特性:可以动态地给类或实例绑定属性和方法
"""


class Student:
    pass


# 给实例绑定属性
s = Student()
s.name = 'ABC'
print(s.name)


# 给实例绑定方法
def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(18)
print(s.age)


# 给class绑定方法
def set_gender(self, gender):
    self.gender = gender


Student.set_gender = set_gender
s.set_gender('female')
print(s.gender)

"""
__slots__：
    用来限制class实例能添加的属性;
    仅对当前类实例起作用,对继承的子类无效;
    子类定义了__slot__属性时,其允许定义的属性为子类__slot__与父类__slot__的并集;
"""


class Person:
    # 允许定义的属性为('name', 'age')
    __slots__ = ('name', 'age')


class Programmer(Person):
    # 允许定义的属性为('name', 'age', 'sex')
    __slots__ = ('sex',)


class Leader(Person):
    # 允许定义的属性无限制
    pass
