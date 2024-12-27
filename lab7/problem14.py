#  Write a Python function that takes a string as input and counts the number of uppercase and lowercase characters in the string.  
def func(s):
    a=0
    b=0
    for i in s:
        if i==i.upper():
            a=a+1
        elif i==i.lower():
            b=b+1
    print(f"Uppercase={a} and lowercase={b}")
s=input("enter a string")
func(s)