""""
Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""
numbers = []
count=0
num = [x for x in input("Enter the binary numbers separated by comma").split(',')]
for i in range (len(num)):
    if num[i] == int:
        print("Not Binary Number")
        count = 1
        break
if count==0:
    for p in num:
        x = int(p, 2)
        if x % 5 == 0:
            numbers.append(p)
    print("Here is the list of divisible by 5")
    print(','.join(numbers))
