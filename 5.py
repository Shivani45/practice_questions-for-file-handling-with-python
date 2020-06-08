f=open("text.txt")
counts={}
for lines in f:
    x=lines.split()
    for word in x:
        counts[word]=counts.get(word,0)+1
print(counts)
