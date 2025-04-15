# Write a Python program to extract characters from various text files and puts them into a list.

f = open("poem2.txt","r")
a=f.read()
l=[]
for i in a:
    l.append(i)
f.close()
f=open("poem.txt","r")
b=f.read()  
for i in b:
    l.append(i)
print(l)