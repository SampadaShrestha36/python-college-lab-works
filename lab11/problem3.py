# Write a Python program to count the number of lines in a text file which starts with an alphabet “T”. 

f = open("poem.txt","r")
count = 0
for line in f.readlines():
    if line.startswith("T"):
        count += 1
print(count)