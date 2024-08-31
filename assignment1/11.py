#WAP to enter a limit from user and print fibonacii series 
#0 1 1 2 3 5 8 13
n=int(input("enter the limit"))
a,b=0,1
i=1
print(a,b,end=" ")
while i<=n-2:
    c=a+b
    a,b=b,c
    print(c,end=" ")
    i+=1