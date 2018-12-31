# even or odd checking
"""
Created on Thu Dec 20 11:08:34 2018

@author: vivek
"""
num = input("Enter the number to  be checked")
if num.isdigit()==1:
    print ("Yo heve entered a right no")
    numm =int(num)
    if numm%2==0:
        print("The number is even")
    else:
        print('The number is odd')
else:
    print("kindly check the input & enter only an int it should not contain space/alphabets/special characters")
        
