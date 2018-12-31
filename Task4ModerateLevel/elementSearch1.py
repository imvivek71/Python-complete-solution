#element search by using if else only
string = input("enter a string")
i = input("Enter the element to be checked")
if len(i)==1:
    if len(i) > 0:
        if i in string:
            print("The element is available in the string")
        else:
            print("The element is not available in the string")
    else:
        print("Kindly check you did not enter anything")
else:
    print("Enter only a single element")
