#Create a script that converts a list of tuples, [(‘a’, 1), (‘b’, 2), (‘c’, 3)], into a dictionary. 
l=[('a',1),('b',2),('c',3)]
d=dict()
for i in l:
    d[i[0]]=i[1]
print(d)