#to copy the contents of one file to another
f=open("t.txt")
str=""
for i in f.read():
    str+=i
fh=open("text.txt","w")
fh.write(str)
fh.close()
