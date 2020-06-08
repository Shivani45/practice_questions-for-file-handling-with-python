#to find the frequency of words in a text file using dict and printing the word having largest frequency

f=open("t.txt","r")
counts=dict()
for line in f:
    x=line.split()
    for word in x:
        counts[word]=counts.get(word,0)+1
print(counts)
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigcount,bigword)
