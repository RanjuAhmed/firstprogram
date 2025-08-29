"""Multiprocessing মুলত কাজ করে অনেক গুলো কাজ একসাথে ডাউনলড দেওয়ার জন্য use kora hoi"""
import multiprocessing
import requests

def ranju(url,name):
    responce=requests.get(url)
    open(f"{name}.jpg","wb").write(responce.content)
    print("Downloading Finished....",name)
pros=[]
url="https://picsum.photo/2000/3000"

for i in range(3):
    r=multiprocessing.Process(target=ranju,args=[url,i])#multiprocess creation 
    r.start()#start
    pros.append(r)

for r in pros:
    r.join()#join 