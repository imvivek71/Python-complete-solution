#list less than 10
"""
Created on Thu Dec 20 19:16:55 2018

@author: vivek
"""
str = input("Enter the numbers seperated by space")
strr= str.replace(" ","")
if strr.isdigit()==1:
    list = str.split()
    lessthan = ""
    for i in range(len(list)):
        if int(list[i])<10:
            lessthan+=list[i]+", "
    print(lessthan.split(),end=' ')
else:
    print("Kindly enter integers seperated by space")
