#augumented Assignmennt-
"""
Created on Thu Dec 20 23:39:49 2018

@author: vivek
"""
str = "1,2,3,4,5,5"
augmentedstr= ""
print(str)
for i in range(0,len(str)):
    if str[i] in '123456789':
        augmentedstr +=str[i]+"," 
print(augmentedstr.split())
#examples
x = 23
x +=1
x*=2
x/=2
greeting = "Binplus"
greeting+=" Technologies"
print(greeting)
