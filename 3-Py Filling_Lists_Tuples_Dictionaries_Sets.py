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
print(d)
