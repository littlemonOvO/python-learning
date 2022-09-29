# _*_ coding: utf-8 _*_
# @Time: 2022/9/29 14:19
# @Author: lemon
# @File: 使用metaclass编写ORM框架
# @Project: learning

"""
orm使用示例：
    class User(Model):
        id = IntegerField('id')
        name = StringField('username')
        email = StringField('email')
        password = StringFiled('password')

    user = User(id=1, name='John', email='test@orm.org', password='123456')
    user.save()

    其中,Model和字段类~Field由orm框架提供,save()等魔术方法由父类Model自动完成
"""


# 定义Field类
class Field:
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.name}>'


# 定义各类型Field子类
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(255)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 定义ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print(f'Found model: {name}')
        # 保存属性和列的映射关系
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print(f'Found mapping: {k} ==> {v}')
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


# 使用ModelMetaclass定义Model类
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f'"Model" object has no attribute {key}')

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = f"insert into {self.__table__} ({','.join(fields)}) values ({','.join(params)})"
        print(f'SQL: {sql}')
        print(f'ARGS: {str(args)}')


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


user = User(id=1, name='John', email='test@orm.org', password='123456')
user.save()
