#to write a list to a file
f=open("text.txt","w")
l=["Apple","oranges","mango"]
f.write(str(l))
f.close()
