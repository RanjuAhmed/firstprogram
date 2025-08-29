'''if statement'''
# x=34
# y=44
# if x<y:
#     print(f"{y} is gretter then {x}")


'''else statements'''
# if x>y:
#     print(f"{x} is gretter then {y}")
# else:
#     print(f"{y} is gretter then {x}")

'''if elif else'''
# a=3
# b=4
# if(a>b):
#     print(f"{a} is gretter then {b}")
# elif a<b:
#     print(f"{b} is gretter  then {a}")
# else:
#     print(f"{a} and {b} are equal")


'''Nested If'''
# t=45
# if t>10:
#     print(f"{t} is gretter then 10")
#     if t>20:
#         print("also above 20")
#     else:
#         print("but not above 20")

'''And'''
# a=34
# b=45
# c=54
# if(a>b)and (a<c):##both condition are true
#     print(f"{a} is gretter then {b}")
# else:
#     print(f"{a} is not gretter then {b} and {c}")

'''Or'''
# a=34
# b=45
# c=54
# if(a>b)or (a<c):#at least one condition is true
#     print(f"{a} is gretter then {b}")
# else:
#     print(f"{a} is not gretter then {b} and {c}")

'''Not'''
# a=23
# b=43
# if not a>b:
#     print(" a is not greater then b")

'''Short hand if....else'''
# a=4
# b=33
# print("A") if a>b else print("B")

r=33
t=44
f=22
print("R") if (r>t)and (r>f) else print("T") if (t>r)and (t>f) else print("F")


'''Pass Statement'''
a=33
b=3
if a<b:
    pass