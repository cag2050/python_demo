class Object1(object):
    attr_1 = 'attr_1_value'


object1 = Object1()
# getattr() 函数用于返回一个对象属性值。
print(getattr(object1, 'attr_1'))
