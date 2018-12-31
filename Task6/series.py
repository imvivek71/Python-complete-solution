""""
 "With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both               included). and then the program should print the dictionary.

Suppose the following input is supplied to the program:

8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"


"""
x= input("Enter the number till that index you want to print the series greater than 0")
if x.isdigit()==1:
    x = int(x)
    if x==0:
        print("{0: 0}")
    else:
        s = {i: i * i for i in range(1, x + 1)}
        print(s)
else:
    print("Number formmat is not correct or entered num is 0")
