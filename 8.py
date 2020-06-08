#finding largest word in a file

f=open("t.txt")
words=f.read().split()
max_len=len(max(words,key=len))
print([word for word in words if len(word)==max_len])
