# _*_ coding: utf-8 _*_
# @Time: 2022/9/21 8:52
# @Author: lemon
# @File: 使用@property
# @Project: learning
"""
    @property:
        使类中的方法可以当作属性来使用;
"""


class Student:
    __score = 0

    # 使方法score可以通过Student.score调用
    @property
    def score(self):
        return self.__score

    # 使属性__score可以通过Student.score = value的方式赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer.')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100.')
        self.__score = value

    # 未使用@rank.setter装饰器时,rank为只读属性
    @property
    def rank(self):
        if self.__score < 60:
            return 'D'
        elif self.__score < 80:
            return 'C'
        elif self.__score < 90:
            return 'B'
        else:
            return 'A'


s = Student()
s.score = 90
print(s.score)
print(s.rank)
