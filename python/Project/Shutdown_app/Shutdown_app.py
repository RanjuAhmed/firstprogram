""" Final Code"""
from tkinter import * #tkinter মুলত GUI এর কাজ করে
import os #operating থেকে সরাসরি কাজ করে
def Restart():#restart button এর জন্য ফাংশন তৈরি করা হয়েছে
    os.system("shutdown /r /t 1") 

def Restart_time():#restart time button এর জন্য ফাংশন তৈরি করা হয়েছে
    os.system("shutdown /r /t 20")
    
def log_out():#Log out button এর জন্য ফাংশন তৈরি করা হয়েছে
    os.system("shutdown -1")
def shutdown():#Shutdown button এর জন্য ফাংশন তৈরি করা হয়েছে
    os.system("shutdown /s /r 1")
    
st=Tk() #GUI এর মূল root window তৈরি করে।
st.title("Shutdown App") #উইন্ডোর শিরোনাম সেট করে।
st.geometry("500x500") #উইন্ডোর আকার নির্ধারণ করে।
st.config(bg="green")#বেকগ্রান্ড কালার দেয়

r_button=Button(st,text="Restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=Restart)# বাটন তৈরি করার জন্য। text restart font size 30 and type time new roman cursor plus type and last of all function call from command
r_button.place(x=150,y=60,height=50,width=200)# place এর জন্য x অক্ষে 150 y অক্ষে 60 height =50, width=200
r_button=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart_time)
r_button.place(x=150,y=170,height=50,width=200)#x অক্ষে 150 y অক্ষে 170 height =50, width=200
r_button=Button(st,text="Log Out",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=log_out)
r_button.place(x=150,y=280,height=50,width=200)#x অক্ষে 150 y অক্ষে 280 height =50, width=200
r_button=Button(st,text="Shutdown",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus",command=shutdown)
r_button.place(x=150,y=390,height=50,width=200)#x অক্ষে 150 y অক্ষে 390 height =50, width=200


st.mainloop()#উইন্ডোকে চালু রাখে যতক্ষণ না আমরা সেটা বন্ধ করি।

"""Practice Code"""

from tkinter import *
import os

def Restart():
    os.system("shutdown /r /t 1")
def Restart_time():
    os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
    
sr=Tk()
sr.title("Shutdown App")
sr.geometry("500x500")
sr.config(bg="red")

l_button=Button(sr,text="Restart",font=("Time New Roman",30,"bold"),cursor="plus",relief=RAISED,command=Restart)
l_button.place(x=150,y=50,height=60,width=200)
l_button=Button(sr,text="Restart Time",font=("Time New Roman",20,"bold"),cursor="plus",relief=RAISED,command=Restart_time)
l_button.place(x=150,y=160,height=60,width=200)
l_button=Button(sr,text="Log Out",font=("Time New Roman",30,"bold"),cursor="plus",relief=RAISED,command=log_out)
l_button.place(x=150,y=270,height=60,width=200)
l_button=Button(sr,text="Shutdown",font=("Time New Roman",30,"bold"),cursor="plus",relief=RAISED,command=shutdown)
l_button.place(x=150,y=380,height=60,width=200)


sr.mainloop()
