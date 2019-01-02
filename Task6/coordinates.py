#Checking the co-ordinates of given x,y values.
x = float(input("Enter x axis value"))
y = float(input("Enter y axis value"))
if x>0:
    str1 = "positive"
else:
    str1 = "Negative"
if y>0:
    str2 = "postive"
else:
    str2 = "negative"
if x ==0 and y==0:
    print("its on origin")
else:
    if (x != 0 and y != 0):
        if ((x > 0) and (y > 0)):
            print("It is in 1st coordinate")
        elif (x < 0 and (y > 0)):
            print("It is in 2nd coordinate")
        elif (x < 0 and y < 0):
            print("It is in 3rd coordinate")
        else:
            print("It is in 4th coordinate")
    else:
        if (x == 0):
            print("its on {} y aixs".format(str2))
        if (y == 0):
            print("its on {} x aixs".format(str1))
