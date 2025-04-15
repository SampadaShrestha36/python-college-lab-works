# Write a Python program to append text to a file and display the text. 

f = open("poem.txt","a")    
f.write("\nBy Emily Dickinson")
f.close()

f = open("poem.txt","r")
print(f.read())