#WAP to enter a number from user and print individual digits on separate lines
n=int(input("enter a number"))
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
while r>0:
    b=r%10
    r=r//10
    print(b)