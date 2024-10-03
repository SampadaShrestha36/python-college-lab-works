#Write a Python program to find the specified number of maximum values in a given dictionary.
d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
n=int(input("Enter the number of max values"))
l=list(d.values())
l.sort(reverse=True)
m=l[:n]
o=[]
s=set()  #for keys that have already been printed
for i in m:
    for j in d:
        if d[j]==i and j not in s:
            o.append(j)
            s.add(j)   #not to repeat those keys again
print(n,"maximum value(s) in the said dictionary: ",o)

