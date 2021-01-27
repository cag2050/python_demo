# 字符串类型str转换为dateTime类型
import datetime

str_p = '2019-01-30'
date_p = datetime.datetime.strptime(str_p, '%Y-%m-%d').date()
print(date_p, type(date_p))  # 2019-01-30 <class 'datetime.date'>


