#finding the last character of a lines that startswith "my name"
f=open("s.txt","r")
c=""
for i in f:
    if i.startswith("my name"):
        l=i.split()
        c+=l[len(l)-1]
print(c)
        
