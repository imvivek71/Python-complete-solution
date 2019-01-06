#Write a Python program to reverse the order of the items in the array
#Write a Python program to get the length in bytes of one array item in the internal representation
a = [str(x) for x in input("Enter the elements seperated by space").split()]
a.reverse()
print(a)
print(len(a))
