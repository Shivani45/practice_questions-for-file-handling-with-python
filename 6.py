#to read a file line by line and store it into a list
f=open("text.txt")
l=list()
for lines in f:
    l.append(lines)
print(l)
