#Check Primality Functions.
"""
Created on Sat Dec 22 12:17:13 2018

@author: vivek
"""
def isPrime():
 z=False
 while z==False:
    n = input("Enter any integer")
    if n.isdigit()==1:
        count=0
        n = int(n)
        d = int(n/2)
        for i in range(2,d):
            if n%i==0:
                count = 1
        if (count==1 or n==1 or n==0):
            print("its not a prime number") 
        else:
            print("Prime")
    else:
         z =False
         print("Again enter the number to be checked")
isPrime();
