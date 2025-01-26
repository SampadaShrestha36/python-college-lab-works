# Write a Python function that accepts a string and counts the number of vowel and consonant letters. 
def count(s):
    s1=['a','e','i','o','u']
    a=0
    b=0
    for i in s:
        if i in s1:
            a=a+1
        else:
            b=b+1
    return a,b
s=input("enter a string")
a,b=count(s)
print(f"number of vowels is {a} and consonants is {b}")