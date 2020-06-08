#taking text file as a input and counting number of words in file(some words can be separated by a comma)

f=input()
file=open(f)
d=file.read()
d.replace(","," ")
print(len(d.split()))
