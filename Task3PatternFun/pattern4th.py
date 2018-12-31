"""""
   1

  232

 34543

4567654
"""
m=1
x=4
for i in range(x+1):
    k = i
    for sp in range(x-i):
        print(" ",end="")
    for j in range(i):
        print(k,end="")
        k+=1
        m=m+1
        l=k-2
    for z in range(m-1):
        if(l>=i):
            print(l,end="")
            l=l-1
    print("\n")
