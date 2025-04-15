# Write a Python program to count and display the total number of words in a file.

f = open("poem.txt","r")
print(len(f.read().split()))
