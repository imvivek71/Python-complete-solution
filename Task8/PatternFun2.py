"""""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

x = input("Enter a odd number of row  greater than or equal to 3")
if x.isdigit()==1:
    x = int(x)
    if x % 2 != 0 and x >= 3:
        for i in range(x + 1):
            if i < int(x / 2) + 1:
                for j in range(i):
                    print("*", end="")

            else:
                for z in range(int(x + 1) - i):
                    print("*", end="")
            print("\n")
    else:
        print("Incorrect input, kindly enter a odd number of row  greater than or equal to 3 ")
else:
    print("Incorrect format")
