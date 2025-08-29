'''Public Variable'''
# class emply:
#     def __init__(self):
#         self.Name="Ranju"#public variable that access from outside

# a=emply()
# print(a.Name)

'''Private'''
# class emply:
#     def __init__(self):
#         self.__Name="Ranju"#private variable that cannot access from outside

# a=emply()
# # print(a.__Name)
# #কিন্তু প্রাইভেট ভেরিয়েবল কেও এক্সক্সে করা যায়
# print(a._emply__Name)#একে নেম মাইনিং বলে
# print(a.__dir__())

'''Protected Method'''
class emply:
    def __init__(self):
        self._Name="Ranju"#protected  variable that access from outside

a=emply()
print(a._Name)#access to function
