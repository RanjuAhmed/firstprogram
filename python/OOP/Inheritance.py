class parent:##parent class
    def __init__(self,name):
        self.Name=name
    def showinfo(self):
        print("Father Name is",self.Name)

class Ranju(parent):#child class
    print("My name is Ranju")
        

r=Ranju("Amjad")
r.showinfo()
