number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list = []
for number in range(1,6):
    number_list.append(number)
print(number_list)

number_list = list(range(1,6))
print(number_list)

## So Pythonic : List 저장할 값을 연산할 수 있음. 또한 조건도 줄 수 있음.
number_list = [number for number in range(1,6)]
print(number_list)

number_list = [number ** 2 for number in range(1,6)]
print(number_list)

a_list = [number for number in range(1,6) if number %2 == 1]
print(a_list)

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

# Nested Loop Comprehension
rows = range(1, 4)
cols = range(1, 3)

for row in rows:
    for col in cols:
        print(row, col)

rows = range(1, 4)
cols = range(1, 3)

cells = [(row, col) for row in rows for col in cols]
print(cells)
print(cells[0][0])

for row, col in cells:
    print (row, col)


# Dictionary Comprehensions
# -------------------------
#  { key_expression:value_expression for expression in iterable }
# ---------------------------------------------------------------
word = 'letters'
letter_counts = {letter:word.count(letter) for letter in word}
print(letter_counts)

letter_counts = {letter:word.count(letter) for letter in set(word)}
print(letter_counts)

# Set Comprehensions
# ------------------
#  { expression for expression in iterable }
# ---------------------------------------------------------------
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# Generator Comprehensions
# ------------------------
# { expression for expression in iterable }
# A generator can be run only once. Lists, sets, strings, and dictionaryies exist in memory,
# but generator creates it values on the fly and hands them out one at a time through an iterator.
# ------------------------------------------------------------------------------------------------
number_thing = (number for number in range(1, 6))
print(type(number_thing))

for number in number_thing:
    print(number)

# 위에서 number_thing Generator를 사용해서 아래에서는 없음.
number_list = list(number_thing)
print(number_list)


