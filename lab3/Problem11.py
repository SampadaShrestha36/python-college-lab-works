#Write a Python program that accepts a word from the user and reverses it.
s=input("Enter a word")
for i in range(-1,-len(s)-1,-1):
    print(s[i],end="")
    
