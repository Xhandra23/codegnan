'''
#oops
-----
1.class
-------
--> a class is a blueprint or template used to create object
eg.
---
class stu:
    name= "teja"

2.odject
--------
--> an odject is an instance of a class
eg.
---
class stu:
    name = "teja"
s1 =stu()
print(s1.name)\


3. attribtes
------------
-->attributes are the variables that belongs to a class or an object
eg.
---
class stu:
    name = "teja"
    age=45
    
s1 =stu()
print(s1.name)
print(s1.age)

4.methods
---------
--> the functions defined inside the class is methods
eg.
---
class pfs_da:
    def python(self):
       pfs_da = "bacth_03"
       print("this pfs and da batch03")
    def Flask(self):
        pfs =  "bacth_03"
        print("this pfs bacth03")

all=pfs_da()
all.python()
all.Flask()

5.constructor
-------------
--> a constructor is a special method that is automatically called when an object is created

eg.
---
class ATM:
    def int__(self,balance,name):
        self.balance = balance
        self.name = name

    def Bal_check(self):
        print(f"{self.name} your total balance is {self.balance}")
card = ATM(balance = 50000,name ="chandu")
card.int__()
card.Bal_check()

6. access specifers
-------------------
1.public
-->this can be accessed from anywhere in the program
eg.
---
class stu:
    name = "teja"
s1=stu()
print(s1.name)


2.protected
-->this is represented using a single underscore(_)
class stu:
    _name = "teja"
s1=stu()
print(s1._name)

3.private
---------
--> this is represented using a single Underscore(__)
eg.
--
class stu:
    __name = "teja"
s1=stu()
print(s1._stu__name)


7.encapsulation
--------------
--> is the process of binding data and methods together










'''
class Bank:
    def __int__(self,balance):
        self.__balance = balance

    def depo_(self,amount):
        self.__balance +=amount

    def get_bala(self):
        return self.__balance
acc = Bank(1000)
acc.depo_(1000)
print(acc.get_bala())


















        
    
    
