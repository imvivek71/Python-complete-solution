# Python Program to Find Factors of Number
def factorNum(num):
    for i in range(1,int(num/2+1)):
        if num%i ==0:
            print(i,end=",")
    print(num)
num = int(input("Enter the number to get the factors"))
factorNum(num);
