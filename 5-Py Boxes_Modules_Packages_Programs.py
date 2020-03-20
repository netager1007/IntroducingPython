# Standalone Programs
# -------------------


# Command_Line Arguments
# ----------------------
# On your computer, create a file called test2.py that contains these two lines:
import sys
print('Program arguments:', sys.argv)

# $ python test2.py
# Program arguments: ['test2.py']
# $ python test2.py tra la la
# Program arguments: ['test2.py', 'tra', 'la', 'la']


# Modules and the import Statement
# --------------------------------
# We refer to code of other modules by using the import statement.
# This makes the code and variables in the imported module available to your program.

# Import a Module with Another Name
# ---------------------------------
# you can import using an alias.

# import report as wr
# description = wr.get_description()
# print("Today's weather:", description)

# Import Only What You Want from a Module
# ---------------------------------------
# With Python, you can import one or more parts of a module.
# Each part can keep its original name or you can give it an alias.
# First, let’s import get_description() from the report module with its original name:

# from report import get_description
# description = get_description()
# print("Today's weather:", description)

print('')
# Module Search Path
# ------------------
# Where does Python look for files to import? It uses a list of directory names
# and ZIP archive files stored in the standard sys module as the variable path.
# You can access and modify this list. Here’s the value of sys.path for Python 3.3 on my Mac:
import sys
for place in sys.path:
    print(place)

# Python looks in the current directory first when you try to import something:
# The first match will be used. This means that if you define a module named random and it’s in the search
# path before the standard library, you won’t be able to access the standard library’s random now.


# Packages
# --------
# We went from single lines of code, to multiline functions, to standalone programs,
# to multiple modules in the same directory.

# To allow Python applications to scale even more, you can organize modules into file hierarchies called packages.
# You’ll need one more thing in the sources directory: a file named __init__.py. This can be empty,
# but Python needs it to treat the directory containing it as a package.


# The Python Standard Library
# ---------------------------
# HandleMissing Keys with setdefault() and defaultdict()
# ------------------------------------------------------
# You’ve seen that trying to access a dictionary with a nonexistent key raises an exception.
# Using the dictionary get() function to return a default value avoids an exception.
# The setdefault() function is like get(), but also assigns an item to the dictionary
# if the key is missing:
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
periodic_table.setdefault('Carbon', 12)
print(periodic_table['Carbon'])    # Return: 12
print(periodic_table)              # Return: {'Helium': 2, 'Carbon': 12, 'Hydrogen': 1}

# If we try to assign a different default value to an existing key, the original value is returned and
# nothing is changed:
print(periodic_table.setdefault('Helium', 947))   # 값이 사전에 존재하면 변경되지 않음. 존재하는 Value를 반환(2)
print(periodic_table)
periodic_table['Helium'] = 99                     # 값이 변경됨.
print(periodic_table['Helium'])
print(periodic_table)


# defaultdict() is similar, but specifies the default value for any new key up front,
# when the dictionary is created. Its argument is a function. In this example,
# we pass the function int, which will be called as int() and return the integer 0:
from collections import defaultdict

periodic_table = defaultdict(int)
print(periodic_table)

# Now, any missing value will be an integer (int), with the value 0:
periodic_table['Hydrogen'] = 1
periodic_table['Lead']   # 'KeyError' Exception 발생하지 않고 'Lead':0 이 추가됨.
print(periodic_table)    # Return: defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})
print(dict(periodic_table))

# 일반적인 키가 없는 Dict를 조회하는 경우 Exception 발생
a_dict = {'h':1}
print(a_dict['h'])
try:
    print(a_dict['b'])
except KeyError as e:
    print('[Exception Occured]: Key Error', e)

# The argument to defaultdict() is a function that returns the value to be assigned to a missing key.
# In the following example, no_idea() is executed to return a value when needed:
from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])
print(bestiary)

# You can use the functions int(), list(), or dict() to return default empty values
# for those types: int() returns 0, list() returns an empty list ([]), and dict()
# returns an empty dictionary ({}). If you omit the argument, the initial value of
# a new key will be set to None.
# By the way, you can use lambda to define your default-making function right inside the call:
bestiary = defaultdict(lambda: 'Huh?')
print(bestiary)
print(bestiary['E'])

# Using int is one way to make your own counter:
from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

print(food_counter)
for food, count in food_counter.items():
    print(food, count)

# In the preceding example, if food_counter had been a normal dictionary
# instead of a defaultdict, Python would have raised an exception every time we tried
# to increment the dictionary element food_counter[food] because it would not have been
# initialized. We would have needed to do some extra work, as shown here:
dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)


# Other Example setdefault(), collections.defaultdict()
# -----------------------------------------------------

# 이러한 코딩 패턴은 파이썬에서 사전을 사용할 때 상당히 자주 접할 수 있는데,
# 코드 가독성 측면에서는 이렇게 사소한 처리가 주요 흐름을 파악을 하는데 방해가 됨.
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

# 위와 같은 if 조건절을 피할 수 있도록 파이썬의 사전(dictionary) 자료구조는 setdefault 함수를 제공
# 첫번째 인자로 키(key)값, 두번째 인자로 기본값(default value)를 넘기면 됨
def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter

# 파이썬의 내장 모듈인 collections의 defaultdict 클래스는 이러한 경우 사용
# defaultdict 클래스의 생성자로 기본값을 생성해주는 함수를 넘기면, 모든 키에 대해서 값이 없는 경우
# 자동으로 생성자의 인자로 넘어온 함수를 호출하여 그 결과값으로 설정해줍니다.
from collections import defaultdict

def countLetters(word):
    counter = defaultdict(int)
    for letter in word:
        counter[letter] += 1
    return counter

# defaultdict 클래스의 생성자로 int 함수를 넘긴 이유는 int()는 0을 리턴하기 때문입니다.
# 람다 함수를 활용해서 다음과 같이 int 함수 대신에 lambda: 0를 넘겨도 동일하게 작동을 합니다.
from collections import defaultdict

def countLetters(word):
    counter = defaultdict(lambda: 0)
    for letter in word:
        counter[letter] += 1
    return counter

# 사전 기본값으로 빈 리스트 세팅하기
from collections import defaultdict

def groupWords(words):
    grouper = defaultdict(list)
    for word in words:
        length = len(word)
        grouper[length].append(word)
    return grouper

word_list = ['a', 'b','c','a','b','c','aa','bb','cc','aaa','bbb','cccc']
print(dict(groupWords(word_list)))

# 만약에 collections.defaultdict 클래스 없이 위 코드를 작성해야했다면
# 다음과 같이 다소 지저분하게 작성했었을 것
def groupWords(words):
    grouper = {}
    for word in words:
        length = len(word)
        if length not in grouper:
            grouper[length] = []
        grouper[length].append(word)
    return grouper

word_list = ['a', 'b','c','a','b','c','aa','bb','cc','aaa','bbb','cccc']
print(dict(groupWords(word_list)))

# [보너스] 사전 기본값으로 빈 세트 세팅하기
# 위에서 작성한 코드에서 단어들을 길이에 따라 분류할 때 중복되지 않은
# 단어만 필요하다면 어떻게 해야할까요?
# defaultdict 생성자에 list 함수 대신에 set 함수를 넘기고,
# append 함수 대신에 add 함수를 이용해서 단어를 넘기면 됩니다. :)
from collections import defaultdict

def groupWords(words):
    grouper = defaultdict(set)
    for word in words:
        length = len(word)
        grouper[length].add(word)
    return grouper

word_list = ['a', 'b','c','a','b','c','aa','bb','cc','aaa','bbb','cccc']
print(dict(groupWords(word_list)))


# Count Items with Counter()
# --------------------------

word_list = ['a', 'b', 'c', 'a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'cccc']
aa = 'abcdefaaa'
print(len(aa))
print(aa.count('a'))  # General count method
print(len(word_list))
print(word_list.count('a'))  # General count method

# Speaking of counters, the standard library has one that does the work
# of the previous example and more:
from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam', 'lee', 'lee']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)            # Return: Counter({'spam': 3, 'lee': 2, 'eggs': 1})

# The most_common() function returns all elements in descending order,
# or just the top count elements if given a count:
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

# Order by Key with OrderedDict()
quotes = {'Moe': 'A wise guy, huh?', 'Larry': 'Ow!', 'Curly': 'Nyuk nyuk!', }   # 순서가 없음.
for stooge in quotes:
    print(stooge)

# An OrderedDict() remembers the order of key addition and returns them in the same order
# from an iterator. Try creating an OrderedDict from a sequence of (key, value) tuples:
from collections import OrderedDict

quotes = OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!'),])
for stooge in quotes:
    print(stooge)      # 순서를 유지

# Stack + Queue == deque
# ----------------------
# A deque (pronounced deck) is a double-ended queue, which has features of both a stack and
# a queue. It’s useful when you want to add and delete items from either end of a sequence.
# Here, we’ll work from both ends of a word to the middle to see if it’s a palindrome.
# The function popleft() removes the leftmost item from the deque and returns it;
# pop() removes the rightmost item and returns it. Together, they work from the ends toward the middle.
# As long as the end characters match, it keeps popping until it reaches the middle:
def palindrome(word):
    from collections import deque
    dq = deque(word)
    print(dq)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        print(dq)
    return True
print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))

# If you really wanted a quick palindrome checker, it would be a lot simpler
# to just compare a string with its reverse.
# Python doesn’t have a reverse() function for strings,
# but it does have a way to reverse a string with a slice, as illustrated here:
def another_palindrome(word):
    return word == word[::-1]

print(another_palindrome('radar'))
print(another_palindrome('halibut'))

# Iterate over Code Structures with itertools
# -------------------------------------------
# itertools contains special-purpose iterator functions.
# Each returns one item at a time when called within a for … in loop,
# and remembers its state between calls.
# chain() runs through its arguments as though they were a single iterable:
import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# cycle() is an infinite iterator, cycling through its arguments:
import itertools
for item in itertools.cycle([1, 2]):
    print(item)
    cnt = 0
    cnt += 1
    break

# accumulate() calculates accumulated values. By default, it calculates the sum:
import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

print('')
# You can provide a function as the second argument to accumulate(),
# and it will be used instead of addition.
# The function should take two arguments and return a single result.
# This example calculates an accumulated product:
import itertools
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)


# Print Nicely with pprint()
# --------------------------
# All of our examples have used print() (or just the variable name,
# in the interactive interpreter) to print things.
# Sometimes, the results are hard to read. We need a pretty printer such as pprint():
from pprint import pprint
quotes = OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!'),])

# Plain old print() just dumps things out there:
print(quotes)

# However, pprint() tries to align elements for better readability:
pprint(quotes)

# More Batteries: Get Other Python Code
# -------------------------------------
# Sometimes, the standard library doesn’t have what you need,
# or doesn’t do it in quite the right way.
# There’s an entire world of open-source, third-party Python software.
# Good resources include:
# 1. PyPi (also known as the Cheese Shop, after an old Monty Python skit)
# 2. github
# 3. readthedocs
# You can find many smaller code examples at activestate.
