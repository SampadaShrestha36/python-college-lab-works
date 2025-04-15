# Write a Python program to read a file line by line store it into a variable.

f = open("poem.txt","r")
a=""
n=f.readlines()
for line in n:
    a=a+line
print(a)