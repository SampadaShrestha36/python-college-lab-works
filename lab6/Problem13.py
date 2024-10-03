#Write a Python program to sort a dictionary by values instead of keys. 
d={"Hello":3,"hi":2,"Bye":1}
for i in d:
    for j in d:
        if(d[i]>d[j]):
            i,j=j,i
            d[i],d[j]=d[j],d[i]
print(d)