#Write a Python program to replace the last value of tuples in a list. 
l=[(10,20,40),(40,50,60),(70,80,90)]
m=[]
for i in l:
    a=list(i)
    a[-1]=100
    b=tuple(a)
    m.append(b)
print(m)
