#to remove newline character from a file
f=open("text.txt")
x=f.read().rstrip()
print(x.split())
