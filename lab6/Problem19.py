#Write a Python program to drop empty items from a given dictionary. 
d= {'c1': 'Red', 'c2': 'Green', 'c3': None} 
l=[]
for i in d:
    if d[i]==None:
        l.append(i)
for i in l:
    d.pop(i)
print(d)