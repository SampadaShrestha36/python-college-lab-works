'''
1
01
101
0101
10101
010101
10101010
0101010101
101010101010
01010101010101
'''

k=1
l=1
for i in range(1,10):
    k=l
    for j in range(0,i):
        print(k,end="")
        if k==0:
            k=1
        else:
            k=0
    print(end="\n")
    if l==0:
        l=1
    else:
        l=0