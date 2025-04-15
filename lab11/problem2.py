# Write a Python program to read first n lines of a file.

n=int(input("Enter the number of lines"))
f = open("poem.txt","r")
for i in range(n):
    print(f.readline())

