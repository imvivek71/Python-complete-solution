"""""
        *
        *
      * * *
      * * *
    * * * * *
"""
row = int(input("enter the number of row "))
row = int(row/2)+1
for i in range(row+1):
    for k in range(row-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print("\n")
    if i<row:
        for k in range(row - i):
            print(" ", end="")
        for j in range(2 * i - 1):
            print("*", end="")
        print("\n")
