#to print sum of three numbers but if they are equal, print three times the sum
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if(a==b==c):
    sum=3*(a+b+c)
else:
    sum=a+b+c
print(f"The sum is {sum}")