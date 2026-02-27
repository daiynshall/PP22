from datetime import date, timedelta

today = date.today()
five_days_ago = today - timedelta(days=5)

print("Today:", today)
print("Five days ago:", five_days_ago)


#place 

from datetime import date, timedelta

today = date.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#place

from datetime import datetime

now = datetime.now()
without_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", without_microseconds)

#place

from datetime import datetime

date1 = datetime(2025, 1, 1, 10, 0, 0)
date2 = datetime(2025, 1, 2, 12, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)