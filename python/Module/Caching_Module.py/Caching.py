"""Caching Function or Functools method এই মেথড এর কাজ হইল একবার প্রোগ্রাম রান করার পর ওই ডাটা সেইভ করে রাখে পরে যখন আবার ফাংশন কল করা হয় তখন সরাসরি store করা ডাটা প্রিন্ট করে যেমন এই প্রোগ্রাম এ টাইম স্লেপ ২ মিনিট দেওয়া হয়েছে একবার প্রিন্ট করতে ২ মিনিট টাইম নিবে বাট যদি একবার রান হয় তাহলে ২য় বার আর টাইম নিবে না সরাসরি কেশ থেকে ডাটা দিবে"""
from functools import lru_cache 
import time

@lru_cache(maxsize=None)
def F(n):
    time.sleep(2)
    return n*2

print(F(5))# ২ সেকেন্ড টাইম নিবে
print("Hello world")
print(F(5))# তারাতারি আউটপুট দিবে কারন জমা করা আছে 
print("Ranju")
print(F(10))#২ সেকেন্ড টাইম নিবে
print("Rabin")
print(F(15))#২ সেকেন্ড টাইম নিবে
print("Raju")
