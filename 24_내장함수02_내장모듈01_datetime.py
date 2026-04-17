## Python 기본 내장 모듈
#  https:/docs.python.org/3/py-modindex.html

# datetime
import datetime # import 키워드를 사용해서 모듈을 추가

today = datetime.date.today()
print(today)    # 2026-04-17

now = datetime.datetime.now()
print(now)      # 2026-04-17 10:40:01.731878

print(now.year)     # 2026
print(now.month)    # 3
print(now.day)      # 4

dir(datetime)   #17


##
import datetime as dt # as를 사용해서 별칭을 지정

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

know = now + dt.timedelta(hours=9)
print(know)

time_diff = know - now
print(time_diff)    # 9:00:00


##
from datetime import datetime, date

xmas1 = datetime(2023, 12, 25, 0, 0, 0)
print(xmas1)    # 2023-12-25 00:00:00

xmas2 = date(2023, 12, 15)
print(xmas2)    # 2023-12-15
