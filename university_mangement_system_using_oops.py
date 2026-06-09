'''class Person:
    university = "Codegnan University"
    def  __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def display(self):
        pass
class Stu(Person):
    def __init__(self,name,age,dept,branch,studentid):
        super().__init__(name,age,dept)
        self.branch=branch
        self.studentid=studentid
    def display(self):
        print(f"Name :{self.name} |Age :{self.age} |Branch :{self.branch} |studentid: {self.studentid} | univ:{self.university}")
class Faculty(Person):
    def __init__(self,name,age,dept,facultyid):
        super().__init__(name,age,dept)
        self.facultyid=facultyid
    def display(self):
        print(f"Name :{self.name} |Age :{self.age} |Branch :{self.dept} |studentid: {self.facultyid}")
f1=Faculty(input("Enter Name: "),int(input("Enter Age: ")),input("Enter Branch: "),input("Enter ID: "))
f1.display()
s1=Stu(input("Name: "),int(input("age:")),input("dept:"),input("faccs"))
s1.display()
'''
class Person:
    university = "Codegnan University"

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        pass


class Stu(Person):
    def __init__(self, name, age, dept, branch, studentid):
        super().__init__(name, age, dept)
        self.branch = branch
        self.studentid = studentid

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Branch: {self.branch} | Student ID: {self.studentid} | Univ: {self.university}")


class Faculty(Person):
    def __init__(self, name, age, dept, facultyid):
        super().__init__(name, age, dept)
        self.facultyid = facultyid

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Dept: {self.dept} | Faculty ID: {self.facultyid}")

s1 = Stu(
    input("Enter Name: "),
    int(input("Enter Age: ")),
    input("Enter Dept: "),
    input("Enter Branch: "),
    input("Enter Student ID: ")
)
s1.display()

f1 = Faculty(
    input("Enter Name: "),
    int(input("Enter Age: ")),
    input("Enter Dept: "),
    input("Enter Faculty ID: ")
)
f1.display()

