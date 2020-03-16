periodic_table = {'Hydrogen':1, 'Helium':2}

print(periodic_table)

carbon = periodic_table.setdefault('Carbon',12)
print(periodic_table)
print(periodic_table['Hydrogen'])
print(periodic_table['Helium'])
print(periodic_table['Carbon'])

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
periodic_table['Lead']
print(periodic_table)

periodic_table['Abc']
print(periodic_table)

def no_idea():
    return 'Huh?'

besitary = defaultdict(no_idea)
besitary['A'] = 'Abominable Snowman'
besitary['B'] = 'Basilisk'
print(besitary['A'])
print(besitary['B'])
print(besitary['C'])

besitary = defaultdict(lambda:"What?")
print(besitary['A'])
print(besitary['B'])
print(besitary['C'])


# Counter 만들기
from collections import defaultdict

food_counter = defaultdict(int)
for food in ['spam', 'spam', 'egg', 'spam', 'apple', 'orange', 'apple', 'orange', 'pig']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
print(food_counter)

dict_counter = {}
for food in ['spam', 'spam', 'egg', 'spam', 'apple', 'orange', 'apple', 'orange', 'pig']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
print(dict_counter)

# 항목세기 : Counter()
from collections import Counter
breakfast = ['orange', 'spam', 'egg', 'spam', 'apple', 'orange', 'apple', 'orange', 'pig', 'egg']
breakfast_counter = Counter(breakfast)

print('Breakfast Counter:', breakfast_counter)


# most_common() : 모든 요소를 내림차순으로 반환 ~ Values를 기준으로 내림차순
print(breakfast_counter.most_common())

lunch = ['egg', 'egg', 'bacon']
lunch_counter = Counter(lunch)
print('Lunch Counter:', lunch_counter)
print('Breakfast Counter:', breakfast_counter)

print('Lunch Counter + Breakfast Counter:', lunch_counter + breakfast_counter)
print('Lunch Counter - Breakfast Counter:', lunch_counter - breakfast_counter)
print('Breakfast Counter - Lunch Counter:', breakfast_counter - lunch_counter)

print('Lunch & Breakfast:', lunch_counter & breakfast_counter)


# OrderdDict() : 키정렬하기, 키가 추가된 순서를 기억하고 이터레이터로부터 순서대로 키 반환
from collections import OrderedDict

quotes = OrderedDict({('Moe', 'A wise guy, huh?'),
    ('Larry', 'Owl'),
    ('Curly', 'Nyuk nyuk')})
print(quotes)
for stooge in quotes:
    print(stooge)