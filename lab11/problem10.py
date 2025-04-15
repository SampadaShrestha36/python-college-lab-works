# Write a Python program to write a list to a file.

f = open("otes.txt","w")
l=['Hi',1,5]
for i in l:
    f.write(str(i))
f.close()
f=open("otes.txt","r")
print(f.read())