#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:39:22 2018

@author: vivek
"""
string = input("Enter your  first Name")
if string.isalpha()==1:
     x = string[0].upper()
     str = string.replace(string[0],"",1)
     second = input("Enter your second name")
     if second.isalpha()==1:
         y = second[0].upper()
         secondst = second.replace(second[0],"",1)
         last = input("Enter the last name")
         if last.isalpha()==1:
             z = last[0].upper()
             lastst=last.replace(last[0],"",1)
             print(x+str+" "+y+secondst+" "+z+lastst+ " you are welcome in  Binplus")
         else:
             print("Format of the name is not correct kindly enter alphabetical value without any space")
     else:
         print("Format of the name is not correct kindly enter alphabetical value without any space")
else:
    print("Format of the name is not correct kindly enter alphabetical value without any space")
