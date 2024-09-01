#WAP to entera number from the user and print sum of its individual digits
n=int(input("enter a number"))
r=0
while n>0:
    a=n%10
    r=r+a
    n=n//10
print("the sum is",r)