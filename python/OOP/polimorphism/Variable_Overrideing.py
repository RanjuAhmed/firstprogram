class ranju:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return(f"{self.i}i + {self.j}j + {self.k}k")
    def __add__(self,x):
        return ranju (self.i+x.i,+self.j+x.j, self.k+x.k) #ranju variable ovarriding       

r=ranju(3,4,7)
print(r)
print(r.__str__())
s=ranju(4,7,9)
print(s)
v=r+s
print(v)