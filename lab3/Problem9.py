# Write a Python program to create the multiplication table (from 1 to 10) of a number.
n=int(input("Input a number:"))
for i in range(1,11):
    print(f"{n}X{i}={n*i}")