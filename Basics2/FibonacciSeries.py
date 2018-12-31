#Fibonacci series where the it starts for F1 = 0 & F2 = 1
"""
Created on Fri Dec 21 16:00:32 2018

@author: vivek
"""
num = input("Enter the number, till that index  we will print Fibonacci Series ")
if num.isdigit()==1:
    f=0
    s=1
    fib = 0
    print(f,end=' ')
    print(s,end=' ')
    for i in range (int(num)-2):
        fib = f+s
        print(fib,end=' ')
        f=s
        s=fib
else:
    print("Kindly enter an integer number")
