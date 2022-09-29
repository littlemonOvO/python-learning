# _*_ coding: utf-8 _*_
# @Time: 2022/9/29 13:38
# @Author: lemon
# @File: 枚举类
# @Project: learning

from enum import Enum, unique

# 定义枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 枚举所有成员
# value为自动赋给成员的int常量,默认从1开始计数
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 直接引用常量
print(Month.Jul)


# 保证没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 通过成员名称引用枚举常量
print(Weekday.Mon)  # Weekday.Mon
print(Weekday['Tue'])  # Weekday.Tue
print(Weekday.Wed.value)  # 3
# 根据value值获取枚举常量
print(Weekday(4))  # Weekday.Wed


# 例
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = Gender(gender)


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
