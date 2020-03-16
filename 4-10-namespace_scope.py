animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
print_global()

def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

print('before:', animal)
change_and_print_global()
print('after:', animal)

animal = 'fruitbat'
def change_local():
    animal = 'wombat'
    print('locals:', locals())
    print('globals:', globals())

change_local()

def amazing():
    '''
    this is the amazing func.
    Want to see it again?
    '''
    print('This func is named :', amazing.__name__)
    print('And its docstrings is:', amazing.__doc__)

amazing()

print(amazing.__doc__)

short_list = [1,2,3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and ', len(short_list)-1, 'but got', position)

short_list = [1,2,3]
while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something wrong:', other)

class UppercaseException(Exception):
    pass

words = ['eeenie','meenie','miny','mo','E']
for word in words:
    if word.isupper():
        raise UppercaseException(word)


class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)