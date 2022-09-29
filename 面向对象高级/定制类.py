# _*_ coding: utf-8 _*_
# @Time: 2022/9/29 9:54
# @Author: lemon
# @File: 定制类
# @Project: learning

"""
    __str__和__repr__:
        __str__由str(),format(),print()三个方法调用,用于为最终用户创建输出,面向用户;
        __repr__比__str__更加正式,在交互式命令行直接输出对象时使用,用于调试和开发,面向开发者.
"""


class Person:
    def __init__(self, name):
        self.name = name


mark = Person('Mark')
print(mark)  # <__main__.Person object at 0x000001E023CE5188>


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Person object (name: {self.name})'

    # repr是为调试服务的字符串,开发者可见
    __repr__ = __str__


mark = Person('Mark')
print(mark)  # Person object (name: Mark)

"""
    __iter__和__next__:
        __iter__()方法返回一个迭代对象,for循环会不断调用此对象的__next__()方法拿到循环的下一个值,直到遇到 StopIteration 退出循环.
"""


# 斐波那契数列类
class Fib:
    def __init__(self):
        # 数列初始元素
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)

"""
    __getitem__:
        使对象能和列表一样使用下标索引和切片操作
    __setitem__:
        使对象能被视作列表或字典来对集合进行赋值
"""


class Fib:
    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for _ in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            result = []
            for i in range(stop):
                if i >= start:
                    result.append(a)
                a, b = b, a + b
            return result


f = Fib()
print(f[0])
print(f[10])
print(f[1:5])

"""
    __getattr__:
        在调用类中不存在的属性或方法时,python解释器会视图调用__getattr__(self, 'attr_name')来获取属性
"""


# 例: rest api的url链式调用
class Chain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __str__(self):
        return self._path

    __repr__ = __str__


c = Chain()
print(c.status.user.timeline.list)  # /status/user/timeline/list

"""
__call__:
    使【实例对象】能像函数一样被直接调用
callable():
    判断一个对象是否使可调用对象
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f'My name is {self.name}')


mark = Person('Mark')
mark()  # My name is Mark

"""
    带参数的链式api实例
"""


class Chain:
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain(f'{self._path}/{path}')

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self, *args, **kwargs):
        if args is not None:
            i = self._path.rfind('/')
            self._path = self._path[:i + 1] + args[0]
        return self


c = Chain()
print(c.user('michael').repos)  # /michael/repos
