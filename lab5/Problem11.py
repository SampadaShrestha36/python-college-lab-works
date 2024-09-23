# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
l1=[(1, 2), (2, 3), (3, 4)] 
l=[]
print("Original list of tuples: ")
print(l1)
for i in l1:
    s=0
    for j in i:
        s=s+j
    l.append(s)
print("Sum of all the elements of each tuple stored inside the said list of tuples: ")
print(l)
l2=[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)] 
l=[]
print("Original list of tuples: ")
print(l2)
for i in l2:
    s=0
    for j in i:
        s=s+j
    l.append(s)
print("Sum of all the elements of each tuple stored inside the said list of tuples: ")
print(l)