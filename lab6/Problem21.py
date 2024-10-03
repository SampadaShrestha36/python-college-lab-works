# Write a Python program to find the key of the maximum and minimum values in a dictionary.
d={'a': 5, 'b': 14, 'c': 32, 'd': 35}
l=list(d.values())
l.sort()
for j in d:
    if d[j]==l[-1]:
        t=j
    if d[j]==l[0]:
        a=j
print("Maximum and minimum key values:",tuple(t)+tuple(a))
