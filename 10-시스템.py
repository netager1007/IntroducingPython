# 10.1 파일

# 10.1.1 생성하기: open()
fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)  # print() 에서 file write
fout.close()

# 10.1.2 존재여부 확인하기: exists()
import os
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))           # 현재 Dir
print(os.path.exists('..'))          # 상위(부모) Dir

# 10.1.3 타입 확인하기: isfile()
# isfile() : 파일 인지
# isdir()  : 디렉터리 인지
# isabs()  : 절대경로 인지 확인
name = 'oops.txt'
print('os.path.isfile(name): ', os.path.isfile(name))
print('os.path.isdir(name): ', os.path.isdir(name))
print('os.path.isabs("."): ', os.path.isabs('.'))
print('os.path.isabs(name): ', os.path.isabs(name))
print('os.path.isabs("/big/fake/name"): ', os.path.isabs("/big/fake/name"))
print('os.path.isabs("big/fake/name"): ', os.path.isabs("big/fake/name"))

# 10.1.4 복사하기: copy() in shutil module
import shutil
shutil.copy('oops.txt', 'ohno.txt')

# shutil.move() 함수는 파일을 복사한 후 원본 파일을 삭제
import shutil
shutil.move('oops.txt', 'ohno1.txt')

# 10.1.5 이름 바꾸기: rename()
import os
os.rename('ohno.txt', 'oops.txt')

# 10.1.6 연결하기: link(), symlink() in Unix, Linux
# link()    : 하드 링크 생성
# symlink() : 심벌릭 링크 생성
# islink()  : 심벌릭 링크인지 확인
if os.path.isfile('yikes.txt'):
    os.remove('yikes.txt')

os.link('oops.txt', 'yikes.txt')
print('os.path.isfile("yikes.txt"): ', os.path.isfile('yikes.txt'))
# print('os.path.islink("yikes.txt"): ', os.path.islink('yikes.txt'))  # islink() : Check symbolic link

# os.symlink('oops.txt', 'jeepers.txt') # In Windows, Can't use it

# 10.1.7 퍼미션 바꾸기: chmod()
# os.chmod('oops.txt', 0o444)

import stat
# os.chmod('oops.txt', stat.S_IRUSR)

# 10.1.8 오너십 바꾸기: chown()
# chown()은 unix/linux/mac에서 사용
#uid = 5
#gid = 22
#os.chown('oops', uid, gid)

# 10.1.9 절대경로 얻기: abspath()
print('os.path.abspath("oops.txt"): ', os.path.abspath("oops.txt"))

# 10.1.10 심벌릭 링크 경로 얻기: realpath()
# os.path.realpath('jeepers.txt')

# 10.1.11 삭제하기: remove()
os.remove('oops.txt')
print("os.path.exist('oops.txt'): ", os.path.exists('oops.txt'))


# 10.2 디렉터리(Directory)
# 10.2.1 생성하기: mkdir()
try:
    os.mkdir('poems')
except FileExistsError as e:
    print('Error: ', e)

print("os.path.exists('poems'): ", os.path.exists('poems'))

# 10.2.2 삭제하기: rmdir()
try:
    os.rmdir('poems')
except:
    print('Error Occured')
print("os.path.exists('poems'): ", os.path.exists('poems'))

# 10.2.3 콘텐츠 나열하기: listdir()
if not os.path.isdir('poems'):
    os.mkdir('poems')
print("os.listdir('poems'): ", os.listdir('poems'))
if not os.path.isdir('poems'):
    os.mkdir('poems/mcintyre')
print("os.listdir('poems'): ", os.listdir('poems'))

with open('poems/mcintyre/the_good_man', 'wt') as fout:
    fout.write('''Cheerfule and happy wsa his mood,
    He to the poor was
    And he oft' times
    Also''')
print("os.listdir('poems/mcintyre'): ", os.listdir('poems/mcintyre'))

# 10.2.4 현재 디렉터리 바꾸기: chdir()
import os
os.chdir('poems')
print(os.listdir('.'))

# 10.2.5 일치하는 파일 나열하기: glob()
# glob() 함수는 복잡한 정규식 표현이 아닌, 유닉스 쉘 규칙을 사용하여 일치하는 파일이나
# 디렉터리의 이름을 검색.
import glob
print("glob.glob('m*'): ", glob.glob('m*'))
print("glob.glob('??'): ", glob.glob('??'))
print("glob.glob('m??????e'): ", glob.glob('m??????e'))
print("glob.glob('[klm]*e'): ", glob.glob('[klm]*e'))


# 10.3 프로그램과 프로세스
import os
print('os.getpid(): ', os.getpid())
print('os.getcwd(): ', os.getcwd())
# print('os.getuid(): ', os.getuid())     # In Unix
# print('os.getugid(): ', os.getugid())   # In Unix

# 10.3.1 프로세스 생성하기(1): subprocess
import subprocess
ret = subprocess.getoutput('date')
ret



