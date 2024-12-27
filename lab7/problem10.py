# Create a function that takes a list and a number, return a list after adding the number to the list preventing it from changing the original list. 
def func(l,n):
    m=[]
    for i in l:
        m.append(i*n)
    return m
n=int(input("Enter a number"))
l=[1,2,3,4,5]
print(func(l,n))