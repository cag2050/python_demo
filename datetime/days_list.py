import datetime

today = datetime.date.today()

days_list = []

for i in range(6):
    # print(str(today - datetime.timedelta(days=i)))
    days_list.append(str(today + datetime.timedelta(days=i)))

print(days_list)

print('2020-12-23' in days_list)




