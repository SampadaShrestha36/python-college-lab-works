# Write a Python function to calculate the factorial of a number (a non-negative integer) with and without using recursion. The function accepts the number as an argument.  
# using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
print(fact(n))
# without using recursion
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(factorial(n)) 