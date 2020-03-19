# Comment with #
# A comment is a piece of text in your program that is ignored by the Python interpreter.

# Continue Lines with \
alphabet = 'abcdefg' + \
 'hijklmnop' + \
 'qrstuv' + \
 'wxyz'
print(alphabet)

alphabet = 'abcdefg' + \
 'hijklmnop' + \
 'qrstuv' + \
 'wxyz'
print(alphabet)


# Compare with if, elif, and else
disaster = True
if disaster:
    print('Woe!')
else:
    print('Whee!')


furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

# Python’s comparison operators are:
# 1. equality              ==
# 2. inequality            !=
# 3. less than             <
# 4. less than or equal    <=
# 5. greater than          >
# 6. greater than or equal >=
# 7. membership            in …

x = 7
print(5 < x and x < 10)
print((5 < x) and (x < 10))
print(5 < x or x < 10)
print(5 < x and x > 10)
print(5 < x and not x > 10)
print(5 < x < 10)
print(5 < x < 10 < 999)

# What Is True?
# What if the element we’re checking isn’t a boolean?
# What does Python consider True and False?
# A false value doesn’t necessarily need to explicitly be False.
# For example, these are all considered False:
# boolean         False
# null            None
# zero integer    0
# zero float      0.0
# empty string    ''
# empty list      []
# empty tuple     ()
# empty dict      {}
# empty set set   ()

# Anything else is considered True.
# Python programs use this definition of “truthiness”`
some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")


# Repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1

# Cancel with break
# while True:
#    stuff = input("String to capitalize [type q to quit]: ")
#    if stuff == "q":
#        break
#    print(stuff.capitalize())

# Skip Ahead with continue
#while True:
#    value = input("Integer, please [q to quit]: ")
#    if value == 'q': # quit
#        break
#    number = int(value)
#    if number % 2 == 0: # an even number
#        continue
#    print(number, "squared is", number*number)

# Check break Use with else    : while ~ else
# If the while loop ended normally (no break call), control passes to an optional else.
# You use this when you’ve coded a while loop to check for something, and breaking as soon as
# it’s found. The else would be run if the while loop completed but the object was not found:
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:                             # break not called
    print('No even number found')

# iterate with for
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)    # Return: keys

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# Cancel with break

# Skip with continue

# Check break Use with else
# Similar to while, for has an optional else that checks if the for completed normally.
# If break was not called, the else statement is run.
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:                 # no break means no cheese
    print('This is not much of a cheese shop, is it?')


# Iterate Multiple Sequences with zip()
# There’s one more nice iteration trick: iterating over multiple sequences in parallel
# by using the zip() function:
# zip() stops when the shortest sequence is done.
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)


# The value returned by zip() is itself not a tuple or list, but an iterable value
# that can be turned into one:
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(zip(english, french))
print(list(zip(english, french)))
print(dict(zip(english, french)))
print(dict(zip(french, english)))

# Generate Number Sequences with range()
# The range() function returns a stream of numbers within a specified range.
# This lets you create huge ranges without using all the memory in your computer
# and crashing your program.
# If you omit start, the range begins at 0. The only required value is stop
# The default value of step is 1, but you can go backward with -1.
for x in range(0, 3):
    print(x)

print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)

print(list(range(2, -1, -1)))

print(list(range(0, 11, 2)))

# Other Iterators  : Let's See Chapter 8


# Comprehensions
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

number_list = list(range(1, 6))
print(number_list)

# The simplest form of list comprehension is:
# [ expression for item in iterable ]

number_list = [number for number in range(1, 6)]
print(number_list)

number_list = [number - 1 for number in range(1, 6)]
print(number_list)

# A list comprehension can include a conditional expression, looking something like this:
# [ expression for item in iterable if condition ]

# Let’s make a new comprehension that builds a list of only the odd numbers between 1 and 5
# (remember that number % 2 is True for odd numbers and False for even numbers):
number_list = [number for number in range(1, 6) if number % 2 == 1]
print(number_list)

# Now, the comprehension is a little more compact than its traditional counterpart:
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)


# Finally, just as there can be nested loops, there can be more than one set of for ... clauses
# in the corresponding comprehension. To show this, let’s first try a plain, old nested loop
# and print the results:
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)

# Now, let’s use a comprehension and assign it to the variable cells,
# making it a list of (row, col) tuples:
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]    # list of tuple
print(cells)

for row, col in cells:
    print(row, col)


a = [1,2,3]
b = [4,5,6]
aa = [(a_num, b_num) for a_num in a for b_num in b if a_num % 2 == 1]
print(aa)

# Dictionary Comprehensions
# -------------------------
# Not to be outdone by mere lists, dictionaries also have comprehensions.
# The simplest form looks familiar:
# { key_expression : value_expression for expression in iterable }
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# So, the following would have been a teeny bit more Pythonic:
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in set(word)}
print(letter_counts)

# Set Comprehensions
# ------------------
# The simplest version looks like the list and dictionary comprehensions that you’ve just seen:
# { expression for expression in iterable }
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)


# Generator Comprehensions
# ------------------------
# Tuples do not have comprehensions! You might have thought that changing the square brackets
# of a list comprehension to parentheses would create a tuple comprehension.
# And it would appear to work because there’s no exception if you type this:
number_thing = (number for number in range(1, 6))  # It is not tuple, it's generator
print(type(number_thing))

# You can iterate over this generator object directly, as illustrated here:
for number in number_thing:
    print(number)

# Or, you can wrap a list() call around a generator comprehension to make it work like
# a list comprehension:
number_thing = (number for number in range(1, 6))  # It is not tuple, it's generator

number_list = list(number_thing)
print(number_list)

# Generator 는 한번 사용하면 값이 사라짐.
# A generator can be run only once. Lists, sets, strings, and dictionaries exist in memory,
# but a generator creates its values on the fly and hands them out one at a time through
# an iterator. It doesn’t remember them, so you can’t restart or back up a generator.
number_thing = (number for number in range(1, 6))  # It is not tuple, it's generator
for number in number_thing:        # First Usage number_thing
    print(number)                  # Return: 1 2 3 4 5
number_list = list(number_thing)   # Second Usage number_thing
print(number_list)                 # Return: []


# Functiions
# ----------
# Function names have the same rules as variable names (they must start with a letter
# or _ and contain only letters, numbers, or _).

def commentary(color):     # color is parameter
    if color == 'red':
        return "It's a tomato."
    elif color == 'green':
        return "it's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it"
    else:
        return "I've never heard of the color " + color + '.'

comment = commentary('blue')  # blue is argument
print(comment)


# NONE IS USEFUL
# --------------
# None is a special Python value that holds a place when there is nothing to say.
# It is not the same as the boolean value False, although it looks false when evaluated
# as a boolean. Here’s an example:
thing = None
if thing:                       # None is not False
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")

# This seems like a subtle distinction, but it’s important in Python.
# You’ll need None to distinguish a missing value from an empty value.
# Remember that zero-valued integers or floats, empty strings (''), lists ([]), tuples ((,)),
# dictionaries ({}), and sets(set()) are all False, but are not equal to None.
def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")
is_none(None)
is_none(True)
is_none(False)
is_none(0)
is_none(0.0)
is_none(())
is_none([])
is_none({})
is_none(set())


# Positional Arguments
# --------------------
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert':dessert}
print(menu('chardonnay', 'chicken', 'cake'))

# Although very common, a downside of positional arguments is that you need to remember
# the meaning of each position. If we forgot and called menu() with wine as the last argument
# instead of the first, the meal would be very different:
print(menu('beef', 'bagel', 'bordeaux'))

# Keyword Arguments
# -----------------
# To avoid positional argument confusion(혼동), you can specify arguments by the names of their
# corresponding parameters, even in a different order from their definition in the function:
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# You can mix positional and keyword arguments. Let’s specify the wine first, but use keyword
# arguments for the entree and dessert:
print(menu('frontenac', dessert='flan', entree='fish'))  # First args : Positional Args
                                                         # Second and Third args : Keyword Args

# Specify Default Parameter Values
# --------------------------------
# You can specify default values for parameters. The default is used if the caller
# does not provide a corresponding argument. This bland-sounding feature can actually be quite
# useful. Using the previous example:
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken'))

def menu(wine='aa', entree='bb', dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu())

# If you do provide an argument, it’s used instead of the default:
print(menu('dunkelfelder', 'duck', 'doughnut'))

# Default argument values are calculated when the function is defined, not when it is run.
# A common error with new (and sometimes not-so-new) Python programmers is to use a mutable data type
# such as a list or dictionary as a default argument.

# In the following test, the buggy() function is expected to run each time with a fresh empty
# result list, add the arg argument to it, and then print a single-item list.
# However, there’s a bug: it’s empty only the first time it’s called.
# The second time, result still has one item from the previous call:
def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')       # expect ['b'], but ['a', 'b']

# It would have worked if it had been written like this:
def works(arg):
    result = []
    result.append(arg)
    print(result)
works('a')      # Result: ['a']
works('b')      # Result: ['b']

# The fix is to pass in something else to indicate the first call:
def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')      # Result: ['a']
nonbuggy('b')      # Result: ['b']

# Gather Positional Arguments with *
# ----------------------------------
# If you’ve programmed in C or C++, you might assume that an asterisk (*) in a Python program
# has something to do with a pointer.
# Nope, Python doesn’t have pointers.
# When used inside the function with a parameter, an asterisk groups a variable number
# of positional arguments into a tuple of parameter values.
def print_args(*args):
    print('[Positional argument tuple]:', args)
print_args()

print_args(3, 2, 1, 'wait!', 'uh...')

# This is useful for writing functions such as print() that accept a variable number of arguments.
# If your function has required positional arguments as well, *args goes at the end and grabs
# all the rest:
def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)
print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')

# Gather Keyword Arguments with **
# --------------------------------
# You can use two asterisks (**) to group keyword arguments into a dictionary,
# where the argument names are the keys, and their values are the corresponding dictionary values.
# The following example defines the function print_kwargs() to print its keyword arguments:
def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# Docstrings
# ----------
# You can attach documentation to a function definition by including a string at the beginning
# of the function body. This is the function’s docstring:
def echo(anything):
    'echo returns its input argument'
    return anything

print(help(echo))     # help(function_name)
print(echo.__doc__)

# You can make a docstring quite long and even add rich formatting,
# if you want, as is demonstrated in the following:
def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
    1. Check whether the *second* argument is true.
    2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)

# Functions Are First-Class Citizens
# ----------------------------------
# I’ve mentioned the Python mantra, everything is an object.
# This includes numbers, strings, tuples, lists, dictionaries—and functions,
# as well. Functions are first-class citizens in Python. You can assign them to variables,
# use them as arguments to other functions, and return them from functions.
# This gives you the capability to do some things in Python that are difficult-to-impossible
# to carry out in many other languages.

# To test this, let’s define a simple function called answer() that doesn’t have any arguments;
# it just prints the number 42:
def answer():
    return 42

# If you run this function, you know what you’ll get:
print(answer())

# Now, let’s define another function named run_something. It has one argument called func,
# a function to run. Once inside, it just calls the function.
def run_something(func):
    print(func())

# If we pass answer to run_something(), we’re using a function as data, just as with anything else:
run_something(answer)

# Notice that you passed answer, not answer(). In Python, those parentheses mean call this function.
# With no parentheses, Python just treats the function like any other object.
# That’s because, like everything else in Python, it is an object:

# Let’s try running a function with arguments. Define a function add_args() that prints
# the sum of its two numeric arguments, arg1 and arg2:
def add_args(arg1, arg2):
    print(arg1 + arg2)

# At this point, let’s define a function called run_something_with_args() that takes three arguments:
# func — The function to run
# arg1 — The first argument for func
# arg2 — The second argument for func
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

# Let’s define a test function that takes any number of positional arguments,
# calculates their sum by using the sum() function, and then returns that sum:
def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)                      # Why pass *args
                                            # print(args)  ~ Return (1, 2, 3, 4) tuple
                                            # print(*args) ~ Return: 1 2 3 4

print(run_with_positional_args(sum_args, 1, 2, 3, 4))

# You can use functions as elements of lists, tuples, sets, and dictionaries.
# Functions are immutable, so you can also use them as dictionary keys.

# Inner Functions
# ---------------
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print(outer(4, 7))

# An inner function can be useful when performing some complex task more than once within
# another function, to avoid loops or code duplication.
# For a string example, this inner function adds some text to its argument:
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))


# Closures
# --------
# An inner function can act as a closure. This is a function that is dynamically generated
# by another function and can both change and remember the values of variables
# that were created outside the function.

# The following example builds on the previous knights() example.
# Let’s call the new one knights2(), because we have no imagination, and turn the inner()
# function into a closure called inner2(). Here are the differences:
# - inner2() uses the outer saying parameter directly
# - instead of getting it as an argument.
# - knights2() returns the inner2 function name instead of calling it.

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

# The inner2() function knows the value of saying that was passed in and remembers it.
# The line return inner2 returns this specialized copy of the inner2 function (but doesn’t call it).
# That’s a closure: a dynamically created function that remembers where it came from.
# Let’s call knights2() twice, with different arguments:
a = knights2('Duck')
b = knights2('Hasenpfeffer')

# Okay, so what are a and b?
print(type(a))    # Return: <class 'function'>
print(type(b))    # Return: <class 'function'>

# They’re functions, but they’re also closures:
print(a)          # Return: <function knights2.<locals>.inner2 at 0x000001ED9818EB88>
print(b)          # Return: <function knights2.<locals>.inner2 at 0x000001ED981978B8>

# If we call them, they remember the saying that was used when they were created by knights2:
print(a())
print(b())

# Anonymous Functions: the lambda() Function
# ------------------------------------------
# In Python, a lambda function is an anonymous function expressed as a single statement.
# You can use it instead of a normal tiny function.
def edit_story(words, func):
    for word in words:
        print(func(word))

# Now, we need a list of words and a function to apply to each word.
# For the words, here’s a list of (hypothetical) sounds made by my cat
# if he (hypothetically) missed one of the stairs:
stairs = ['thud', 'meow', 'thud', 'hiss']

# And for the function, this will capitalize each word and append an exclamation point,
# perfect for feline tabloid newspaper headlines:
def enliven(word):         # give that prose more punch
    return word.capitalize() + '!'

edit_story(stairs, enliven)

# Finally, we get to the lambda. The enliven() function was so brief that
# we could replace it with a lambda:
stairs = ['thud', 'meow', 'thud', 'hiss']

def edit_story(words, func):
    for word in words:
        print(func(word))

edit_story(stairs, lambda word: word.capitalize() + '!')

# The lambda takes one argument, which we call word here.
# Everything between the colon and the terminating parenthesis is the definition of the function.
# Often, using real functions such as enliven() is much clearer than using lambdas.
# Lambdas are mostly useful for cases in which you would otherwise need to define many tiny functions
# and remember what you called them all. In particular, you can use lambdas in graphical user interfaces
# to define callback functions; see Appendix A for examples.

# Generators
# ----------
# A generator is a Python sequence creation object.
# With it, you can iterate through potentially huge sequences without creating and storing
# the entire sequence in memory at once. Generators are often the source of data for iterators.
# If you recall, we already used one of them, range(), in earlier code examples to generate
# a series of integers. In Python2, range() returns a list, which limits it to fit in memory.
# Python 2 also has the generator xrange(), which became the normal range() in Python 3.
# This example adds all the integers from 1 to 100:
print(sum(range(1,101)))


# Every time you iterate through a generator, it keeps track of where it was the last time
# it was called and returns the next value. This is different from a normal function,
# which has no memory of previous calls and always starts at its first line with the same state.

# If you want to create a potentially large sequence, and the code is too large for a generator
# comprehension, write a generator function. It’s a normal function, but it returns its value
# with a yield statement rather than return. Let’s write our own version of range():
def my_range(first=0, last=0, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)    # It's a normal function. Return: <function my_range at 0x0000017767129D38>

# And it returns a generator object:
ranger = my_range(1, 5)
print(ranger)      # <generator object my_range at 0x000001418D6A1EC8>

# We can iterate over this generator object:
for x in my_range(1, 5):
    print(x)

for x in ranger:
    print(x)


# Decorators
# ----------
# Sometimes, you want to modify an existing function without changing its source code.
# A common example is adding a debugging statement to see what arguments were passed in.

# A decorator is a function that takes one function as input and returns another function.
# We’ll dig(파다, 깊이 연구하다) into our bag of Python tricks and use the following:
# - *args and **kwargs
# - Inner functions
# - Functions as arguments

# The function document_it() defines a decorator that will do the following:
# - Print the function’s name and the values of its arguments
# - Run the function with the arguments
# - Print the result
# - Return the modified function for use

# Here’s what the code looks like:
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

print('')
# Whatever func you pass to document_it(), you get a new function that includes the extra statements
# that document_it() adds. A decorator doesn’t actually have to run any code from func,
# but document_it() calls func part way through so that you get the results of func as well as
# all the extras.
# So, how do you use this? You can apply the decorator manually:
def add_ints(a, b):
    return a + b
print(add_ints(3, 5))

cooler_add_ints = document_it(add_ints)    # manual decorator assignment
print(type(cooler_add_ints))
cooler_add_ints(3, 5)

print('')
# As an alternative to the manual decorator assignment above, just add @decorator_name before
# the function that you want to decorate:
@document_it
def add_ints(a, b):
    return a + b

add_ints(1, 3)
print('')
print(add_ints(1, 3))


# You can have more than one decorator for a function.
# Let’s write another decorator called square_it() that squares the result:
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

# The decorator that’s used closest to the function (just above the def) runs first
# and then the one above it.
# Either order gives the same end result, but you can see how the intermediate steps change:
print('')

@document_it
@square_it
def add_ints(a, b):
    return a + b
add_ints(3, 5)

# Let’s try reversing the decorator order:
print('')
@square_it
@document_it
def add_ints(a, b):
    return a + b
print(add_ints(3, 5))


# Using Decorator in Class
# ------------------------
import datetime
class DatetimeDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())

class MainClass:
    @DatetimeDecorator
    def main_func_1():
        print('Main Func 1 Start')

    @DatetimeDecorator
    def main_func_2():
        print('Main Func 2 Start')

my = MainClass()
my.main_func_1()
my.main_func_2()


# -*- coding: utf-8 -*-
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print '{} 함수가 호출되기전 입니다.'.format(original_function.__name__)
#         return original_function(*args, **kwargs)
#     return wrapper_function

class DecoratorClass:  #1
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass  #2
def display():
    print('display 함수가 실행됐습니다.')


@DecoratorClass  #3
def display_info(name, age):
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display()
print
display_info('John', 25)

# 프로젝트에서 실제로 어떻게 사용을 해야 하는지를 모르는 경우가 많습니다.
# 다음 예제를 통해 실제 프로젝트에서 데코레이터가 어떻게 쓰이는지 살펴보죠.
# 일반적으로 데코레이터는 로그를 남기거나 유저의 로그인 상태등을 확인하여 로그인 상태가 아니면
# 로그인 페이지로 리더랙트(redirect)하기 위해서 많이 사용됩니다.
# 또한 프로그램의 성능을 테스트하기 위해서도 많이 쓰입니다.
# 리눅스나 유닉스 서버 관리자는 스크립트가 실행되는 시간을 측정하기 위해서
# 다음과 같은 date와 time 명령어를 많이 사용합니다.
import datetime
import time

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('Lee', 25)



# -*- coding: utf-8 -*-
# ------------------------------------------------------------
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):  # 1
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_timer  # 2
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('Soon', 25)

# -*- coding: utf-8 -*-
# 두개의 decorator 를 동시에 사용
# ------------------------------------------------------------
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_logger  # 1
@my_timer  # 2
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('John', 25)

# #1, #2에 데코레이터 2개를 한꺼번에 사용하였습니다.
# 터미널 상의 실행결과는 아까와 같이 출력되었습니다.
# 그런데 로그 파일에 아무것도 기록이 안됐습니다.
# 그 대신에 wrapper.log란 이름의 로그 파일 생성됐고, 그 안에 다음과 같은 로그가 남았습니다.

# 흠... 왜 그럴까요? 그럼 이번에는 데코레이터의 순서를 바꿔 볼까요?
# -*- coding: utf-8 -*-
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper  # 3


def my_timer(original_function):  # 4
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_timer  # 2
@my_logger  # 1
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('John', 25)

# 이번에는 로그 파일(display_info.log)에 잘 로깅이 됐네요.
# 앗! 그런데 터미널에 출력된 결과가 좀 이상하네요. : [ wrapper 함수가 실행된 총 시간: 1.0019299984 초 ]

# 이렇게 되는 이유는 아주 간단합니다.
# 복수의 데코레이터를 스택해서 사용하면 아래쪽 데코레이터부터 실행되는데,
# 위의 코드의 경우에는 #1의 my_logger가 먼저 실행되고 #2의 my_timer에게 #3에서 wrapper 함수를
# 인자로써 리턴하기 때문에 생기는 현상입니다.
# #4에서 original_function은 물론 wrapper 함수와 같습니다.

# 위와 같은 현상을 방지하기 위해서 만들어진 모듈이 있는데 그것이 functools 모듈의 wraps 데코레이터입니다.
# 한 번 사용해 볼까요?
# -*- coding: utf-8 -*-
from functools import wraps
import datetime
import time


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)  # 1
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info(
            '[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)  # 2
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('Jimmy', 30)  # 3



# Namespaces and Scope
# --------------------
# The main part of a program defines the global namespace; thus, the variables in that namespace
# are global variables.
# You can get the value of a global variable from within a function:
animal = 'fruitbat'

def print_global():
   print('inside print_global:', animal)
print('at the top level:', animal)

print_global()

# But, if you try to get the value of the global variable and change it within the function,
# you get an error:
animal = 'fruitbat'
def change_and_print_global():
    print('inside change_and_print_global:', animal)  # 여기에서 global의 animal을 사용하고
    animal = 'wombat'                                 # global의 animal을 변경해서 Exception 발생
    print('after the change:', animal)
try:
    change_and_print_global()
except UnboundLocalError as e:
    print('[Exception Occured]:', e)

# If you just change it, it changes a different variable also named animal,
# but this variable is inside the function:
animal = 'fruitbat'
def change_local():
    animal = 'wombat'                                 # local 변수 animal 정의되고 할당됨.
    print('inside change_local:', animal, id(animal))

change_local()
print(animal)
print(id(animal))

# To access the global variable rather than the local one within a function,
# you need to be explicit and use the global keyword (you knew this was coming:
# explicit is better than implicit):
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print(animal)
change_and_print_global()
print(animal)


# Python provides two functions to access the contents of your namespaces:
# 1. locals() returns a dictionary of the contents of the local namespace.
# 2. globals() returns a dictionary of the contents of the global namespace.
animal = 'fruitbat'
def change_local():
    animal = 'wombat' # local variable
    print('locals:', locals())

print(animal)
change_local()

print('globals:', globals()) # reformatted a little for presentation
print(animal)


# Uses of _ and __ in Names
# -------------------------
# Names that begin and end with two underscores (__) are reserved for use within Python,
# so you should not use them with your own variables. This naming pattern was chosen
# because it seemed unlikely to be selected by application developers for their own variables.
# For instance, the name of a function is in the system variable function .__name__,
# and its documentation string is function .__doc__:
def amazing():
    '''This is the amazing function.
       Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()


# Handle Errors with try and except
# ---------------------------------
short_list = [1, 2, 3]

while True:
#    value = input('Position [q to quit]? ')
    value = 'q'
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

# Make Your Own Exceptions
# ------------------------
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)
        except:
            pass


# You can access the exception object itself and print it:
class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)
