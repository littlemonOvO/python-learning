# _*_ coding: utf-8 _*_
# @Time: 2022/10/10 16:11
# @Author: lemon
# @File: 02.collections
# @Project: learning
from collections import namedtuple

# namedtuple
# 定义一个坐标对象
# 创建自定义tuple对象，规定tuple元素个数，使用属性索引
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)

# deque: 实现高效插入和删除操作的双向列表,适合队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.appendleft('w')
q.pop()
print(q)

# defaultdict:dict的key不存在时返回默认值
from collections import defaultdict

d = defaultdict(lambda: 'Nothing')
d['name'] = 'abc'
print(d['name'])
print(d['age'])

# OrderedDict: 有序dict
from collections import OrderedDict

od = OrderedDict()
od['z'], od['y'], od['x'] = 1, 2, 3
# 按插入的顺序而不是对key本身排序
print(list(od.keys()))

"""
ChainMap
    ChainMap 可以将多个字典合并为一个独有的字典，这样的操作不是对源数据的拷贝，而是指向源数据。
    假如原字典数据修改，ChainMap 映射也会改变；如果对 ChainMap 的结果修改，那么原数据一样也会被修改。
"""
from collections import ChainMap

dict1 = {"a": "zhangsan", "b": "lisi"}
dict2 = {"c": "wangwu"}
dict3 = {"d": "liqui", "e": "laowang"}
cm = ChainMap(dict1, dict2, dict3)
print(cm)
# 遍历
for key, value in cm.items():
    print(f'{key}: {value}')
# 修改
cm.maps[0]['a'] = 'abc'
print(cm.maps[0])
