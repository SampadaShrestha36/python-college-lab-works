# Write a Python function that takes a list and returns a new list with distinct elements from the first list. 
def func(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return l1
l=[1,2,3,4,1,2,34,12,54]
print(func(l))