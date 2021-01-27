str1 = '1,2,3'
shrink = 1
# 字符串转成list
list1 = str1.split(',')
print(list1)
# 列表截取
print(','.join(list1[0: len(list1) - shrink]))


