segments = '1,2,3'

# 返回数组
print(segments.split(','))
# 数组的每一项，转换成int
map1 = map(int, segments.split(','))

print(map1)
print(type(map1))

for item in map1:
    print(item)
