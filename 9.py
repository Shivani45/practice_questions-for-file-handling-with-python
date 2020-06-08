#finding file size 
import os
x=os.stat("text.txt")
print(x.st_size)
