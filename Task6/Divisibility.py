####" Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
##The numbers obtained should be printed in a comma-separated sequence on a single line."
x = input("Enter the starting range")
y = input("Enter the end range ")
if x.isdigit()==1 and y.isdigit()==1:
    x = int(x)
    y = int(y)
    for i in range(x, y):
        if (i % 7 == 0 and i % 5 != 0):
            print(i, end=" ")
else:
    print("Kindly enter the ranges in right fromat")
