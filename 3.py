f=open("text.txt","r")
n=int(input("ENter no of lines u want to read from last"))
count=0
for line in f:
    print(f.readlines()[-n:])
