class a:
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(f"my name is {self.name}")
class b:
    def __init__(self,id):
        self.id=id
    def sow1(self):
        print(f"{self.id}")
class c(b,a):#Multiple inheritance 
    def __init__(self, id,name,Dept):
        self.id=id
        self.dept=Dept
        self.name=name


r=c(34,"ranju","CSE")
print(r.id)
print(r.name)
r.show1()

