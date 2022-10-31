# _*_ coding: utf-8 _*_
# @Time: 2022/10/31 13:51
# @Author: lemon
# @File: 03.base64
# @Project: learning
import base64

"""
base64编码：
    1. 准备一个包含64个字符的数组
        ['A', 'B', 'C', ..., 'a', 'b', 'c', ..., '0', '1', ..., '+', '/']
    2. 对原始二进制数据进行分组，每3个byte一组，一共 3x8=24 bit，划分为4组，每组6个bit，可以表示 2^6=64 个二进制数字
    3. 将每一组的6个bit视作二进制数字得到0~63的索引值，在字符数组中找到对应的字符，每3个字节数据得到一个4个字符的字符串作为编码
    4. 编码二进制数据长度不是3的倍数时，用\x00字节在末尾补足，再在编码末尾加上相应数量的=号表示补字节数量，解码时自动去掉
    
    Base64编码将每3字节的二进制数据编码为4字节的文本数据，长度增加了33%.
"""

# base64编码
encode_str = base64.b64encode(b'binary\x00string')
print(encode_str)
# base64解码
decode_str = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(decode_str)
# +和/无法作为url参数，因此将+和/分别变成-和_的编码方法为urlsafe编码
str = b'abcd++//'
encode_str = base64.urlsafe_b64encode(str)
print(encode_str)
decode_str = base64.urlsafe_b64decode(b'YWJjZCsrLy8=')
print(decode_str)
