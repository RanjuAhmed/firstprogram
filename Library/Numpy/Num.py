import numpy as np
"""First Program create a array"""
# arr=np.array([[3,6],[37,7]])
# print(arr)
"""Array Properties"""
# print(arr.dtype)
# print(arr.shape)
# print(arr[0:4])
# print(arr.ndim)
# print(arr.flatten())
# print(arr.T)
"""Array Creation"""
# a=np.zeros((3,3))
# print(a)
# a=np.ones((3,3))
# print(a)
# a=np.eye((3))
# print(a)
# a=np.arange(3,10,2)
# print(a)
# a=np.linspace(3,10,5)
# print(a)
"""Indexing and Slicing"""
# a=np.array([[3,5],[3,6],[3,6]])
# print(a)
# print(a[1,1])
# # print(a([1:1])==5)
"""Mathematical & statistics Function"""
a = np.array([1, 2, 3, 4])
# b=np.array([4,5,6])
# print(a+b)
# print(a*b)
# print(a**3)
# # print(a+10)
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.min(a))
# print(np.std(a))
# print(np.sqrt(a))

"""Concatation and Spliting"""
# a=np.array([1,2,3,4])
# b=np.array([1,7,3,8])
# print(np.concatenate((a,b),axis=0))
# print(np.vstack(a))
# print(np.hstack(a))
# print(np.split(a,2,axis=0))

"""Boolean Indexing and filtering"""
# a=np.array([2,4,5,3,5,6])
# print(a[a<5])
# print(np.where(a%2==0,"Even","Odd"))

"""Linear Algebra"""
a = np.array([[3, 5, 4], [6, 7, 3], [3, 5, 6]])
print(np.dot(a, a))
print(np.linalg.eigvals(a))
print(np.linalg.eig(a))
