import datetime
reportLifecycle = 17
eventEndDate = datetime.date(2022, 2, 28)



#print(str((datetime.date.today()) + datetime.timedelta(days=reportLifecycle) + datetime.timedelta(eventEndDate - datetime.date.today())))

today = datetime.datetime.today()

date = datetime.date.today()
date2 = datetime.timedelta(days=reportLifecycle)
date4 = (eventEndDate - datetime.date.today()).days
date3 = datetime.timedelta(days = date4)

test1 = date + date2
print(test1.strftime("%Y-%m-%d"))
