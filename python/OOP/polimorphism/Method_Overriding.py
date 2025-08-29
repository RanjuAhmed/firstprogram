"""Method Overriding"""
# class shape:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def area(self):
#         return self.x*self.y

# class Circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#         super().__init__(radius,radius) 
#     def area(self):
#         return 3.1416*super().area()

# C=Circle(5)
# print(C.area())

"""Method Overriding"""
class shape:
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def show(self):
        print("Hello everyone")
    
class Circle(shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def show(self):
        print(self.x*self.y)
        print(3.342*self.radius**2)  

C=Circle(3,4,5)
C.show()
