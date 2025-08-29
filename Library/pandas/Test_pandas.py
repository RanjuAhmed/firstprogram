import pandas as pd
import numpy as np
# d = pd.Series([10, 345, 45])
# print(d)

s=pd.DataFrame(
    {'name':['Ranju','Raju','Raj'], 'ID':[33,44,33],'class':[11,12,10]
     })
# print(d)
# print(s)
# print(d.shape)
"""Upload file or create a file"""
# s.to_csv("first_Name.csv")
# s.to_csv("first_Namewithoutindex.csv",index=False)
""" Structure """
# s.to_excel("first_Name1.xlsx")
# print(s.head(2))
# print(s.tail(2))    
# print(s.shape)
# print(s.info())
# print(s.describe())
# print(s.columns)
"""File read"""
# s=pd.read_csv("first_Name.csv")
# print(s)
# s['name'][1]='ranj'
# print(s)
# s.to_csv("my_csv.csv")

""" Random"""
newd=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(newd.head())
# print("Difference")
# print(newd)
# print(newd.describe)
# print(newd.columns)
# s=newd.loc[0][0]='ranju'
# print(s)
# print(newd.index)
print(newd.T)
print(newd.sort_index(axis=0,ascending=False))




