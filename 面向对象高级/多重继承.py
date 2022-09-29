# _*_ coding: utf-8 _*_
# @Time: 2022/9/29 9:39
# @Author: lemon
# @File: 多重继承
# @Project: learning

"""
    Python 允许多重继承,一个类可以继承多个父类,并获得父类的非私有方法和属性
"""


# 动物类
class Animal:
    pass


# 哺乳动物子类
class Mammal(Animal):
    pass


# 鸟类子类
class Bird(Animal):
    pass


# 可行走类
class RunnableMixIn:
    def run(self):
        print(f'{self.__class__.__name__} is Running...')


# 可飞行类
class FlyableMixIn:
    def run(self):
        print(f'{self.__class__.__name__} is Flying...')


# 狗是哺乳动物,可行走
class Dog(Mammal, RunnableMixIn):
    pass


# 蝙蝠是哺乳动物,可飞行
class Bat(Mammal, FlyableMixIn):
    pass


dog = Dog()
bat = Bat()
dog.run()
bat.run()

"""
    MixIn:
        需要给一个类增加额外功能时,优先考虑通过多重继承来组合多个MixIn的功能,而不是设计多层次的复杂继承关系.
"""
