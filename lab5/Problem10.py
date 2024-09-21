#Write a Python program to compute the element-wise sum of given tuples.
t1=(1, 2, 3, 4) 
t2=(3, 5, 2, 1) 
t3=(2, 2, 3, 1) 
print("Original lists: ")
print(t1)
print(t2)
print(t3)
s=[]
print("Element-wise sum of the said tuples: ")
for i in range(len(t1)):
    a=t1[i]+t2[i]+t3[i]
    s.append(a)
print(tuple(s))