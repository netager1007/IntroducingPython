# Stack + Queue == deque

def palindrome(word):
    from collections import deque
    dq = deque(word)
    print('len(dq): ', len(dq))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    print('Last Print')
    return True
print(palindrome('aba'))
print(palindrome('a'))

print(palindrome('ab'))


# Python doesn't have a reverse() function for string, but it does have a way to reverse
# a string whit a slice.
def another_palindrome(word):
    return word == word[::-1]
print('another palindrome: ', another_palindrome('radar'))
print('another palindrome: ', another_palindrome('halibut'))


# 코드구조 순회하기 : itertools
# for ... in 루프에서 이터레이터 함수를 호출할 때 함수는 한 번에 한 항목을 반환, 호출상태 기억

# itertools.chain()
import itertools
for item in itertools.chain([1, 2],['a','b']):
    print(item)

# itertools.cycle()
import itertools
num = 0
for item in itertools.cycle([1,2]):
    print(item)
    num += 1
    if num > 2:
        break

# itertools.accumulate()
import itertools
for item in itertools.accumulate([1, 2, 3, 4, 5]):
    print('itertools.accumulate: ', item)

import itertools
for item in itertools.accumulate(range(1, 1001)):
    pass
print('itertools.accumulate: ', item)
print('공식: ', 1001 * 500)

import itertools
def multifly(a, b):
    return a * b

for item in itertools.accumulate([1,2,3,4], multifly):
    print(item)


# Print Nicely with pprint()
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([ \
    ('Moe', 'A wise quy, huh?'), \
    ('Larry', 'Ow!'), \
    ('Curly', 'Nyuk nyuk!'), \
     ])
print(quotes)
pprint(quotes)
