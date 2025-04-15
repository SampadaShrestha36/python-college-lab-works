# Write a Python program to read a random line from a file. 

f = open("poem.txt","r")
n=int(input("Enter the line number"))
print(f.readlines()[n-1])