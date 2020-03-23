# What Are Objects?
# -----------------


# Define a Class with class
# -------------------------
# You create an object from a class by calling the class name
# as though it were a function:
class Person():
    pass

someone = Person()

# Let’s try again, this time including the special Python
# object initialization method __init__:

class Person():
    def __init__(self):
        pass

# __init__() is the special Python name for a method that initializes an individual object
# from its class definition.

# When you define __init__() in a class definition, its first parameter should be self.
# Although self is not a reserved word in Python, it’s common usage.

# we’ll add the parameter name to the initialization method:
class Person():
    def __init__(self, name):
        self.name = name

# Now, we can create an object from the Person class by passing a string for the name parameter:
hunter = Person('Elmer Fudd')

# Here’s what this line of code does:
# 1. Looks up the definition of the Person class
# 2. Instantiates (creates) a new object in memory
# 3. Calls the object’s __init__ method, passing this newly-created object
#    as self and the other argument ('Elmer Fudd') as name
# 4. Stores the value of name in the object
# 5. Returns the new object
# 6. Attaches the name hunter to the object

# What about the name value that we passed in? It was saved with the object
# as an attribute. You can read and write it directly:
print('The mighty hunter: ', hunter.name)

# It is not necessary to have an __init__ method in every class definition;
# it’s used to do anything that’s needed to distinguish this object from others created
# from the same class.


# Inheritance
# -----------
# The solution is inheritance: creating a new class from an existing class
# but with some additions or changes. It’s an excellent way to reuse code.
# When you use inheritance, the new class can automatically use all the code
# from the old class but without copying any of it.

# You define only what you need to add or change in the new class,
# and this overrides the behavior of the old class.
# The original class is called a parent, superclass, or base class;
# the new class is called a child, subclass, or derived class.
class Car():
    pass

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

# give_me_a_yugo is an instance of class Yugo, but it also inherits whatever a Car can do.

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# Override a Method
# -----------------
# you’ll see how to replace or override a parent method.
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()

# In these examples, we overrode the exclaim() method.
# We can override any methods, including __init__().
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
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)


# Add a Method
# ------------
# The child class can also add a method that was not present in its parent class.
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

# But a generic Car object cannot:
try:
    give_me_a_car.need_a_push()
except AttributeError as e:
    print('[Exception Occured]:', e)


# Get Help from Your Parent with super
# ------------------------------------
# We saw how the child class could add or override a method from the parent.
# What if it wanted to call that parent method? “I’m glad you asked,” says super().
# We’ll define a new class called EmailPerson that represents a Person with an email address.
# First, our familiar Person definition:
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)     # Gets the definition of the parent class, Person
                                   # Calls the Person.__init__() method.
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

# We should be able to access both the name and email attributes:
print(bob.name)
print(bob.email)

# Why didn’t we just define our new class as follows?
class EmailPerson(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email

# We could have done that, but it would have defeated our use of inheritance.
# We used super() to make Person do its work, the same as a plain Person object would.
# There’s another benefit: if the definition of Person changes in the future,
# using super() will ensure that the attributes and methods that EmailPerson inherits
# from Person will reflect the change.
# Use super() when the child is doing something its own way but still needs something from the parent
# (as in real life).


# In self Defense
# ---------------
# Just for fun, you can even run it this way yourself and it will work the same as the normal (car.exclaim())

car = Car()
car.exclaim()

Car.exclaim(car)    # Check


# Get and Set Attribute Values with Properties
# --------------------------------------------
# Some object-oriented languages support private object attributes
# that can’t be accessed directly from the outside;
# programmers often need to write getter and setter methods
# to read and write the values of such private attributes.

# Python doesn’t need getters or setters, because all attributes
# and methods are public, and you’re expected to behave yourself.
# If direct access to attributes makes you nervous, you can certainly write
# getters and setters. But be Pythonic — use properties

# Example: Direct Change Nmae
class Car():
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

car = Car('SOON')
print(car.name)
car.name = 'LEE'    # I can chagne name directly
print(car.name)
car.set_name('CHEON')
print(car.name)     # Change name with Method

print('')
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('Inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        self.hidden_name = input_name

    name = property(get_name, set_name)    # Define these method as property of the name attribute

# The new methods act as normal getters and setters until that last line;
# it defines the two methods as properties of the attribute called name.
# The first argument to property() is the getter method, and the second is the setter.
# Now, when you refer to the name of any Duck object,
# it actually calls the get_name() method to return it:
fowl = Duck('Howard')
print(fowl.name)

# You can still call get_name() directly, too, like a normal getter method:
print(fowl.get_name())

print('')
# When you assign a value to the name attribute, the set_name() method will be called:
fowl.name = 'Daffy'
print(fowl.name)
#print(fowl.name)

# You can still call the set_name() method directly:
fowl.set_name('Daffy')
print(fowl.name)


# Another way to define properties is with decorators.
# In this next example, we’ll define two different methods,
# each called name() but preceded by different decorators:
# 1. @property, which goes before the getter method
# 2. @name.setter, which goes before the setter method
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

# If you don’t specify a setter property for an attribute, you can’t set it
# from the outside. This is handy for read-only attributes:
try:
    c.diameter = 20
except AttributeError as e:
    print('[Exception Occured]:', e)


# Name Mangling for Privacy
# -------------------------
# Python has a naming convention for attributes that should not be visible outside
# of their class definition: begin by using with two underscores (__).
# Let’s rename hidden_name to __name, as demonstrated here:
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

# Looks good. And, you can’t access the __name attribute:
try:
    print(fowl.__name)
except AttributeError as e:
    print('[Exception Occured]:', e)

# This naming convention doesn’t make it private, but Python does mangle the name
# to make it unlikely for external code to stumble upon it.
# If you’re curious and promise not to tell everyone, here’s what it becomes:
print(fowl._Duck__name)

# Notice that it didn’t print inside the getter. Although this isn’t perfect protection,
# name mangling discourages accidental or intentional direct access to the attribute.


# Method Types
# ------------
# 정적 메소드(Static Method, Class Method)
# 둘다 인스턴스를 만들지 않아도 class 메서드를 바로 실행 할 수 있음.

# static method
class hello:
    num = 10

    @staticmethod
    def calc(x):
        return x + 10
print(hello.calc(10))

# classmethod
class hello:
    num = 10

    @classmethod
    def calc(cls, x):
        return x + 10
print(hello.calc(10))

# 둘 다 객체를 만들지 않고 바로 해당 메서드를 사용 함.
# 차이점은 calc 메서드를 만들때 cls 인자가 추가 된 거임.

# 이제 개념적인 차이점을 살펴보자.  만약 hello 클래스의 num 속성에 접근하려면?
# 우선 객체가 아니므로 self.num을 사용할 수 없음.

# staticmethod
class hello:
    num = 10

    @staticmethod
    def calc(x):
        return x + 10 + hello.num
print(hello.calc(10))

# 정적 변수로 접근. 좋아 보이지 않음.

# classmethod
class hello:
    num = 10

    @classmethod
    def calc(cls, x):
        return x + 10 + cls.num
print(hello.calc(10))

# classmethod는 cls가 있는데 이것은 '클래스'를 가리킨다.
# 이것으로 클래스의 어떤 속성에도 접근할 수 있다.
# 위 예시 경우 또한 cls.num을 통해 hello 클래스의 num 속성에 접근했다.

# 만약 상속 관계가 있는 클래스들에선 cls가 가리키는 클래스는 어떤 클래스일까?
class hello:
    t = '내가 상속해 줬어'

    @classmethod
    def calc(cls):
        return cls.t

class hello_2(hello):
    t = '나는 상속 받았어'

print(hello_2.calc())



class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, 'little objects')

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This Coyote Weapon has been brought to you by Acme')

CoyoteWeapon.commercial()


# Abstract class(추상 메서드)
# --------------------------
# Python 3.3 에서 추상 메서드 방법이 변경된 것 같음.

# 잘 만들어진 class는 잘 사용되도록 만들어져있다.
# class로 만들었다면 class에서 정의된 메서드를 있는 그대로 사용하지 않을 것이다.
# 반드시 상속받아 class변수를 추가하거나 메서드를 추가할 것이고 어떤 메서드는 오버라이드 해야 할 것이다.
# 그래야만 class로 만든 의미가 있다. 확장된 기능을 만들면서 통일된 체계를 구축하는 것이 class의 개념이다.

# 이런 개념을 유지하기 위해 class를 만들 때 반드시 구현 해야 할 메서드를 class에 명시할 수 있다.
class Car:
    def turnning(cls):
        raise NotImplementedError

class Sonaty(Car):
    def turnning(self):
        print('turnning finish')

class test_car(Car):
    pass

sonaty = Sonaty()
sonaty.turnning()

t_car = test_car()
try:
    t_car.turnning()
except NotImplementedError as e:
    print('[Exception Occured]:', e)

# 위와 같이 하면 상속받은 Sonaty class에서 turnning메서드를 구현하지 않으면 에러가 발생한다.
# raise NotImplementedError가 이런 역할을 한다.

# 이보다 좀 더 세련된 방법이 있음.
# import abc

# class Car:
#     @abc.abstractclassmethod

# Duck Typing
# -----------
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

# We didn’t change how QuestionQuote or ExclamationQuote were initialized,
# so we didn’t override their __init__() methods.
# Python then automatically calls the __init__() method of the parent class Quote
# to store the instance variables person and words.

# That’s why we can access self.words in objects created from the subclasses
# QuestionQuote and ExclamationQuote.
hunter = Quote('Elmer Fudd', "I'm huntering wabbits")
print(hunter.who(), 'says', hunter.says())

hunter1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunter1.who(), 'says', hunter1.says())

hunter2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunter2.who(), 'says', hunter2.says())

# Three different versions of the says() method provide different behavior for the three classes.
# This is traditional polymorphism(다형성) in object-oriented languages.

class BabblingBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Babble'

brook = BabblingBrook()

# Now, run the who() and says() methods of various objects, one (brook) completely unrelated to the others:

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunter1)
who_says(hunter2)
who_says(brook)

# This behavior is sometimes called duck typing.


# Special Methods
# ---------------
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

# We defined the method equals() to do this lowercase conversion and comparison.

# It would be nice to just say if first == second, just like Python’s built-in types.
# So, let’s do that. We change the equals() method to the special name __eq__() (you’ll see why in a moment):
class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, words):
        print('Word.__eq__')
        return self.text.lower() == words.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)

# Magic methods for comparison
# 1. __eq__(self, other)     self == other
# 2. __ne__(self, other)     self != other
# 3. __lt__(self, other)     self <  other
# 4. __gt__(self, other)     self >  other
# 5. __le__(self, other)     self <= other
# 5. __ge__(self, other)     self >= other

# Magic methods for math
# 1. __add__(self, other)      self +  other
# 2. __sub__(self, other)      self -  other
# 3. __mul__(self, other)      self *  other
# 4. __floordiv__(self, other) self // other
# 5. __truediv__(self, other)  self /  other
# 6. __mod__(self, other)      self %  other
# 7. __pow__(self, other)      self ** other

# Other, miscellaneous magic methods
# 1. __str__(self)     str(self)
# 2. __repr__(self)    repr(self)
# 3. __len__(self)     len(self)

first = Word('ha')
print(first)

class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, words):
        return self.text.lower() == words.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word('" self.text "')'


# >>> first = Word('ha')
# >>> first               # Uses __repr__ , Return : Word("ha")

# >>> print(first)        # Uses __str__,   Return : ha


# Composition
# -----------
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print("This duck has a", self.bill.description, "bill and a", self.tail.length, "tail")

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()

# When to Use Classes and Objects versue Modules

# Here are some guidelines for deciding whether to put your code in a class or a module:

# 1. Objects are most useful when you need a number  of individual instances that have similar behavior methods),
#    but differ in their internal states(attributes).
# 2. Classes support inheritance, modules don’t.
# 3. If you want only one of something, a module might be best. No matter how many times a Python module is
#    referenced in a program, only one copy is loaded. (Java and C++ programmers: if you’re familiar with
#    the book Design Patterns: Elements of Reusable Object-Oriented Software by Erich Gamma,
#    you can use a Python module as a singleton.)
# 4. If you have a number of variables that contain multiple values and can be passed as arguments to multiple
#    functions, it might be better to define them as classes. For example, you might use a dictionary with keys
#    such as size and color to represent a color image. You could create a different dictionary for each image
#    in your program, and pass them as arguments to functions such as scale() or transform(). This can get messy
#    as you add keys and functions. It’s more coherent to define an Image class with attributes size or
#    color and methods scale() and transform(). Then, all the data and methods for a color image are defined in
#    one place.
# 5. Use the simplest solution to the problem. A dictionary, list, or tuple is simpler, smaller, and faster than
#    a module, which is usually simpler than a class.

# Guido’s advice:
# ---------------
# Avoid overengineering datastructures. Tuples are better than objects (try namedtuple too though).
# Prefer simple fields over getter/setter functions ...
# Built-in datatypes are your friends. Use more numbers, strings, tuples, lists, sets, dicts.
# Also check out the collections library, esp. deque.
#                                                                            — Guido van Rossum


# Named Tuples
# ------------
# A named tuple is a subclass of tuples with which you can access values by name (with .name) as well as
# by position (with [ offset ]).

# Let’s take the example from the previous section and convert the Duck class to a named tuple,
# with bill and tail as simple string attributes. We’ll call the namedtuple function with two arguments:
# 1. The name
# 1. A string of the field names, separated by spaces

# Named tuples are not automatically supplied with Python, so you need to load a module before using
# them. We do that in the first line of the following example:
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orage', 'long')
print(duck)

print(duck.bill)
print(duck.tail)

# You can also make a named tuple from a dictionary:
Duck = namedtuple('Duck', 'bill tail')
parts = {'bill': 'wide orage', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
print(duck3)

# We could have defined duck as a dictionary:
duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)

# You can add fields to a dictionary:
duck_dict['color'] = 'green'
print(duck_dict)

# But not to a named tuple:
from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orage', 'long')
try:
    duck.color = 'green'
except AttributeError as e:
    print('[Exception Occured]:', e)

# To recap, here are some of the pros of a named tuple:
# 1. It looks and acts like an immutable object.
# 2. It is more space- and time-efficient than objects.
# 3. You can access attributes by using dot notation instead of dictionary-style square brackets.
# 4. You can use it as a dictionary key.

# 파이썬만의 특별한 클래스 작성 기법(namedtuple)
# -------------------------------------------
# - 클래스없이 객체를 생성할 수 있는 방법 - 클래스에 attribute만 있는 경우에 해당 함.
import collections

# C언어는 변수를 묶어서 하나의 변수로 쓸 수 있는데, 파이썬에서는 이와 같은 방식으로 사용 가능.
# struct student {
#    int id:
#    char *name;
# };

# int main() {
#    struct student s;
#    s.id = 1;
#    s.name = '김철수';
# }

# 사용법 in Python
# 클래스명 = collections.namedtuple('실제 클래스명', [각 튜플 데이터 이름 리스트])
# Employee = collections.namedtuple('Person', ['name', 'id'])
# 클래스명 = collections.namedtuple('실제 클래스명', '각 튜플 데이터 이름을 한칸씩 띄우면서 나열')
# Employee = collections.namedtuple('Person', 'name id')
Employee = collections.namedtuple('Employee', ['name', 'id'])    # 리스트로 써도 되고!
employee1 = Employee('Dave', '4011')
print(employee1)
print(type(employee1))

Employee = collections.namedtuple('Employee', 'name id')        # 스트링처럼 써도 됨
employee1 = Employee('LEE', '4022')
print (employee1)
print (type(employee1))

# 속성을 다루는 방법
Employee = collections.namedtuple('Employee', ['name', 'id'])

employee1 = Employee('Dave', '4011')
employee2 = Employee('David', '4012')

# 일반적인 튜플 처럼 속성 접근 (권장하지는 않음, 추후 일반 클래스로 바꾼다면 관련 코드를 모두 변경해야함)
print(employee1, employee1[0], employee1[1])
print(employee2.name, employee2.id)
name, id = employee2
print(name, id)


# 초간단 연습1
# 1. 직장인 이름, 나이, 부서를 속성으로 갖는 기존과 같은 방식으로 class를 만들고,
# - 세 개의 객체를 임의 속성값과 함께 넣어보고, 각각을 출력해보기
# 2. 이번에는 직장인 이름, 나이, 부서를 속성으로 갖는 class를 namedtuple 로 정의하고,
# - 세 개의 객체를 임의 속성값과 함께 넣어보고, 각각을 출력해보기
class EmployeeClass:
    def __init__(self, name, id, org):
        self.name = name
        self.id = id
        self.org = org

employee2 = EmployeeClass('Dave', '4011', 'sales')
print(employee2.name, employee2.id, employee2.org)

Employee = collections.namedtuple('Employee', ['name', 'id', 'org'])
employee1 = Employee('David', '4012', 'consult')
print(employee1.name, employee1.id, employee1.org)

# typing.NamedTuple
# -----------------
# 파이썬 3.6에서 추가된 클래스 (collections.namedtuple 의 개선 방식?)
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    id: int

employee1 = Employee('Guido', 2)
print(employee1)
print(employee1.name, employee1.id)
print(employee1[0], employee1[1])

# 디폴트값도 선언할 수 있음.
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    id: int = 3

employee1 = Employee('Guido')
print(employee1)
print(employee1.name, employee1.id)
print(employee1[0], employee1[1])


from typing import NamedTuple

class Employee(NamedTuple):
    name: str = 'Guido'
    id: int = 3

employee1 = Employee()
employee2 = Employee('Dave', 4)

print(employee1)
print(employee1.name, employee1.id)
print(employee2.name, employee2.id)
