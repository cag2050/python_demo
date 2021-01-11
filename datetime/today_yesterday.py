import datetime

today = datetime.date.today()
print("today: %s " % today)

yesterday = today - datetime.timedelta(days=1)
print("yesterday: %s" % yesterday)