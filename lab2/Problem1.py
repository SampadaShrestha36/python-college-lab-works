#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
n=int(input("enter a number"))
if n<17:
    print("The difference is", (17-n))
else:
    print(-1*(17-n))