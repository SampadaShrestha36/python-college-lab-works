# Write a Python program to remove duplicates from a list.  
l=[1,1,1,2,3,4,4]
n=[]
for i in l:
    if i not in n:
        n.append(i)
l=n.copy()
print(l)