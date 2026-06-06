'''
Inheritance
-----------
--> this alloes one class to aquire the properties and methods of another class...
types
-----

1.single inheritance
----------------------
--> a class inherts from a single parent class..

               parent
                  |
                  |
                child


eg.
--
class father:
    def land(self):
        print(" i am have 23 acerS")

class my(father):
    def my_(self):
        print("nothing")
fam = my()
fam.land()

2.multiple inheriatance
------------------------
-->a class inherts from a more one class parent classs..



               parent       mother
                  |           |
                  |           |
                  -------------
                        |
                      child

eg.
---

class father:
    def land(self):
        print(" i am have 23 acerS")
class mother:
    def gold(self):
        print("20 kg of golds")

class my(father,mother):
    def my_(self):
        print("nothing")
fam = my()
fam.land()
fam.gold()


3.muilt-level inheritance
--------------------------
--> a class inherts from a parent class and another class inherts from that child
class

4. hierarchical inheritance
5. hybride inheritance
'''




class grandfather:
    def land(self):
        print(" i am have 23 acerS")
class mother(grandfather):
    def gold(self):
        print("20 kg of golds")

class my(mother):
    def my_(self):
        print("nothing")
fam = my()
fam.land()
fam.gold()
fam.my_()








