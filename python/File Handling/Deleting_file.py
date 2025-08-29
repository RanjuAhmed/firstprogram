
with open ("Ex.txt","w") as f:
    print(f.write("I am ranju"))

import os
if os.path.exists("Ex1.txt"):
    os.remove("Ex.txt")
else:
    print("The file does not exist")
