"""""
*
**
***
****
*****
"""
x = input("Enter the number of required row")
if x.isdigit()==1:
    x = int(x)
    for i in range(x+1):
        for j in range(0, i):
            print("*", end=" ")
        print('\n')
