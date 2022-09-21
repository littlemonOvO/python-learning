# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 14:19
# @Author: lemon
# @File: 基础
# @Project: learning
"""
1. 类是创建实例的模板,实例则是具体的对象,各实例拥有的数据互相独立,互不影响;
2. 和静态语言不同,Python允许对实例变量绑定任何数据
"""
"""
访问限制:
    __attr: 属性名称前添加双下划线代表私有属性,外部无法直接访问
    __attr__: 属性名称前后都有双下划线的是特殊变量,可以直接访问
    _attr: 属性名称前有单下划线,代表这个变量可以被访问,但按照约定应视作私有属性不要随意访问
"""
"""

"""


class Student(object):
    pass


stud1 = Student()
stud2 = Student()
stud1.name = 'Abc'
print(stud1.name)
# print(stud2.name)  AttributeError: 'Student' object has no attribute 'name'


"""
    类属性:
        归类本身所有的属性,通过【类名.属性名】访问，所有的类实例都可以访问
    实例属性:
        各实例私有的属性
"""


class Student:
    # 类属性, 记录实例数量
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')
