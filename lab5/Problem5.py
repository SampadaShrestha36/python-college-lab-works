#Write a Python program to sort a tuple by its float element. 
l=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
for i in range(len(l)):
    for k in range(i+1,len(l)):
        for j in range(len(l[i])):
            try:
                s=float(l[i][j])
                m=float(l[k][j])
                if s<m:
                    l[i],l[k]=l[k],l[i]
            except ValueError:
                pass

print(l)