import datetime

start_time = '2021-01-26'
end_time = '2021-01-27'

start_time_obj = datetime.datetime.strptime(start_time, "%Y-%m-%d")
end_time_obj = datetime.datetime.strptime(end_time, "%Y-%m-%d")
diff_days = (end_time_obj - start_time_obj).days
# 间隔日期的列表
days_list = []
for i in range(diff_days + 1):
    days_list.append(str(start_time_obj.date() + datetime.timedelta(days=i)))
print(days_list)

hour_list = []
for i in range(24):
    if i < 10:
        hour_list.append('0' + str(i))
    else:
        hour_list.append(str(i))
print(hour_list)

for day_index, day in enumerate(days_list):
    for hour_index, hour in enumerate(hour_list):
        print((day_index + 1) * (hour_index + 1))