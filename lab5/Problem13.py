# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value. 
s=[1,2,3,4,5,6,7,8,9,10]
a=set()
n=int(input("enter the sum number"))
for i in s:
    for j in s:
        if i!=j and i+j==n:
            b=(i,j)
            if (j,i) not in a:
                a.add(b)
print(a)