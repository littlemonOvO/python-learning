# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 10:31
# @Author: lemon
# @File: 闭包
# @Project: learning

"""
    闭包:
        1. 有函数的嵌套（外函数包裹着内函数）
        2. 内函数引用了外函数中的变量
        3. 外函数的返回值是内函数的引用
"""


# 闭包函数示例
def outer():
    x = 1

    def inner():
        y = x + 1
        print(y)

    return inner


f = outer()
f()  # 2

"""
Python是动态语言，变量使用前不需要先声明，对变量赋值时自动创建变量。
在下述代码中,程序运行到子函数funcY中时，执行语句x = x + 2,
    首先创建局部变量x,覆盖了父函数里的x;
    此时子函数中的x尚未被赋值，所以无法进行运算。
"""


def funcX():
    x = 2

    def funcY():
        # 指定x为非局部变量,在对x进行写操作时不再创建局部变量x
        nonlocal x
        # 不指定x为非局部变量时,下一行代码将报错:x为未解析的引用
        x = x + 2
        return x

    return funcY


f = funcX()
print(f())  # 4


# 小例
def inc():
    x = 0

    def fn():
        nonlocal x
        x = x + 1
        return x

    return fn


f = inc()
print(f())  # 1
print(f())  # 2
print(f())  # 3

"""
闭包中被内部函数引用的变量不会因为外部函数return而被释放掉，而是存在内存中直到内部函数被调用结束.
    在上述代码中,f指向了函数fn,fn内的x为非局部变量,因此不会因外函数inc返回而被释放,累加操作有效.
"""
