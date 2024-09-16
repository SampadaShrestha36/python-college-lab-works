# Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 15 (both included). 
l=[x**2 for x in range(1,16)]
print("The list of first 5 elements is",l[:5])
print("The list of last 5 elements is",l[-5:])
