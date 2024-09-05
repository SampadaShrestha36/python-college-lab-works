#Write a Python program that accepts a string and calculates the number of digits and letters.
s=input("Enter a string")
a,b=0,0
for i in s:
    if i.isdigit()==True:
        a+=1
    elif i.isalpha()==True:
        b+=1
    else:
        pass
print("Letters",b)
print("Digits",a)