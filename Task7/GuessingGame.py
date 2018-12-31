#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 22:53:11 2018

@author: vivek
"""
import random
numbers = []
num = input("Enter the number in integer form")
if  num.isdigit()==1:
 for i in range(10):
    numbers.append(random.randint(1, 101))
    if int(num) == numbers[i]:
        print("You Guessed right you won")
        break
    else:
        print("Try again")
        break
else:
    print("You did not enter a number kindly enter a num(int)")
