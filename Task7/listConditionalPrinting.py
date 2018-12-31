#list comprehensions print till given index
"""
Created on Fri Dec 21 17:18:07 2018

@author: vivek
"""
string = input("Enter the string/array seperated by space")
num = input("Enter the index till you want to print the list")
if num.isdigit()==1:
    if len(string)>0:
        list = string.split()
        num = int(num)
        if num<=len(list):
            print("[",end='')
            for i in range(num):
                print(list[i]+",",end='')
            print("]",end='')  
        else:
            print("Kindly enter index less than or equal to list size")
    else:
        print("You entered space or nothing kindly enter again")
else:
    print("Enter integer index")
