# Functions
# ---------
def do_nothing():
    pass

do_nothing()
print(do_nothing())


def make_a_sound():
    print('quack')
make_a_sound()


def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')


# Input Argument
# --------------
def echo(anything):
    return anything + ' ' + anything

print(echo('Yahoo'))

def commentary(color):
    if color == 'red':
        return "It's a tomato"
    elif color == 'green':
        return "It's a green pepper"
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."

comment = commentary('blue')
print(comment)

# None Is Useful
# --------------
# Remember that zero-valued integers of floats, empty string(''), lists([]), tuples((,)),
# dictionaries({}), and sets(set()) are all False, but are not queal to None.
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

if thing is None:
    print("It's nothing")
else:
    print("It's something")


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
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu('chardonnay','chicken','cake'))

# Keyword Arguments
# -----------------
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# Positional and keyword arguments
# --------------------------------
print(menu('frontenac', dessert='flan', entree='fish'))

# Specify Default Parameter Values
# --------------------------------
# Default argument values are calculated when the function is defined, not when it is run.

def menu(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

print(menu('chardonnay', 'chicken'))
print(menu('dunkelfelder', 'duck','doughnut'))


# Default argument values are calculated when the function is defined.

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')    # ['a']
buggy('b')    # ['a', 'b']

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    return result

# Gather Positional Arguments with *
# When used inside the function with a parameter, an asterisk groups a varialbenumber
# of positional arguments into a tuple of parameter values.

def print_args(*args):
    print('Position argument tuple:', args)

print_args(3, 2, 1, 'wait!', 'uh...')

def print_more(required1, required2, *args):
    print('Need this one: ', required1)
    print('Need this one too: ', required2)
    print('All the rest: ', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


# Gather Keyword Arguments with **
# Inside the function, kwargs is a dictionary

def print_kwargs(**kwargs):
    print('Keyword arguemnts: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# Docstrings

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operation is:
        1. Check wheather the *second* argument is true.
        2. If it is, print the *first* arguemnt
    '''
    if check:
        print(thing)

print(help(echo))
print('echo.__doc__ : ', echo.__doc__)
print(help(print_if_true))
print(print_if_true.__doc__)


# Functions Are First-Class Citizens

def answer():
    print(42)
answer()

def run_something(func):
    func()

run_something(answer)


def add_args(arg1, arg2):
    print(arg1 + arg2)

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)


def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))


# Inner Functions
def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

print('outer: ', outer(4, 7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)
print(knights('Ni!'))


# Closures ~ 어떨때 유용하게 사용할 수 있을까?
# -----------------------------------------
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
print(knights2('Duck'))
a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(type(b))
print(a())


# Anonymous Functions: the lambda() Function
def edit_story(words, func):
    for word in words:
        print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'

edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalize() + '!')


# Generators

print(sum(range(1, 101)))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
print(my_range)
ranger = my_range(1, 5)
print(ranger)
print(type(ranger))

for x in ranger:
    print(x)


# Decorators
# ----------
# Sometimes, you want to modify an existing function without changing its source code.
# A common example is adding a debugging statement to see what arguments were passed in

def document_it(func):
    def new_function(*args, **kwargs):
        print('')
        print('[Document_it] Running function:', func.__name__)
        print('[Document_it] Positional argument:', args)
        print('[Document_it] Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('')
        print('[Document_it] Result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print('add_ints():', add_ints(3, 5))

cooler_add_ints = document_it(add_ints)  # manual decorator assignment
print(cooler_add_ints)
print(type(cooler_add_ints))
cooler_add_ints(3, 7)
cooler_add_ints(b=3, a=7)
cooler_add_ints(4, b=8)

print('add_ints():', add_ints(5, 5))

debug_flag = False

@document_it
def add_ints1(a, b):
    return a + b

print(add_ints1(1, 1))

def square_it(func):
    def new_function(*args, **kwargs):
        print('')
        print('[Square_it] Running function:', func.__name__)
        print('[Square_it] Positional argument:', args)
        print('[Square_it] Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('[Square_it] Result:', result)
        print('')
        return result * result
    return new_function

@square_it
def add_int2(a, b):
    return a + b
print('add_int2():', add_int2(2, 3))


@document_it
@square_it
def add_int3(a, b):
    return a + b
print('add_int3():', add_int3(3, 3))

@square_it
@document_it
def add_int4(a, b):
    return a + b
print('add_int4():', add_int4(4, 4))


# Namespaces and Scope

animal = 'fruitbat'  # Global Variable
def print_global():
    print('Inside print_global:', animal)
print('At the top level:', animal)
print_global()

animal = 'redrabbit'
def change_and_print_global():
    print('Inside change_and_print_global:', animal)
    animal = 'wombat'                 # Can't modified Global Variable
    print('After the change:', animal)
try:
    change_and_print_global()
except Exception as err:
    print('Error Occured: ', err)

animal = 'bluerabbit'
def change_local():
    animal = 'wombat'
    print('Inside change_local: ', animal, id(animal))
change_local()
print('Outside: ', animal, id(animal))

# Global Variable Modify
animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('Inside change_and_print_global: ', animal, id(animal))
change_and_print_global()
print('Outside: ', animal, id(animal))

# locals() returns a dictionary of the contents of the local namespace.
# globals() returns a dictionary of the contents of the global namespace.

animal = 'fruitbat'
def change_local():
    animal = 'wombat'   # local variable
    print('locals:', locals())
#    print('globals:', globals())

print(animal)
change_local()


# Uses of _ and __ in Names
def amazing():
    '''
    This is the amazing function.
    Want to see it again?
    '''

    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)
amazing()


# Handle Errors with try and except
short_list = [1, 2, 3]
position = 5

try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list) - 1, ' but got', position)


# Make Your Own Exceptions
class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise UppercaseException(word)
        except UppercaseException as exc:
            print(exc)


