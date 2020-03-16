class Person():
    def __init__(self, name):
        self.name = name
class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor" + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
layer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(layer.name)

class Car():
    def exclaim(self):
        print("I'm a Car")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yogo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print('A little help here?')

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email

bob = EmailPerson('Bob Frapples','bob@naver.com')
print(bob.name)
print(bob.email)

# self
class Car():
    def exclaim(self):
        print("I'm a Car")

car = Car()
car.exclaim()

Car.exclaim(car)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('Inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        self.hidden_name = input_name
    name = property(get_name, set_name)
fowl = Duck('Howard')
print('fowl.name:', fowl.name)
fowl.name = 'Daffy'
print('fowl.name:', fowl.name)
fowl.set_name('Daffy1')
print(fowl.name)

class Duck() :
    def __init__(self, input_name) :
        self.hidden_name = input_name

    @property
    def name(self):
          print('inside the getter')
          return self.hidden_name

    @name.setter
    def name(self, input_name):
          print('inside the setter')
          self.hidden_name = input_name

    fowl = Duck('Howard')
    print(fowl.name)

    fowl.name = 'Donald'
    print(fowl.name)

class Cicle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

c = Cicle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.diameter)

class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('Inside the getter')
        return self.__name

    @name.setter
    def name(self, input_name):
        print('Inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)

fowl.name = 'Donald'
print(fowl.name)

#print(fowl.__name)

print(fowl._Duck__name)


class A():
    count = 0
    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
easy_a.kids()
aa = A()
aa.kids()

# 덕 타이핑
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd',"I'm hunting rabbits" )
print(hunter.who(), hunter.says())

hunter1 = QuestionQuote('Bug Bunny', "What's up, doc")
print(hunter1.who(), hunter1.says(), hunter1.says())

hunter2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunter2.who(), hunter2.says(), hunter2.says())


class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook = BabblingBrook()
print(brook.who())
print(brook.says())

def who_says(obj):
    print(obj.who(), obj.says())

who_says(hunter)
who_says(hunter1)
who_says(brook)

class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, words):
        return self.text.lower() == words.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, words):
        return self.text.lower() == words.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)


class bill():
    def __init__(self, description):
        self.description = description

class tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print("aaa")
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, "tail")

tail = tail('long')
bill = bill('wide orange')
duck = Duck(bill, tail)
duck.about()

# Named tuple
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orage', 'long')
print(duck)
