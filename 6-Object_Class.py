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


import os
os.exit()


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
