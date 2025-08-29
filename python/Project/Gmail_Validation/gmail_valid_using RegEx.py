"""Gmail  Validation Using Regular Expresion"""
import re
#1.start with (a-z)
#2.(0-9)
#3._. one time
#4.@ one time
#5. . last 2 or 3 indes

# email_Gen="^[a-z]+[\._]?[a-z,0-9]+[@]\w+[.]\w{2,3}$"
# email=input("Please! Enter your valid Gmail: ")
# if re.search(email_Gen,email):
#     print("Right Email")
# else:
#     print("Wrong Email")

"""Invalide code becouse Regular Exprestion only work for String(include phone number,gmail)"""
import re
# number="[a/b==0]"
# a, b=input("Enter your two number :").split()

# if re.search(number,a,b):
#     print("even")
# else:
#     print("Odd")
"""Phone number validation for bangladesh"""
phone=input("Enter your phone number: ")
pattern=r"\d{11}"

if re.search(pattern,phone):
    print("your phone number is: ",phone)
else:
    print("Your phone number invalide. Please try again")