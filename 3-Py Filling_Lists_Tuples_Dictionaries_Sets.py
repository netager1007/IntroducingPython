## Lists

# Create with [] or list()
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
another_empty_list = list()

# Convert Other Data Types to Lists with list()
print(list('cat'))
print(list('cat')[0])
print(list('cat')[1])

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# use split() to chop a string into a list by some separator string:
birthday = '1/6/1952'
print(birthday.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('/'))

splitme = 'a/b//c/d///e'
print(splitme.split('//'))

# Get an Item by Using [offset]
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[-1])

try:
    marxes[5]
except IndexError as e:
    print('[Exception Occured]:', e)

# Lists of Lists
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[0][0])
print(all_birds[1][0])

# Change an Item by [offset]
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
print(marxes)

# Get a Slice to Extract Items by Offset Range
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])

# A slice of a list is also a list.

print(marxes[::2])

# we start at the end and go left by 2:
print(marxes[::-2])

# And finally, the trick to reverse a list:
print(marxes[::-1])

# Add an Item to the End with append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

# Combine Lists by Using extend() or +=
# You can merge one list into another by using extend().
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
print(marxes.extend(others))
print(marxes)
print(others)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)

# If we had used append(), others would have been added as a single
# list item rather than merging its items:
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)     # list 자체를 item으로 추가 됨.
print(marxes)

# Add an Item by Offset with insert()
# The append() function adds items only to the end of the list.
# When you want to add an item before any offset in the list, use insert().
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(3, 'Gummo')
print(marxes)

# An offset beyond the end of the list inserts at the end, like append()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.insert(10, 'Karl')
print(marxes)

# Delete an Item by Offset with del
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
del marxes[-1]
print(marxes)

# When you delete an item by its position in the list, the items that follow
# it move back to take the deleted item’s space, and the list’s length
# decreases by one. If we delete 'Harpo' from the last version of the
# marxes list, we get this as a result:
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(marxes[2])
del marxes[2]
print(marxes)
print(marxes[2])

# del() is a Python statement, not a list method.
# marxes[-2].del()   # SyntaxError Occured


# Delete an Item by Value with remove()
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
print(marxes)

# Get an Item by Offset and Delete It by Using pop()
# You can get an item from a list and delete it from the list at the
# same time by using pop().
# If you call pop() with an offset, it will return the item at that
# offset; with no argument, it uses -1. So, pop(0) returns thehead (start)
# of the list, and pop() or pop(-1) returns the tail (end), as shown here:
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())   # Default : -1
print(marxes)
print(marxes.pop(1))
print(marxes)

# Find an Item's Offset by Value with index()
# If you want to know the offset of an item in a list by its value, use index():
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))   # Return: item's index

# Test for a Value with in
# The Pythonic way to check for the existence of a value in a list is using in:
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)

# The same value may be in more than one position in  the list.
words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)

# Count Occurrences of a Value by Using count()
# To count how many times a particular value occurs in a list, use count():
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
print(marxes.count('Bob'))

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

# Convert to a String with join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(','.join(marxes))
print(type(','.join(marxes)))

# It might help to remember: join() is the opposite of split().
# join() is a string method, not a list method.
friends = ['Harry', 'Hermione', 'Ron']
separator = '*'
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

# Reorder Items with sort()
# You’ll often need to sort the items in a list by their values rather than their offsets.
# Python provides two functions:
# 1. The list function sort() sorts the list itself, in place.
# 2. The general function sorted() returns a sorted copy of the list.

# If the items in the list are numeric, they’re sorted by default in ascending numeric order.
# If they’re strings, they’re sorted in alphabetical order:
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)   # it did not change the original list
print(sorted_marxes)
print(marxes)

# But, calling the list function sort() on the marxes list does change marxes:
marxes = ['Groucho', 'Chico', 'Harpo']
sort_marxes = marxes.sort()      # list function sort() does change marxes
print(sort_marxes)    # Return : None
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)

# The default sort order is ascending, but you can add the argument reverse=True
# to set it to descending:
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

# Get Length by Using len()
# len() returns the number of items in a list
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print(marxes.count('Chico'))

# Assign with =, Copy with copy()
# When you assign one list to more than one variable, changing the list in one place
# also changes it in the other, as illustrated here:
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surprise'
print(a)
print(b)
b[0] = 'I hate surprises'
print(a)
print(b)

# You can copy the values of a list to an independent, fresh list by using any of these methods:
# 1. The list copy() function
# 2. The list() conversion function
# 3. The list slice[:]
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[0] = 'integer lists are boring'
print(a)
print(b)
print(c)
print(d)
b[0] = '1. integer lists are boring'
print(a)
print(b)
print(c)
print(d)
c[0] = '2. integer lists are boring'
print(a)
print(b)
print(c)
print(d)
d[0] = '3. integer lists are boring'
print(a)
print(b)
print(c)
print(c)
print(d)


## Tuples
# Create a Tuple by Using ()
empty_tuple =()
one_marx = 'Groucho',
print(one_marx)
marx_tuple='Groucho', 'Chico', 'Harpo'
print(marx_tuple)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# Tuple unpacking
a, b, c = marx_tuple
print(a)
print(b)
print(type(a))

# You can use tuples to exchange values in one statement without using a temporary variable:
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password)
print(icecream)
print(type(password))

# The tuple() conversion function makes tuples from other things:
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_list))

# Tuples Versue Lists
# You can often use tuples in place of lists, but they have many fewer functions—there is no append(),
# insert(), and so on—because they can’t be modified after creation.
# Why not just use lists instead of tuples everywhere?
# 1. Tuples use less space.
# 2. You can’t clobber(큰 타격을 주다) tuple items by mistake.
# 3. You can use tuples as dictionary keys (see the next section).
# 4. Named tuples (see Named Tuples) can be a simple alternative(대안이 되는) to objects.
# 5. Function arguments are passed as tuples (see Functions).


# Dictionaries
# Creat with {}
empty_dict = {}

bierce = {
 "day": "A period of twenty-four hours, mostly misspent",
 "positive": "Mistaken at the top of one's voice",
 "misfortune": "The kind of fortune that never misses",
 }
print(bierce)

# Convert by Using dict()
# Remember that the order of keys in a dictionary is arbitrary.

# A list of two-item lists:
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

# A list of two-item tuples:
lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(dict(lot))

# A tuple of two-item lists:
tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
print(dict(tol))

# A list of two-character strings:
los = [ 'ab', 'cd', 'ef' ]
print(dict(los))

# A tuple of two-character strings:
tos = ( 'ab', 'cd', 'ef' )
print(dict(tos))


# Add or Change an Item by [key]
# If the key was already present in the dictionary, the existing value is replaced by the new one.
# If the key is new, it’s added to the dictionary with its value.
pythons = {
 'Chapman': 'Graham',
 'Cleese': 'John',
 'Idle': 'Eric',
 'Jones': 'Terry',
 'Palin': 'Michael',
 }
print(pythons)

pythons['Gilliam'] = 'Gerry'  # 새로 Insert
print(pythons)
pythons['Gilliam'] = 'Terry'  # 기존값을 Update
print(pythons)

some_pythons = {
 'Graham': 'Chapman',
 'John': 'Cleese',
 'Eric': 'Idle',
 'Terry': 'Gilliam',
 'Michael': 'Palin',
 'Terry': 'Jones',
 }
print(some_pythons)

# Combine Dictinaries with update()
pythons = {
 'Chapman': 'Graham',
 'Cleese': 'John',
 'Gilliam': 'Terry',
 'Idle': 'Eric',
 'Jones': 'Terry',
 'Palin': 'Michael',
 }
others = { 'Marx': 'Groucho', 'Howard': 'Moe' }
pythons.update(others)                            # Likely extend() of Lists
print(pythons)

# What happens if the second dictionary has the same key as the dictionary into which it’s being merged?
# The value from the second dictionary wins:
first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)     # second dict win
print(first)

# Delete an Item by Key with del
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

# Delete All Items by Using clear()
pythons.clear()
print(pythons)
pythons = {}
print(pythons)


# Test for a Key by Using in
# If you want to know whether a key exists in a dictionary
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael'}
print('Chapman' in pythons)
print('Palin' in pythons)
print('Gilliam' in pythons)

# Get an Item by [key]
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael'}
print(pythons['Cleese'])

# If the key is not present in the dictionary, you’ll get an exception:
try:
    print(pythons['Marx'])
except KeyError as e:
    print(e)

# There are two good ways to avoid this. The first is to test for the key at the outset by using in,
# as you saw in the previous section:
print('Marx' in pythons)

# The second is to use the special dictionary get() function.
# You provide the dictionary, key, and an optional value.
# If the key exists, you get its value:
print(pythons.get('Cleese'))
print(pythons.get('Marx'))
print(pythons.get('Marx', 'Not a Python'))

# Get All keys by Using Keys()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())    # Return: dict_keys(['green', 'yellow', 'red'])
print(list(signals.keys()))    # Return: Type of Lists

# Get All Values by Using values()
print(signals.values())    # Return: dict_values
print(list(signals.values()))    # Return: Type of Lists

# Get All Key-Value Pairs by Using items()
print(signals.items())    # Return: dict_values
print(list(signals.items()))    # Return: list of two-items tuples


# Assign with =, Copy with copy()
# As with lists, if you make a change to a dictionary, it will be reflected in
# all the names that refer to it.
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)


## Sets

# Create with set()
empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
odd_numbers = {1, 3, 5, 7, 9}
print(odd_numbers)

# As with dictionary keys, sets are unordered.

# Convert from Other Data Types with set()
# You can create a set from a list, string, tuple, or dictionary, discarding any duplicate values.
print(set( 'letters' ))     # 중복은 1개만 남김.

# Make a Set from a list
print(set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] ))

# A set from a tuple
print(set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') ))

# When you give set() a dictionary, it uses only the keys:
print(set( {'apple': 'red', 'orange': 'orange', 'cherry': 'red'} ))  # Return: A set of only keys

# Test for Value by Using in
drinks = {
 'martini': {'vodka', 'vermouth'},
 'black russian': {'vodka', 'kahlua'},
 'white russian': {'cream', 'kahlua', 'vodka'},
 'manhattan': {'rye', 'vermouth', 'bitters'},
 'screwdriver': {'orange juice', 'vodka'}
 }

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print('')
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
print('')
# Combinations and Operations
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('')
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'orange juice'}:
        print(name)

drinks = {
 'martini': {'vodka', 'vermouth'},
 'black russian': {'vodka', 'kahlua'},
 'white russian': {'cream', 'kahlua', 'vodka'},
 'manhattan': {'rye', 'vermouth', 'bitters'},
 'screwdriver': {'orange juice', 'vodka'}
 }

bruss = drinks['black russian']
wruss = drinks['white russian']

a = {1, 2}
b = {2, 3}

# You get the intersection (members common to bothsets) with the special punctuation symbol &
# or the set intersection() function
print(a & b)     # Return: set {2}
print(a.intersection(b))
print(bruss & wruss)

# you get the union (members of either set) by using | or the set union() function:
print(a | b)     # Return: set {1, 2, 3}
print(a.union(b))
print(bruss | wruss)

# The difference (members of the first set but not the second) is obtained by using
# the character - or difference():
print(a - b)     # Return: set {1}
print(a.difference(b))
print(bruss - wruss)

# The exclusive or (items in one set or the other, but not both) uses ^ or symmetric_difference():
print(a ^ b)     # Return: set {1, 3}
print(a.symmetric_difference(b))
print(bruss ^ wruss)

# You can check whether one set is a subset of another
# (all members of the first set are also in the second set) by using <= or issubset():
a = {1, 2}
b = {2, 3}
print(a <= b)     # Return: Boolean
print(a.issubset(b))
print(bruss <= wruss)

# Is any set a subset of itself? Yup. (집합 자기자신은 부분집합)
print(a <= a)     # Return: Boolean
print(a.issubset(a))

# To be a proper subset, the second set needs to have all the members of the first and more.
# Calculate it by using <:   ~ 진부분집합
print(a < b)     # Return: Boolean
print(a.issubset(b))
print(bruss < wruss)

print('')
# A superset is the opposite of a subset (all members of the second set are also members of
# the first). This uses >= or issuperset():
print('[wruss]:', wruss)
print('[bruss]:', bruss)
print(a >= b)     # Return: Boolean
print(a.issuperset(b))
print(wruss >= bruss)

# Any set is a superset of itself:
print(a >= a)     # Return: Boolean
print(a.issuperset(a))
print(wruss >= wruss)

print('')
# And finally, you can find a proper superset (the first set has all members of the second,
# and more) by using >:
print(a > b)     # Return: Boolean
print(wruss > bruss)

print('')
# You can’t be a proper superset of yourself:
print(a > a)     # Return: Boolean

# Compare Data Structures
# you make a list by using square brackets ([]), a tuple by using commas, and a dictionary by
# using curly brackets ({}). In each case,
# you access a single element with square brackets:
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}

print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])


# Make Bigger Data Structures

marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

# We can make a tuple that contains each list as an element:
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)

# And, we can make a list that contains the three lists:
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)

# Finally, let’s create a dictionary of lists. In this example, let’s use the name of
# the comedy group as the key and the list of members as the value:
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)

# Your only limitations are those in the data types themselves. For example, dictionary keys need
# to be immutable, so a list, dictionary, or set can’t be a key for another dictionary.
# But a tuple can be. For example, you could index sites of interest by GPS coordinates
# (latitude, longitude, and altitude; see Maps for more mapping examples):
houses = {
(44.79, -93.14, 285): 'My House',
(38.89, -77.03, 13): 'The White House'
}


