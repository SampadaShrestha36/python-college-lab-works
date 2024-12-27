#  Write a Python recursive function to find out factorial of any given number.
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a number"))
print(fact(n))