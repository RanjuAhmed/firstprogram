"""Generator একবারে সব value return না করে, একটার পর একটা value produce করে। """
def ranju():
    for i in range(5):
        yield i

gen=ranju()
print(next(gen))#0
print(next(gen))#1
print(next(gen))#2

    