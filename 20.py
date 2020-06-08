#create a list and insert the distinct words of a file in it and display it in sorted order

f=open("s.txt","r")

lst = list()
for line in f:
    x=line.split()
    for wrd in x:
        if wrd not in lst:
            lst.append(wrd)

s=sorted(lst)
print(s)

