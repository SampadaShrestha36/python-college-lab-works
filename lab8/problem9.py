# Write a Python program to find the power of a number using recursion function. 
def func(n,p):
    if p==1:
        return n
    else:
        return n*func(n,p-1)
print(func(5,2))
print(func(2,3))