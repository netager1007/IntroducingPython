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

