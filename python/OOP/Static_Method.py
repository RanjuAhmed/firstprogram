class ranju:
    def __init__(self,n):
        self.num=n
    def show(self,num2):
        return self.num+num2
    @staticmethod #static method use করলে সেলফ নেওয়া লাগে না শুধু ক্লাস নাম দিয়ে ওবজেক্ট ক্রিয়েট করে মেথড কল করলেই আউটপুট দেখায়।
    def add(a,b):
        return a+b

r=ranju(4)
print(r.num)
print(r.show(5))
print(r.add(34,34))
