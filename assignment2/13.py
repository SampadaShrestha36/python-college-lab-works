'''
1
01
101
0101
'''
k=1
l=1
for i in range(1,5):
    k=l
    for j in range(0,i):
        print(k,end="")
        if k==0:
            k=1
        else:
            k=0
    print()
    if l==0:
        l=1
    else:
        l=0