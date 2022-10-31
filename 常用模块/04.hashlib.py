# _*_ coding: utf-8 _*_
# @Time: 2022/10/31 14:09
# @Author: lemon
# @File: 04.hashlib
# @Project: learning
import hashlib
import hmac

# md5摘要算法
message = b'Hello world'
encrypy_str = hashlib.md5(message).hexdigest()
print(encrypy_str)

# md5加盐
salt = b'+Salt'
encrypy_str = hashlib.md5(message + salt).hexdigest()
print(encrypy_str)

# hmac: 为每一个待加密数据随机生成salt作为key，再进行md5加密
key = b'secret'
encrypy_str = hmac.new(key, message, digestmod='MD5').hexdigest()
print(encrypy_str)
