# x=lambda a,b:a*b#lambda argument: expression
# print(x(3,4))

def my_f(n):# function inside another function
    return lambda x:x*n
m=my_f(3)
print(m(4))
