# itertools.chain()

import itertools

for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

for item in ([1, 2], ['a', 'b']):
    print(item)

# itertools.cycle()
cnt = 0
for item in itertools.cycle([1, 2]):
    cnt += 1
    print(cnt, item)
    if cnt > 9:
        break

# itertools.accumulate() ~ 누적 Sum
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)