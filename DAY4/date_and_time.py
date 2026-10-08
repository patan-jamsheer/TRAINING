import datetime 
# print(datetime.datetime.now())
# today=datetime.date.today()
# print(datetime.date.today())
# print(today.day)
# print(today.month)
# print(today.year)

dob=datetime.date(2006,1,7)
age=datetime.date.today()-dob
print(age//365,(age//365)%30)


