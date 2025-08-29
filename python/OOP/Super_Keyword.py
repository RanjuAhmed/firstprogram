"""Super Keyword"""
# class parent:
#     def parent_mehtod(self):
#         print("This is the parent method")
    
# class child(parent):
#     def parent_meh(self):
#         print("Hello everyone")
#         super().parent_mehtod()
#     def child_method(self):
#         print("Child class")
#         super().parent_mehtod()# super allowys parent class ke access kore 

# r=child()
# r.parent_mehtod()#print parent method
# r.parent_meh()#print parent class method and prent_mah method
# r.child_method() #print child class mehtod and parent class method

class parent:
    def __init__(self,name,id):
        self.Name=name
        self.id=id
    def show1(self):
        print("Hello everyone")
    
class child(parent):
    def __init__(self,course, name, id):
        super().__init__(name, id)
        self.Course=course
    def child_method(self):
        print(f"My name is {self.Name} id is{self.id} and may course is {self.Course}")

C=child("ICT","Ranju",3343)
C.show1() #print show method        
print(C.Course)# print course name
print(C.id)# print id
print(C.Name)# print Name
print(C.child_method())#print child method 
        