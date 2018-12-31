#Hashin of the file
import os
import hashlib
filename = input("filename")
if (os.path.isdir(filename))==False:
    if (os.path.exists(filename)) == True:
        hasher = hashlib.md5()
        with open(filename, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            print(hasher.hexdigest())
    else:
        print("Check right file name")
else:
    print("its a direc")
