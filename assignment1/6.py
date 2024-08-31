#WAP to enter a number from user and print reverse of it
n=int(input("enter a number"))
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
print("the reverse is",r)