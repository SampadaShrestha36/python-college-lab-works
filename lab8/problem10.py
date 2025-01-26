# Write a Python function that takes a sentence as a parameter and print the words in ascending order.
def func(s):
    l=s.split()
    l.sort()
    for i in l:
        print(i,end=" ")
s=input("enter a sentence")
func(s)