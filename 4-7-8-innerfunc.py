def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

aa = outer(4, 7)
print(aa)

def knights(saving):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saving)

bb = knights('Ni!')
print(bb)


def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('Duck')
b = knights2('Hasenpfeffer')
print(type(a))
print(a)
aa = a()
bb = b()
print(aa)
print(bb)


def edit_story(words, func1):
    for word in words:
        print(func1(word))

stairs = ['thud', 'meow', 'thud', 'hiss']

def enlive1(word1):
    return word1.capitalize() + '!'

edit_story(stairs, enlive1)

print('aaaaaaaaaaaaaaaaa')


edit_story(stairs, lambda word: word.capitalize()+'!')

def capchar(words, func):
    for word in words:
        print(func(word))

def aaa(word):
    return 'aaa()' + word.capitalize() + '!'

capchar(stairs, aaa)

capchar(stairs, lambda word: 'lambda: ' + word.capitalize() + '!')

print('sum(range(1,101)):', sum(range(1,101)))

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

for i in my_range(step=2, last=20, first=10):
    print(i)

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return new_function

def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
color_add_ints = document_it(add_ints)
color_add_ints(3,5)

@document_it
def add_ints1(a, b):
    return a + b

aa = add_ints1(4, 6)
print(aa)