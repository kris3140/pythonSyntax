from time import time, ctime, sleep
from datetime import datetime,timedelta

# time() = seconds since 01 01 1970
# ctime() = date
# sleep() = wait a number of seconds

x = time()
print(x)             # seconds sinds 01 01 1970

nu = ctime()
print('nu : ', nu)

nu = datetime.now()
print('nu : ', nu)
print()

dt = datetime(2019, 10, 21, 16, 29, 20)    # creating an object
print('dt : ')
print(dt)
print(dt.year, dt.month, dt.day)
print(dt.hour, ':' ,dt.minute, ':'  ,dt.second)
print()
# dt is an object with attributes : year, month, day, hour,...

datum = datetime.fromtimestamp(1630000000)
print('datum : ', datum)
print()

halloween2019 = datetime(2019, 10, 31, 0, 0, 0)
yearend2019 = datetime(2019, 12, 31, 0, 0, 0)
if halloween2019 < yearend2019:
    print('True')
    verschil = yearend2019 - halloween2019
    print('verschil: ', verschil)
    print(type(verschil))
    print('verschil in dagen: ', verschil.days)
    print()

# timedelta = a period of time
delta = timedelta(days=11, hours=10, minutes=9, seconds=8)     # creating an object
print('timedelta = ', delta.days, delta.seconds, delta.microseconds)
print('string timedelta = ', str(delta))
print()
# timedelta() function takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds.
# There is no month or year keyword argument, because “a month” or “a year” is a variable amount of time depending
# on the particular month or year. A timedelta object has the total duration represented in days, seconds, and microseconds.
# These numbers are stored in the days, seconds, and microseconds attributes, respectively. There is no hours or minutes attribute.

today = datetime.now()
print('today :', today)
thousandDays = timedelta(days=1000)
todayPlus = today + thousandDays
print('today + :', todayPlus)