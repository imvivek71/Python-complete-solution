# continue Break & Else
"""
Created on Wed Dec 19 12:29:59 2018

@author: vivek
"""
look_list = ["Beautiful","Charm","cool","young","loveable"]
for quality in look_list: 
    if quality =='cool':
        continue
    print(quality, end='\t')
    
print('\n'"output when using break")
for quality in look_list: 
    if quality=='cool':
        break
    print(quality)  
xyz = ''    
for quality in look_list: 
    if quality=='Charm':
        xyz = quality
        break
else:
    print("Nothing")
if xyz== 'Charm':  
    print("You got")
