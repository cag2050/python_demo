set1 = {'111', '222'}

set2 = {'111', '222', '333'}

set3 = {'444'}

# print(set1)
# print(set2)
# 集合中,都包含的元素
print(set1 & set2)
# 集合中,包含的所有元素
print(set1 | set2)

set3 |= set2
print(set3)