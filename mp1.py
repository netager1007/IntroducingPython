import multiprocessing
import time
import os

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s. Honk!" % (num, stop))
        time.sleep(1)

if __name__== '__main__':
    whoami('main')
#    p = multiprocessing.Process(target=loopy, args=('loopy',))
#    p.start()
#    time.sleep(5)
#    p.terminate()

# 10.4.1 datetime 모듈
# date : 년, 월, 일
# time : 시, 분, 초 마이크로초
# datetime : 날짜와 시간
# timedelta: 날짜와/또는 시간 간격
from datetime import date
halloween = date(2015, 10, 31)
print(halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())  # iso 8601 참고.

# today()
from datetime import date
now = date.today()
print(now)

# timedelta
from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)
print(now + 17*one_day)
# print(now+17)    # Error Occured, because 17 is not day
yesterday = now - one_day
print(yesterday)

# 날짜의 범위 : date.min(year=1, month=1, day=1) ~ date.max(year=9999, month=12, day=31)
# 결과적으로 역사적 혹은 천문학적인 날짜는 계산할 수 없음.

# time 객체는 하루의 시간을 나타내는 데 사용
from datetime import time
noon = time(12, 0, 0)
print(noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)

# datetime 객체는 날짜와 시간을 모두 포함
from datetime import datetime
some_day = datetime(2015, 1, 2, 3, 4, 5, 6)
print(some_day)
print(some_day.isoformat())

# datetime 객체에서 now() 메서드로 현재 날짜와 시간을 얻을 수 있음.
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# combine() : date 객체와 time 객체를 datetime 객체로 병합
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)

print(noon_today.date())
print(noon_today.time())

# 10.4.2 time 모듈
# 파이썬에서 datetime 모듈의 time 객체와 별도의 time 모듈이 있어 혼란스러움.
# time 모듈에는 time() 함수가 있음.
# 절대 시간을 나타내는 한가지 방법은 어떤 시작점 이후 시간의 초를 세는 것.
# 유닉스 시간은 1970년 1월 1일 자정 이후 시간의 초를 사용. 이 값을 에포치(epoch) 라고 함.

# time 모듈의 time() 함수는 현재 시간을 에포치값으로 반환
import time
now = time.time()
print(now)

# ctime() : 에포치값을 문자열로 변환
print(time.ctime(now))

# 에포치값은 자바스크립트와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한
# 최소 공통분모 임.

# localtime() : 시스템의 표준시간대
# gmtime()    : UTC (이전에는 그리니치 시간 또는 줄루 시간)
import time
now = time.time()
print('now: ', now, 'time.localtime(now): ', time.localtime(now))
print('now: ', now, 'time.gmtime(now): ', time.gmtime(now))

# mktime() : struct_time 객체를 에포치 초로 반환
import time
now = time.time()   # 에포치 반환
tm = time.localtime(now)
print(time.mktime(tm))  # now()의 에포치 값과 일치하지 않음. struct_time 객체는
                        # 시간을 초까지만 유지.

# 가능하면 표준시간대 대신 UTC를 사용. UTC는 표준시간대와 독립적인 절대시간임.
# 서버를 운영한다면 현지 시간이 아닌 UTC를 설정하라.

# 10.4.3 날짜와 시간 읽고 쓰기
