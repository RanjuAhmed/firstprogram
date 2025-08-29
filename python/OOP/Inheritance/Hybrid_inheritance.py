"""Hybrid And Hierarchical Inheritance"""
class a:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class b(a):
    def __init__(self, name,id):
        a.__init__(self,name)
        self.id=id
    def show1(self):
        a.show(self)
        print(self.id)
    
class d:
    def __init__(self,dept):
        self.dept=dept
    def show2(self):
        print(self.dept)
class c(d,b): 
    def __init__(self, name,id,dept,course):
        d.__init__(self,dept)
        b.__init__(self,name,id)
        self.course=course
    def show3(self):
        b.show1(self)
        d.show2(self)
        print(self.course)

r=c("Ranju",35,"CSE","ICT")
# print(r.name)
# print(r.id)
# print(r.dept)
# print(r.course)
# print(r.show())
# print(r.show1())
# print(r.show2())
print(r.show3())
