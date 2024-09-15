#Write a Python Program to merge two lists and removes all duplicates from the combined list
l1=[1,2,3,4,5,6,7]
l2=[1,2,3,4,8,9,10]
l=l1+l2
n=[]
for i in l:
    if i not in n:
        n.append(i)
l=n.copy()
print(l)
