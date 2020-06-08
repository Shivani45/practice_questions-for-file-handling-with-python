f=open("text.txt","r")
n=int(input("Enter the lines u want to read"))
for i in range(n):
    s=f.readline()
    print(s,end="")
