#List Overlap
"""
Created on Thu Dec 20 17:19:53 2018

@author: vivek
"""
stringf = input("Enter the elements seperated by space")
strings = input("Enter the elements for list seperated by space ")
teststrf = stringf.replace(" ","")
teststrs = strings.replace(" ","")
#if (teststrf.isdigit()==1 & teststrs.isdigit()==1):
listf = stringf.split()
lists= strings.split()
lenf = len(listf)
lens = len(lists)
def Intersection(listf,lists):
    return  set(listf).intersection(lists)
print (Intersection(listf,lists))    
#else:
#    print("Only integers seperated by space is accepted kindly check again")

