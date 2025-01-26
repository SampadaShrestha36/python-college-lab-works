# Write a Python function that takes a sentence, and return a sentence with the words reversed. 
def func(s):
    l=s.split()
    
    for i in l[::-1]:
        print(i,end=" ")
s=input("enter a sentence")
func(s)