# Write a Python program to access a function inside a function.
def func1():
    def func2():
        return "hello"
    return func2()
a=func1()
print(a)