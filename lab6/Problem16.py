# Given a dictionary d = {‘a’:1, ‘b’:2, ‘c’:3}, write a python script to reverse the key-value pairs to get a new dictionary. 
d={'a':1,'b':2,'c':3}
e={}
for x,y in d.items():
    e[y]=x
print(e)