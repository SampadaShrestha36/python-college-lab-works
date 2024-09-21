#Write a Python program to find repeated items in a tuple. 
t=(1,2,3,1,2,4)
l=[]
print("the repeated items are:")
for i in t:
    if i not in l:
        l.append(i)
    else:
        print(i)