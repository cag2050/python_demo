# 计算两个日期相差的天数
import datetime

start_time_str = '2021-01-28'
end_time_str = '2021-02-3'
start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d")
end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d")
diff_days = (end_time - start_time).days
print(diff_days)

# 间隔日期的列表
days_list = []
# + 1: 包含最后一天
for i in range(diff_days + 1):
    # print(str(today - datetime.timedelta(days=i)))
    days_list.append(str(start_time.date() + datetime.timedelta(days=i)))
print(days_list)
