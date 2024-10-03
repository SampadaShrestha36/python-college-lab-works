# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
d={"Hello":3,"hi":2,"Bye":1,"Bye bye":0}
l=list(d.values())
l.sort(reverse=True)
m=l[:3]
for i in d:
    if d[i] in m:
        print(i,d[i])


