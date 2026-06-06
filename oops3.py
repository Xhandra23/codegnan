'''
polymorphism
------------
-->this means "many forms".. it allows the same function,method ,or opertor to
behave differently depending on the object..

1. method overloading
---------------------
--> method overloading means defining multiple methods with same but different parameters
eg.
--
class calu:
    def add(self,a ,b,c=0):
        return a + b +c
a=calu()
print(a.add(23,45))
print(a.add(23,985,234))

eg.
---
class calu:
    def add(self,a ,b):
        return a + b 
    def add(self,a,b,c=0):
        retrun a+b+c
a=calu()
print(a.add(23,45))
print(a.add(23,985,234))

2.method overriding
-------------------
-->this occurs when a child class provides its own implemention of a  method
already defined in the parent class...
eg.
---
class animal:
    def sound(self):
        print("it can sound")
class dog:
    def sound(slef):
        print("it can darks")
u = dog()
u.sound()

3.operator overloading
-----------------------
-->this  allows operators such as +,-,* etc,, to perform  different actions
for user-defined objects


note:-
------
--> the operator inside the method will overload a special method or operator
given in  the call
eg.
---
class stu:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,others):
        return self.marks  others.marks
so1=stu(34)
so=stu(234)
print(so1+so)

4.Data Abstraction
------------------
-->this is the process of hiding internsl implementation details and
showing only essential features to the user
--> it focuses on what an object does rather than how it does it ..



'''
from abc import ABC, abstractmethod
class shape(ABC):

    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class rec(shape):
    def __init__(self,a,b):
        self.a =a
        self.b =b
    def area(self):
        return self.a*self.b
    def parimeters(self):
        return 2*(self.a*self.b)
an = rec(10,5)
an.area()
an.parimeters()










