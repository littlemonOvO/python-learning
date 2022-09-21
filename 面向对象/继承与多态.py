# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 14:41
# @Author: lemon
# @File: 继承与多态
# @Project: learning


class Animal:
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


class Hen(Animal):
    pass


dog = Dog()
cat = Cat()
hen = Hen()
dog.run()
cat.run()
hen.run()

print(isinstance(dog, Animal))

"""
继承: 子类获得父类的全部功能,子类同时也视为父类类型
    上述代码中,类Hen继承了类Animal,获得了方法run()
多态: 
    对外部而言,外部只需知道一个实例是Animal类型即可调用run()方法,而具体实现逻辑无需关心;
    对内部而言,Animal可以扩展任意多子类并重写run()方法,其实现逻辑对外部封闭;

对于静态语言来说,如果需要传入Animal类型,传入对象必须是Animal类及其子类才能调用run()方法;
对Python这样的动态语言来说,只需要保证传入对象实现了run()方法即可。

一些内置函数:
    dir(obj):
        获得一个对象的所有属性和方法
        返回一个包含字符串的list,内容为对象的属性和方法名称
    obj.__len__():
        返回长度
        len(obj) <=> obj.__len__()
    hasattr(obj, attr:str):
        检查一个对象是否有属性attr
    getattr(obj, attr:str, default_value):
        获得一个对象的attr属性值,属性不存在时返回默认值
    setattr(obj, attr:str, value):
        向一个对象设置attr属性值
"""
