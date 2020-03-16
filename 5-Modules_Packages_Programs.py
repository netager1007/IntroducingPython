
# Module Search Path
# ------------------
# The first match will be used.
import sys
print('Program arguments:', sys.argv)
for place in sys.path:
    print('[Python Search Path]:', place)


# Packages
# --------
# You can organize modules into file hierarchies called packages.
#
# Show boxes/weather.py

# The Python Standard Library


# The Python Standard Library
# ---------------------------

# setdefault()
# defaultdict()
# handle Missing Keys with setdefault() and defaultdict()
# -------------------------------------------------------
periodic_table = {'Hydrogen':1, 'Helium':2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
periodic_table.setdefault('Lee', 13)
periodic_table.setdefault('Lee', 15)
print(carbon)
print(type(carbon))
print(periodic_table)

from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 11
periodic_table['SLee']
print(periodic_table)

from collections import defaultdict
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])


# Using int is one way to make your own counter:
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

print(food_counter)
print(type(food_counter))
for food, count in food_counter.items():
    print(food, count)

dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1
for food, count in dict_counter.items():
    print(food, count)

# Counter()
# --------------------------
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam', 'can','can','can','can','a','a','aa','bb','bb']
breakfast_counter = Counter(breakfast)
print('Breakfast Counter:', breakfast_counter)
print(type(breakfast_counter))

# most_common() function in Counter Class
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))
print(breakfast_counter.most_common(2))
print(breakfast_counter.most_common(3))

# Combine counters
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print('Breakfast Counter:', breakfast_counter)
print('Lunch Counter:', lunch_counter)

print('+ :', breakfast_counter + lunch_counter)
print('- :', breakfast_counter - lunch_counter)
print('& :', breakfast_counter & lunch_counter)
print('| :', breakfast_counter | lunch_counter)


# Order by Key with OrderDict()
# -----------------------------
quotes = {}
