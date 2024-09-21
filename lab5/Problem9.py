#Write a Python program to convert a given tuple of positive integers into an integer.
t1=(1, 2, 3) 
print("Original tuple: ")
print(t1)
print("Convert the said tuple of positive integers into an integer: ")
s=""
for i in t1:
    s=s+str(i)
print(int(s))
t2=(10, 20, 40, 5, 70) 
print("Original tuple: ")
print(t2)
print("Convert the said tuple of positive integers into an integer: ")
a=""
for i in t2:
    a=a+str(i)
print(int(a))