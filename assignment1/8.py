#WAP to enter a number fromthe user and check if it is pallindrome or not
n=int(input("enter a number"))
b=n
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
if b==r:
    print("It is pallindrome")
else:
    print("It is not pallindrome")