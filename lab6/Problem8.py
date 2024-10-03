#Write a Python script to merge two Python dictionaries.  dict1 = {‘a’: 1, ‘b’: 2} and dict2 = {‘b’: 3, ‘c’:4} merge them into a single dictionary. What happens to the value of the key ‘b’? 
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
# dict1.update(dict2)
# print(dict1)
for i in dict2:
    dict1[i]=dict2[i]
print(dict1)  #value of b is updated as 3