'''import re

name = input("Enter your name: ")
mobile = input("Enter 10 digit number: ")
password = input("Enter your password: ")
email = input("Enter your email id: ")

# Name
if re.fullmatch(r'[a-zA-Z ]+', name):
    print("Valid name")
else:
    print("Invalid name")

# Mobile
if re.fullmatch(r'[6-9][0-9]{9}', mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")

# Password
if re.fullmatch(r'(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&*])[A-Za-z\d@#$%^&*]{8,16}', password):
    print("Valid password")
else:
    print("Invalid password")

# Email
if re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}', email):
    print("Valid email")
else:
    print("Invalid email")
'''
import re

class UserValidation:

    def __init__(self, name, mobile, password, email):
        self.name = name
        self.mobile = mobile
        self.password = password
        self.email = email

    def validate_name(self):
        if re.fullmatch(r'[a-zA-Z ]+', self.name):
            print("Valid Name")
        else:
            print("Invalid Name")

    def validate_mobile(self):
        if re.fullmatch(r'[6-9][0-9]{9}', self.mobile):
            print("Valid Mobile Number")
        else:
            print("Invalid Mobile Number")

    def validate_password(self):
        if re.fullmatch(r'(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^&*])[A-Za-z\d@#$%^&*]{8,16}', self.password):
            print("Valid Password")
        else:
            print("Invalid Password")

    def validate_email(self):
        if re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}', self.email):
            print("Valid Email")
        else:
            print("Invalid Email")

    def validate_all(self):
        self.validate_name()
        self.validate_mobile()
        self.validate_password()
        self.validate_email()


name = input("Enter your name: ")
mobile = input("Enter mobile number: ")
password = input("Enter password: ")
email = input("Enter email: ")

obj = UserValidation(name, mobile, password, email)
obj.validate_all()
