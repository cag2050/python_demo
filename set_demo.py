# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set1 = set()

list1 = [1, 1, 2, 3]

set1 = {item for item in list1}

print(set1)
