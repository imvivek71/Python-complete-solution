num = input("Enter the number in integer format")
if num.isdigit() == 1:
    x = len(num)
    sum = 0
    for i in range(0, x):
        y = int(num[i])
        sum = y**x + sum
    if sum==int(num):
        print("The number is an Armstrong number ")
    else:
        print("The number is not an Armstrong number ")
else:
    print("Kindly enter the number in integer format")
