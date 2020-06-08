#to read a random line from a file
import random
f=open("text.txt")
print(random.choice(f.read().splitlines()))

