#Write a Python program to create a dictionary from a string. 
s="engineerings"
d={}
for i in s:
    a=s.count(i)
    d[i]=a
print(d)