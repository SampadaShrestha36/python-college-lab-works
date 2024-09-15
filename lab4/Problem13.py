# Write a Python Program to print a list in a reverse order. 
l=[1,2,3,4,5,6,7,8,9,10,"hi"]
#l.reverse()
n=[]
# for i in range(len(l)-1,0,-1):
#     n.append(l[i])
# n.append(l[0])
# l=n.copy()
# print(l)

for i in l[len(l)-1:0:-1]:
    n.append(i)
n.append(l[0])
l=n.copy()
print(l)