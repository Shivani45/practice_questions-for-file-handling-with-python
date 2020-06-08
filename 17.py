#creating 26 text files A.txt,B.txt..upto Z.txt
import os

for i in range(65,91):
    os.remove(chr(i)+".txt")
    
