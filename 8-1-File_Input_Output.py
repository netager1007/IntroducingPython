poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started ond day
In a relative way,
And returned on the previous night.'''

print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print('[print] ', poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()

try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('[Exception Error] relativity already exists!. That was a close one.')


# Text File Read : read(), readline(), readlines()
# read() : 인자 없이 호출하면 전체 파일을 읽을 수 있음. but, 메모리 관리에 신경 써야함.

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
print(len(poem))


# 문자를 다 읽어서 끝에 도달하면, read()는 빈 문자열('')을 반환. if not fragment에서 gragment가 False 가되어 not False는
# True 가 되어 while 문을 탈출함.

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))


# readline()
poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print('readline(): ', len(poem))

# text file을 가장 읽기 쉬운 방법은 이터레이터(iterator)를 사용하는 것.
# 이터레이터는 한번에 한 라인씩 반환한다.
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
print('iterator file read: ', len(poem))


# readlines()
fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print('readlines(): ', len(lines))
print('lines: ', lines)
print('lines[0]:', lines[0])
for line in lines:
    print(line, end='')