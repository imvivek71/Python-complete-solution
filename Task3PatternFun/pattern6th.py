""""
  
    *

   ***

  *****

 *******

*********
"""
x =int(input("Enter the number"))
for i in range(x+1):
    for sp in range(x-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print("\n")
