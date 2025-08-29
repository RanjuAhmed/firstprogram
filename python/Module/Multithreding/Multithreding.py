""" Threading মুলত এক সাথে অনেক গুলো ফাংশনের কাজ একসাথে চলে যেমন নিচের যে প্রোগাম টা আছে সেটাই দেখলেই বুজা যায়। টাইম লস হইনা।  """
import threading
import time 

def ranju():
    for i in range (1,5):
        print(i)
        time.sleep(2)
def raju():
    for c in "ABCD":
        print(c)
        time.sleep(1)


t1=threading.Thread(target=ranju)#থ্রেড তৈরী করে এটি ranju ফাংশন এর জন্য কাজ করবে।
t2=threading.Thread(target=raju)
#থ্রেড তৈরী করে এটি raju ফাংশন এর জন্য কাজ করবে।
t1.start()#কাজ শুরু করবে ranju এর জন্য
t2.start()#কাজ শুরু করবে rju এর জন্য
t1.join()#কাজ শেষ করবে ranju এর জন্য
t2.join()#কাজ শেষ করবে ranju এর জন্য
print("Done the work")