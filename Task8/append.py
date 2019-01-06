# Write a Python program to append a new item to the end of the array
X =[str(x) for x in input("enter the  array elements separated by space").split()]
Y =[str(y) for y in input("enter the  array elements separated by space").split()]
X.extend(Y)
#X.append(Y)
print(X)
