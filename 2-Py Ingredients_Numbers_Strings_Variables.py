# Variable names can only contain these characters:
# Lowercase letters (a through z)
# Uppercase letters (A through Z)
# Digits (0 through 9)
# Underscore (_)
# Names cannot begin with a digit. Also, Python treats names that begin with an
# underscore in special ways(which you can read about in Chapter 4).

# Here’s how to get both the (truncated) quotient and remainder at once:
print(divmod(9, 5))  # Return a two-item result called a tuple
print(9//5)
print(9%5)
print(9/5)

# In Python, you can express literal integers in three bases besides decimal:
# 0b or 0B for binary(base 2)
# 0o or 0O for octal(base 8)
# 0x or 0X for hex(base 16)


## Type Conversions

print(int(True))
print(int(False))
print(int(98.6))
print(int(1.0e4))
print(int(1.0E4))
print(int('99'))
print(int('-23'))
print(int('+12'))
try:
    print(int('99 bottles of beer on the wall'))
except ValueError as e:
    print('[Exception Occured]:', e)

# int() will make integers from floats or strings of digits, but won’t handle strings
# containing decimal points or exponents:
try:
    print(int('98.6'))
except ValueError as e:
    print('[Exception Occured]:', e)

# If you mix numeric types, Python will sometimes try to automatically convert them for you:
print(4 + 7.0)    # Return float type

# The boolean value False is treated as 0 or 0.0 when mixed with integers or floats,
# and True is treated as 1 or 1.0:
print(True + 2)
print(False + 5.0)


## Floats
print(float('98.6'))
print(float('-1.5'))
print(float('1.0e4'))


## Strings
print("'Nay,' said the naysayer.")

# print() strips quotes from strings and prints their contents. It’s meant for human output.
# It helpfully adds a space between each of the things it prints, and a newline at the end:
print(99, 'bottls', 'would be enough.')

# Why would you need an empty string? Sometimes you might want to build a string from other strings,
# and you need to start with a blank slate.
bottles = 99
base = ''
base += 'current inventory:'
base += str(bottles)
print(base)


## Convert Data Types by Using str()
print(str(98.6))      # Return: '98.6'
print(str(1.0e4))     # Return: '10000.0'
print(str(True))      # Return: 'True'

# Python uses the str() function internally when you call print() with objects that
# are not strings and when doing string interpolation, which you’ll see in Chapter 7.


# Escape with \
palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)

# You will see the escape sequence \t (tab) used to align text:
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)

speech = 'Today we honor our friend, the backslash:\\.'
print(speech)

# Combine with +
print('Release the kraken! ' + 'At once!')
print("My word! " "A gentleman caller!")

# It does add a space between each argument to a print() statement, and a newline at the end:
a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a + b +c)
print(a, b, c)

# Duplicate with *
# You use the * operator to duplicate a string.
start = 'Na '* 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

# Extract a Character with []
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])
print(letters[25])
try:
    print(letters[100])
except IndexError as e:
    print('[Exception Occured]:', e)

name = 'Henny'
try:
    name[0] = 'P'
except TypeError as e:
    print('[Exception Occured]:', e)

# Instead you need to use some combination of string functions such as replace() or
# a slice (which you’ll see in a moment):
name = 'Henny'
tempname = name.replace('H', 'P')
print(tempname)         # Return: 'Penny'
print(name)             # Return: 'Henny'
print('P' + name[1:])


# Slice with [start:end:step]
# [:] extracts the entire sequence from start to end.
# [ start :] specifies from the start offset to the end.
# [: end ] specifies from the beginning to the end offset minus 1.
# [ start : end ] indicates from the start offset to the end offset minus 1.
# [ start : end : step ] extracts from the start offset to the end offset minus 1,
#   skipping characters by step.

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[10:])
print(letters[12:15])
print(letters[-3:])

# ending at –3 actually stops at –4, the w:
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])

# And that’s not all! Given a negative step size, this handy Python slicer can also
# step backward. This starts at the end and ends at the start, skipping nothing:
print(letters[-1::-1])
print(letters[::-1])

# Slices are more forgiving of bad offsets than are single-index lookups.
# A slice offset earlier than the beginning of a string is treated as 0,
# and one after the end is treated as -1, as is demonstrated in this next
# series of examples.
print(letters[-50:])
print(letters[-51:-50])    # Return: ''
print(letters[:70])
print(letters[70:71])      # Return: ''

# Get Length with len()

# The len() function counts characters in a string:
print(len(letters))
empty=''
print(len(empty))    # Return: 0

# Split with split()
todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(','))       # Return: list data type

# If you don’t specify a separator, split() uses any sequence of white space
# characters—newlines, spaces, and tabs.

# Combine with join()  ~ Opposit of split()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ','.join(crypto_list)
print('Found and signing book deals:', crypto_string)
crypto_string = '\n'.join(crypto_list)
print('Found and signing book deals:', crypto_string)

# Playing with Strings
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))

print(poem.startswith('All'))      # Return: True
print(poem.endswith("That's all, folks!"))    # Return: False
print(poem.endswith("bt."))    # Return: True

# Now, let’s find the offset of the first occurrence of the word the in the poem:
word = 'the'
print(poem.find(word))
word = 'low'
print(poem.find(word))

# And the offset of the last the:
word = 'the'
print(poem.rfind(word))

# How many times does the three-letter sequence the occur?
word = 'the'
print(poem.count(word))

# Are all of the characters in the poem either letters or numbers?
print(poem.isalnum())    # Return: False

# Case and Alignment

# Remove . sequences from both ends: str.strip()
setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup)

# Capitalize the first word:
print(setup.capitalize())

# Capitalize all the words:
print(setup.title())

# Convert all characters to uppercase:
print(setup.upper())

# Convert all characters to lowercase:
print(setup.lower())

# Swap upper- and lowercase:
print(setup.swapcase())

# Center the string within 30 spaces:
print(setup.center(30))

# Left justify:
print(setup.ljust(30))

# Right justify:
print(setup.rjust(30))


## Substitute with replace()
setup = 'a duck goes into a bar...'
print(setup.replace('duck', 'marmoset'))

# Change up to 100 of them:
print(setup.replace('a ', 'a famous ', 100))

print(setup.replace('a', 'a famous', 100))


# More String Things








