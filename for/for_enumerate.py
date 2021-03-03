list1 = ['a', 'b', 'c']

# 方式1：加变量
index = 0
for item in list1:
    index += 1
    print(index)

# 方式2：enumerate()
for i, item in enumerate(list1):
    print('%d\t%s' % (i, item))
