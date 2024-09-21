#Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 
t1=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)) 
l=[]
print("Original Tuple:")
print(t1)
for b in range(len(t1[0])):
    a=0
    for i in t1:
        a=a+i[b]
    avg=a/len(t1)
    l.append(avg)
print("Avereage value of the numbers of the said tuple of tuples:")
print(l)
t2=((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3)) 
l1=[]
print("Original Tuple:")
print(t2)
for b in range(len(t2[0])):
    a=0
    for i in t2:
        a=a+i[b]
    avg=a/len(t2)
    l1.append(avg)
print("Avereage value of the numbers of the said tuple of tuples:")
print(l1)