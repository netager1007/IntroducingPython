import re
result = re.match('You', 'young Frank')
print(result)

you_pattern = re.compile('You')

result0 = you_pattern.match('Young Frank')
print('result0: ', result0)

result1 = you_pattern.match('abYoung Frank')
print('result1: ', result1)

result2 = you_pattern.search('Young Frank')
print(result2)

result3 = you_pattern.findall('Young FrankYour')
print(result3)

result4 = you_pattern.split('abYoung FrankYour')
print(result4)


# match() : 시작붜 일치하는 패턴 찾기

source = 'Young Frankenstein '
m = re.match('You', source)
if m:
    print('first: ', m.group())
m = re.match('^You', source)
if m:
    print('second: ', m.group())
m = re.match('Frank', source)
if m:
    print('third: ', m.group())
m = re.match('.*Frank', source)
if m:
    print('fourth: ', m.group())

# search() : 첫번째 일치하는 패턴 찾기
m = re.search('Frank', source)
if m:
    print('first search(): ', m.group())

# findall() : 일치하는 모든 패턴 찾기
m = re.findall('n', source)
if m:
    print('Found', len(m), 'matches: ', m)

m = re.findall('n.', source)
if m:
    print('Found', len(m), 'matches: ', m)
