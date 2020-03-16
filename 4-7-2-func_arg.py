def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

aa = menu('chardonnay','chicken','cake')
print(aa)

bb = menu(wine='bordeaux', entree='beef', dessert='bagel')
print(bb)

def menu(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

cc = menu('cs', 'pork')
print(cc)

dd = menu('cs', 'pork', 'abc')
print(dd)

# 기본 인자값은 실행될 때가 아닌 정의할때 계산
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

# 실행할 때마다 result = [] 초기화 됨
def works(arg):
    result = []
    result.append(arg)
    return result
aa = works('a')
bb = works('b')
print(aa)
print(bb)

# 가변 인자 : *
def print_args(*args):
    print('Positional argument tuple:', args)
print_args()
print_args(3,2,1,'Wait!','uh...')

def print_more(required1, required2, *args):
    print('Need this one: ', required1)
    print('Need this two: ', required2)
    print('all the rest: ', args)

print_more('cap','belf','watch','labtop')

# 키워드 인자 모의기 : **kwargs
def print_kwargs(**kwargs):
    print('Keyword argments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')

# docstring 예제
def echo(anything):
    'echo returns its input argument twice'
    return anything + anything

help(echo)
print(echo('abc'))
print(echo.__doc__)