#to combine each line from first file with corresponding line in second line
f=open("t.txt")
fh=open("text.txt")
for line1,line2 in zip(f,fh):
    print(line1+line2)
