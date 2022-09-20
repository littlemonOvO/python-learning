# _*_ coding: utf-8 _*_
# @Time: 2022/9/20 10:58
# @Author: lemon
# @File: 装饰器
# @Project: learning

"""
python装饰器本质上就是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能.
    装饰器的返回值也是一个函数对象（函数的指针）;
    装饰器函数的外部函数传入需要装饰的函数，返回经过修饰后的函数;
    内层函数（闭包）负责修饰被修饰函数。
"""

# 装饰器示例
# 需求: 对函数func进行装饰,在函数执行前后输出执行信息
# 目标函数
import functools


def func(a, b):
    print(f'函数 {func.__name__} 执行中...')
    return a ** b


# 装饰器
# 外层函数,用于接收目标函数,返回被修饰后的新函数
def outer(function):
    # 内层函数,对目标函数进行修饰
    # 接收目标函数的参数
    # @functools.wraps(function)
    def inner(*args, **kwargs):
        print(f'函数 {function.__name__} 执行前...')
        result = function(*args, **kwargs)
        print(f'函数 {function.__name__} 执行后...')
        return result

    return inner


# 使用装饰器
func = outer(func)
# 等价写法:
#   @outer
#   def func()
print('2 ^ 3 = ', func(2, 3))

"""
    由于func指向了outer生成的新函数inner,原func中的函数内部信息改变,输出结果为 函数 inner 执行中...
    @functools.wraps()可将函数内部信息从原函数转移到新函数中
"""

"""
带参数的装饰器
    由于最外层的装饰器需要接收参数,整个装饰器结构须增加一层,即
        最外层:接收参数,返回接收目标函数的装饰器
        中间层:接收目标函数,返回装饰后的新函数
        内层:接收目标函数参数,对目标函数进行装饰
        
    原结构:                                新结构:
        func = outer(func)                    func = outer(param)(func)
                                <=>
        @outer                                @outer(param)
        def func()                            def func()
"""


# 最外层装饰器: 接收参数,返回接收目标函数的装饰器
def outer(param):
    # 中间层: 接收目标函数,返回装饰后的新函数
    def dec(function):
        # 内层: 接收目标函数参数,对目标函数进行装饰
        @functools.wraps(function)
        def inner(*args, **kwargs):
            print(f'传入的参数为: {param}')
            return function(*args, **kwargs)

        return inner

    return dec


# 使用装饰器
# 等价于: func = outer('abc')(func)
@outer('abc')
def func(a, b):
    print(f'函数 {func.__name__} 执行中...')
    return a ** b


print('2 ^ 3 = ', func(2, 3))
