#Write a python program to find the sum of n natural numbers 
n=int(input("Enter a number"))
s=0
for i in range(n+1):
    s=s+i
print("The sum of thee natural numbers is",s)