class a:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def show(self):
        print(self.name,self.species)
class b(a):
    def __init__(self, name,bread ):
        a.__init__(self,name, species="dog")
        self.bread=bread
    def show_d(self):
        a.show(self)
        print(self.bread)
class c(b): #Multilevel inheritance 
    def __init__(self, name,color):
        b.__init__(self,name,bread="Golden")
        self.color=color
    
    def show1(self):
        b.show_d(self)
        print(self.color)

r=c("Animal","red")
# r.show_d()
r.show1()