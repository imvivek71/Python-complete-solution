# Python Basics factorial program
x = int(input("Enter the no."))
fact = 1
if x>1:
    print("You are eligible to print reverse of it")
else:
    x= int(input("Enter the number again"))
for i in range (1,x):
    fact = fact*i
fact = (fact)
print("The factorial of the given is number is {}".format (str(fact)))
