#Write a Python program to sort a given list of strings (numbers) numerically.
l=['4', '12', '45', '7', '0', '100', '200', '-12', '-500'] 
n=[]
for i in l:
    i=(int(i))
    n.append(i)
l=sorted(n)
print(l)