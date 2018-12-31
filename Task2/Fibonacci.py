#Fibonacci series where the it starts for F1 = 0 & F2 = 1
"""
Created on Fri Dec 21 16:00:32 2018

@author: vivek
"""
num = input("Enter the number for Fibonacci Series ")
if num.isdigit()==1:
    num = int(num)
    f=0
    s=1
    fib = 1
    if num==1:
        print(f,end=' ')
    elif num!=0:
        print(f,s,end=' ')
    for i in range (num-2):
        fib = f+s
        print(fib,end=' ')
        f=s
        s=fib
else:
    print("Kindly enter an integer number")
