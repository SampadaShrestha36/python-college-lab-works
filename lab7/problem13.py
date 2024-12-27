# Write a Python function that checks whether a passed string is a palindrome or not.
def func(s):
    if s[::-1]==s:
        print("It is pallindrome")
    else:
        print("It is not pallindrome")
s=input("Enter a string")
func(s)