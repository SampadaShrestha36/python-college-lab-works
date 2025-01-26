# Write a Python program to detect the number of local variables declared in a function.
def func():
    a=1
    b=2
    c=3
    d="Hello"
print(func.__code__.co_nlocals)