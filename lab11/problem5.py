# Write a Python program to read a file line by line and store it into a list.

f = open("poem.txt","r")
l=[]
for i in f.readlines():
    l.append(i)
print(l)

