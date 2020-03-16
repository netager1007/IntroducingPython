from collections import deque
def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('토마토'))
print(palindrome('aaba'))

def another_palindrom(word):
    print(word)
    print(word[::-1])
    return word == word[::-1]
print(another_palindrom('토마토마토'))


abc = 'abcdefghi'

print(abc)
print(abc[::-1])