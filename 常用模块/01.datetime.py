# _*_ coding: utf-8 _*_
# @Time: 2022/10/10 15:50
# @Author: lemon
# @File: 01.datetime
# @Project: learning
from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(now)

# 获取指定日期时间 年月日时分秒
date = datetime(2020, 2, 21, 12, 20)
print(date)

# datetime转timestamp, 整数位表示秒数
print(date.timestamp())

# timestamp转datetime
print(datetime.fromtimestamp(1493462588))

# str转datetime
date = date.strptime('2020-02-20 12:21:32', '%Y-%m-%d %H:%M:%S')

# datetime转str
print(date.strftime('%Y/%m/%d'))

# datetime计算
now = datetime.now()
# 20天后
print(now + timedelta(days=20))
# 3天11小时前
print(now - timedelta(days=3, hours=11))
