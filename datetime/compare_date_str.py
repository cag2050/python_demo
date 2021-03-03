import datetime

date1 = "2017-06-07"
date2 = "2017-06-09"
# 注意在转换过程中date1和date2必须是str类型！！
date1 = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
date2 = datetime.datetime.strptime(date2, '%Y-%m-%d').date()

date3 = date1 - datetime.timedelta(days=1)
print(date1)
print(str(date1) == '2017-06-07')
print(date2)
print(type(date2))
print(date1 >= date2)
print(date1 <= date2)
print(date3)
print(type(str(date3)))
