#WAP to enter a number from user and print factorial of it
n=int(input("Enter a number"))
i=1
f=1
while i<=n:
    f=f*i
    i+=1
print("The factorial is", f)