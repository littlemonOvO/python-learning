# _*_ coding: utf-8 _*_
# @Time: 2022/9/29 13:53
# @Author: lemon
# @File: 元类
# @Project: learning


"""
    使用type()创建class对象
    type()接收三个参数:
        1. class的名称
        2. 继承的父类元组集合
        3. class的方法名和函数绑定关系
    用type()创建的类和直接写class完全一样,python解释器遇到class定义时仍调用type()方法创建class
"""


def func(self, name='world'):
    print(f'Hello, {name}.')


Hello = type('Hello', (object,), dict(hello=func))
h = Hello()
h.hello()  # Hello, world.

"""
    使用metaclass创建类
        metaclass允许创建类或修改类,可以把类看作是metaclass创建出来的实例
"""


# 例:使用metaclass给自定义的MyList添加一个add()方法
# 1. 定义ListMetaclass 按习惯metaclass的类名以Metaclass结尾
class ListMetaclass(type):
    # 创建类的入口,在此可以修改类的定义并返回
    # cls: 准备创建类的对象; name: 类的名字; bases:类继承的父类集合; attr:类的方法集合
    def __new__(cls, name, bases, attrs):
        # 添加add()方法
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 2. 定义MyList
# 告诉python解释器,在创建MyList时要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass


# 3. 创建MyList实例并调用add()方法
li = MyList()
li.add('AAA')
print(li)  # ['AAA']
