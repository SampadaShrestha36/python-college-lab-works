# Write a Python program to remove newline characters from a file.

f = open("poem2.txt","r+")
a=f.read()
f.seek(0)
f.write(a.replace("\n"," "))
f.seek(0)
print(f.read())