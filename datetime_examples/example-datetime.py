#http://defpython.ru/kak_v_python_poluczit_tekusczuu_datu_i_vremya

import datetime

now = datetime.datetime.now()

print("Текущая дата и время с использованием метода str:")
print(str(now))

print("Текущая дата и время с использованием атрибутов:")
print("Текущий год: %d" % now.year)
print("Текущий месяц: %d"% now.month)
print("Текущий день: %d" % now.day)
print("Текущий час: %d" % now.hour)
print("Текущая минута: %d" % now.minute)
print("Текущая секунда: %d" % now.second)
print("Текущая микросекунда: %d" % now.microsecond)

print("Текущая дата и время с использованием strftime:")
print(now.strftime("%d-%m-%Y %H:%M:%S"))

print("Текущая дата и время с использованием isoformat:")
print(now.isoformat())

# String to datetime
# https://www.journaldev.com/23365/python-string-to-datetime-strptime

from datetime import datetime
import time

datetime_str = '09/19/18 13:55:26'
datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
print(type(datetime_object))
print(datetime_object)  # printed in default format

# strptime() ValueError Example
datetime_str = '09/19/18 13:55:26'

try:
    datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')
except ValueError as ve:
    print('ValueError Raised:', ve)

time_str = '99::55::26'

try:
    time_object = time.strptime(time_str, '%H::%M::%S')
except ValueError as e:
    print('ValueError:', e)

# Convert UTC datetime string to local datetime
# https://stackoverflow.com/questions/4770297/convert-utc-datetime-string-to-local-datetime
from datetime import datetime
from dateutil import tz

# METHOD 1: Hardcode zones:
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
# to_zone = tz.gettz('Europe/Moscow')

# METHOD 2: Auto-detect zones:
from_zone = tz.tzutc()
to_zone = tz.tzlocal()

# utc = datetime.utcnow()
utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since 
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
central = utc.astimezone(to_zone)

# https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime

dt = datetime(2021, 1, 1, 0, 0, 0)
print(dt)

###############################################################################

# ----------------------------------------
# astimezone()
# Return a datetime object with new tzinfo attribute tz,
# adjusting the date and time data so the result is the same UTC time as self,
# but in tz’s local time.
from dateutil import tz
utc_dt = dt.astimezone(tz=tz.UTC)
# as system tz
local_dt = dt.astimezone()
print(dt, utc_dt, local_dt)

# get system local tzinfo
tzinfo = datetime.now().astimezone().tzinfo

# ----------------------------------------
# replace()
import pytz
msc_tz = pytz.timezone('Europe/Moscow')
msc_dt = dt.replace(tzinfo=msc_tz)
print(dt, msc_dt)

