# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 20 (both included).
def func():
    l=[]
    for i in range(1,21):
        l.append(i*i)
    print(l)
func()