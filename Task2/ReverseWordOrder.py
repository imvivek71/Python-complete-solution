#Reverse word order
"""
Created on Sat Dec 22 14:14:28 2018

@author: vivek
"""
x = input("Enter any string of words seperated by space")
list = x.split()
print(sorted(list,reverse=True))
