# #general function
# class ranju:
#     x=1
#     b=34
#     sum=x+b 
#     print(sum)
# a=ranju()#object create

'''__init__ function ইনপুট নেওয়ার জন্য ইনিট ব্যবহার করা হয়'''
# class rangu:
#     def __init__(self, d,c):
#         self.data=d
#         self.carecter=c
#         print(f"{self.data},{self.carecter}")
# p=rangu(34,"strg")
# print(p) 

'''__self__'''
# class ranju:
#     def __init__(self,a,b,c):
#         self.num1=a
#         self.num2=b
#         self.num3=c
#     def __str__(self):
#         return f"{self.num1},{self.num1}"
# r=ranju(3,4,8)
# print(r)

'''Mehtod Create'''
# class raj:
#     def __init__(self,Name,id,collage):
#         self.name=Name
#         self.Id=id
#         self.collage=collage
    
#     def Ranju(self):
#         print("Hello my name is "+self.name)
#         print("My id id ",+self.Id)
#         print("My collage is "+self.collage)
    
# r=raj("Ranju",1048,"City University")
# r.Ranju()

'''self keyword'''
# class ranju:
#     def __init__(RM,role,rabi):#সেলফ বাদ দিয়ে আরএম দেওয়া হয়েছে 
#         RM.raki=role
#         RM.raj=rabi
#     def ran(abc):#আরএম প্রথম ইন্ডেক্স এ জন্য এবিসি দেওয়া হয়েছে যা আরএম এর কাজ করবে
#         print("Hello my name is "+abc.raj)
    
# r=ranju("raj","ranju")
# r.ran()


'''Delete object'''
# del r.raj
# r.ran()

'''Deleting Object Properties'''
# del r #Object delete
# r.ran()

"""Pass Statement"""
class ranju:
    def __init__(self):
        pass