#Divisors of any number
"""
Created on Thu Dec 20 18:28:05 2018

@author: vivek
"""
num = input("Enter an integer number")
if num.isdigit()==1:
    div = 0
    num = int(num)
    r = int(num/2)+1
    for i in range(1,r):
        if num%i==0:
            div = i
            print(div,end=' ')
    print(num)
else:
    print("Kindly enter a valid integer")


