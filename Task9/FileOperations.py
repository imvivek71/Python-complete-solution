# Perform file operations(Read, write,open,close)
f = open("/home/vivek/Downloads/readme.txt")      # read
print(f)
f = open("/home/vivek/PycharmProjects/BinplusTasks/Task9/SizeResolutionImage.py",'w')  # write in text mode
print(f)
f = open("/home/vivek/PycharmProjects/BinplusTasks/Task9/SizeResolutionImage.py",'r+b') # read and write in binary mode
print(f)
f.close()
