# Check whether given letter is vowel or consonant
#t&c - it should show whether the char is num, alph or special
# for more than a letter it should notify
"""
Created on Wed Dec 19 15:42:01 2018

@author: vivek
"""
x = input("Enter any letter")
if  ((len(x)<2) & len(x)!=0):
  if((ord(x) > 64) & (ord(x) < 91)) | ((ord(x) > 96) & (ord(x) < 123)):
      if((x=='A') | (x=='E') | (x=='I') | (x=='O') | (x=='U') | (x=='a') | (x=='e') | (x=='i') | (x=='o') | (x=='u')):
        print("Vowel")
      else:
        print("consonant")
  elif((ord(x) > 47) & (ord(x) < 58)):
    print("Number")
  else:
    print("Special Character")
elif len(x)==0:
    print("Kindly enter any letter")
else:
    print("Kindly run again & enter single letter")

