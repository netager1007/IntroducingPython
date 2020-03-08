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
print('now(epoch: time.time()): ', now)

# ctime() : 에포치값을 문자열로 변환
print('time.ctime(now): ', time.ctime(now))

# 에포치값은 자바스크립트와 같은 다른 시스템에서 날짜와 시간을 교환하기 위한 유용한
# 최소 공통분모 임.

# localtime() : 시스템의 표준시간대
# gmtime()    : UTC (이전에는 그리니치 시간 또는 줄루 시간)
import time
now = time.time()
print('now(epoch: time.time()): ', now, 'time.localtime(now): ', time.localtime(now))
print('now(epoch: time.time()): ', now, 'time.gmtime(now): ', time.gmtime(now))

# mktime() : struct_time 객체를 에포치 초로 반환
import time
now = time.time()   # 에포치 반환
print('now(epoch: time.time()): ', now)
tm = time.localtime(now)
print('tm(time.localtime(now)): ', tm)
print('time.mktime(tm): ', time.mktime(tm))  # now()의 에포치 값과 일치하지 않음. struct_time 객체는
                                             # 시간을 초까지만 유지.

# 가능하면 표준시간대 대신 UTC를 사용. UTC는 표준시간대와 독립적인 절대시간임.
# 서버를 운영한다면 현지 시간이 아닌 UTC를 설정하라.

# 10.4.3 날짜와 시간 읽고 쓰기
import time
now = time.time()
print('now(epoch: time.time()): ', now)
print('time.ctime(now): ', time.ctime(now))
print('')


# strftime() : 날짜와 시간을 문자열로 변환
# strftime() 출력 지정자
# 문자열 포맷  : 날자/시간 단위   : 범위
# %Y          : 년              : 1900 ~
# %m          : 월              : 01 ~ 12
# %B          : 월 이름         : January,
# %b          : 월 축약 이름     : Jan,
# %d          : 월의 일자       : 1 ~ 31
# %A          : 요일 이름       : Sunday,
# %a          : 요일 축약 이름  : Sun,
# %H          : 24시간         : 00 ~ 23
# %I          : 12시간         : 01 ~ 12
# %p          : 오전/오후      : AM, PM
# %M          : 분            : 00 ~ 59
# %S          : 초            : 00 ~ 59

import time
fmt = "It's %A, %B %d, %Y, localtime %I:%M:%S %p"
t = time.localtime()
print('t(time.localtime()): ', t)
t1 = time.gmtime()
print('t1(time.gmtime()): ', t1)
print('time.strftime(fmt, t): ', time.strftime(fmt, t))
print("time.strftime('%Y-%m-%d %H-%M-%S', t1): ", time.strftime('%Y-%m-%d %I-%M-%S', t1))
print('')

# date 객체에 사용하면 날짜 부분만 작동. 시간은 기본값으로 지정됨. 현재 시간이 아님.
from datetime import date
some_day = date(2015, 12, 12)
fmt = "It's %B %d, %Y, local time %I:%M:%S %p"
print('some_day.strftime(fmt): ', some_day.strftime(fmt))

# time 객체는 시간 부분만 변환
from datetime import time
some_time = time(10, 25)
fmt = "It's %B %d, %Y, local time %I:%M:%S %p"
print('some_time.strftime(fmt): ', some_time.strftime(fmt))

# strptime() : 문자열을 날짜나 시간으로 변환
import time
fmt = "%Y-%m-%d"
try:
    time.strptime("2015 06 02", fmt)
except ValueError as e:
    print("Error Occured: ", e)

print('time.strptime("2015-06-02", fmt): ', time.strptime("2015-06-02", fmt))   # 대시(-)를 붙임

# 값의 범위를 넘어가는 경우 예외 발생
import time
fmt = "%Y-%m-%d"
try:
    time.strptime("2015-13-29", fmt)
except ValueError as e:
    print('Error Occured: ', e)

# 이름은 운영체제의 국제화 설정인 로케일(locale)에 따름. 다른 월, 일의 이름을 출력하려면 setlocale() 사용.
# setlocale()의 첫 인자는 날짜와 시간을 위한 locale.LC_TIME이고, 두번째는 언어와 국가 약어가 결합된 문자열.
import locale
from datetime import date
halloween = date(2015, 10, 31)
for lang_country in ['ko_kr', 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    print('lang_country: ', lang_country, ', halloween.strftime("%A, %B %d"): ', halloween.strftime('%A, %B %d'))
# lang_country 찾는 방법
# "ko_ko" : "두 글자의 언어코드_두 글자의 국가 코드
import locale
names = locale.locale_alias.keys()
#print('names: ', names)
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print('good_name[0:5]: ', good_names[0:5])
de = [name for name in names if name.startswith('de')]
print(de)
ko = [name for name in names if name.startswith('ko')]
print(ko)


# 10.4.4 대체 모듈
# arrow : 많은 날짜와 시간 함수를 결합하여 간단한 API를 제공
# dateutil : 대부분의 날짜 포맷을 파싱하고, 상대적인 날짜와 시간에 대해서 처리
# iso8601 : ISO8601 포맷에 대한 표준 라이브러리의 부족한 부분을 보충
# fleming : 표준시간대 함수를 제공

