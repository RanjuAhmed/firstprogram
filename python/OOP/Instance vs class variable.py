class ranju:
    collage_Name="City University" #class variable
    def __init__(self,name):
        self.name=name 
        self.raise_amount=45.35 #istant variable
    def show(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amount} and collage name is {self.collage_Name}")

a=ranju("Ranju")
a.collage_Name="Bangla"# এইটা শুধু a এর জন্য change করা হয়েছে রহান এর জন্য হবে না।
a.raise_amount=34#install variable সব সময় change করা যায়। same class variable এর মতো। 
a.show()
b=ranju("Rohan")
b.show()