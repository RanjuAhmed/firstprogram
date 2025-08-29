# f=open("Exercise.txt","x")#create a file
# f=open("Exercise.txt","rt")
# print(f.read())
# f.close()

# '''With'''
# with open("Exercise.txt","r")as f:#read mode
#     print(f.read())

# with open("Exercise.txt","r")as f:
#     print(f.readline())

# with open("Exercise.txt","r")as f:
#     print(f.readlines(3))

with open("Exercise.txt","w")as f: #write mode
    print(f.write("hi sakib"))
with open("Exercise.txt","a")as f:#append mode
    print(f.write("a am"))
