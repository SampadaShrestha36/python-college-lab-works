#Write a Python Program to get the largest and smallest number in a list without using built in functions. 
l=[10,20,40,12,234,534,23,1]
largest=l[0]
smallest=l[0]
for i in l:
    if largest<i:
        largest=i
    if smallest>i:
        smallest=i
print(f"largest={largest} and smallest={smallest}")