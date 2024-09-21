#Write a Python program to convert a given string list to a tuple. 
s=input("enter a string")
print(type(s))
t=()
for i in s:
    t=t+(i,)
print(t)
print(type(t))