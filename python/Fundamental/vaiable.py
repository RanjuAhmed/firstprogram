# a=45
# A="ranju"
# # print(a)
# print(A) #A will not override a
'''Many value and multiple variable'''
# x,y,z="ranju","raju","mokles"#many value to multiple variable 
# print(x)
# print(y)
# print(z)
'''One value and multiple variable'''
# x=y=z="ranju"# one value to multiple variable 
# print(x)
# print(y)
# print(z)
'''Unpack a collection'''
# fruit=["apple","banana","cherry"]#Unpack a collection
# x,y,z=fruit
# print(x)
# print(y)
# print(z)
'''Output variable '''
# O="ranju"
# print(O)#output variable 

# fruit=["apple","banana","cherry"]#concatation variable
# x,y,z=fruit
# print(x + y + z)

'''Global Variable'''
x = "awesome"#this is global varibale that can use inside of a function and outside

def myfunc():
  print("Python is " + x)

myfunc() 

# x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x) 

