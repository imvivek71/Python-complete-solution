#elements search in a string using loop & if else

str = input("Enter any strng")
z = input("Enter the char to be searched")
counts = 0
if len(z)==1:
    if len(z) > 0:
        count = 0
        for i in range(len(str)):
            if z == str[i]:
                print("The element is available in index {} the string".format(i))
                counts=counts+1
            else:
                count = count + 1
        if (count >= 1&counts==0):
            print("The element is not available in the string")
    else:
        print("You did not enter anything")
else:
    print("Enter only single element")
