# Python Program to Find HCF or GCD

def computeHCF(x, y):
    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))


print("The H.C.F. of", num1, "and", num2, "is", computeHCF(num1, num2))
