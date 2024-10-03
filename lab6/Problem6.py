#Write a Python program to get the key, value and item in a dictionary.
d={'name':'Hari','age':'29','city':'Bhaktapur'}
print("keys:")
for i in d.keys():
    print(i,end=" ")
print("\nvalues:")
for i in d:
    print(d.get(i),end=" ")
print("\nitems:")
for i in d.items():
    print(i,end=" ")