# Write a Python program to insert a given string at the beginning of all items in a list.
l=[1,2,3,4]
s=input("enter a string")
for i in range(len(l)):
    l[i]=s+str(l[i])
print(l)