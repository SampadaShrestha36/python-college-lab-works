# Write a Python a function that takes a string as argument and print the most common character in that string.
def count(s1,s):
    n=0
    for i in s:
        if s1==i:
            n=n+1
    return n
def func(s):
    n='' 
    for i in s:
        if count(i,s)>count(n,s):
            n=i
    return n
s=input("enter a string")
print("The most common string is",func(s))