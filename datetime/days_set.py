import datetime

today = datetime.date.today()

days_set = set()

for i in range(29):
    # print(str(today - datetime.timedelta(days=i)))
    days_set.add(str(today - datetime.timedelta(days=i)))

print(days_set)

print('2020-12-23' in days_set)




