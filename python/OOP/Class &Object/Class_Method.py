class ranju:
    collage="city University"
    def show(self):
        print(f"The name is {self.name} and company is {self.collage}")
    @classmethod #claa method class variable ke change korte pare
    def changeCollage(sr,New_collage):
        sr.collage=New_collage
    
r=ranju()
r.name="Ranju"
r.show()
r.changeCollage("Bangla")
r.show()
