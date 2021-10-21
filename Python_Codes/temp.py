import datetime
from dateutil.parser import parse
from dateutil.tz import gettz
tzinfos = {"IST": "Asia/Kolkata" }
print(parse("October 21, 2021 04:53 PM IST", tzinfos=tzinfos))



format = '%b %d %Y %I:%M%p'
date_time="Dec 4 2018 10:07AM"
x=datetime.datetime.strptime(date_time, format)

print(x)