#Triangle & rectangle print
"""
Created on Wed Dec 19 17:01:21 2018

@author: vivek
"""
#for square shape
s=input("Enter thr size/length of square")
if s.isdigit()==1:
    s =int(s)
    print("Following is the square shape")
    for num in range(s):
        for i in range(s):
            print("* ",end='')
        print("\n")
else:
        print("Run again and enter the inputs in number integer")
#for rectangle shape
r=input("Enter thr height of rectangle")
if r.isdigit()==1:
    r = int(r)
    print("Following is the rectangle shape")
    for num in range(r):
         for i in range(r+1):
              print("* ",end='')
         print("\n")
else:
    print("Run again and enter the desired area in number integer")
#for triangle printing
h=input("Enter thr height of triangle")
if h.isdigit()==1:
    h = int(h)
    print("Following is the pattern of the triangle")
    for num in range(h+1):
        for i in range(num):
            print("* ",end='')
        print("\n")
