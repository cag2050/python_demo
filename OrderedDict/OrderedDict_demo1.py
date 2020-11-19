from collections import OrderedDict

USERS = [
    ('bbb', b'444=='),
    ('aaa', b'111='),
]
print(USERS)
print(type(USERS))

d = OrderedDict(USERS)
print(type(d))
print(d)
print(d.get('bbb'))
