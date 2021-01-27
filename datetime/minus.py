# 计算两个日期相差的天数
import datetime

end_time = datetime.datetime.strptime('2021-01-27', "%Y-%m-%d")
start_time = datetime.datetime.strptime('2021-01-25', "%Y-%m-%d")
num = (end_time - start_time).days
print(num)
