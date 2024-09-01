'''
10
9 8
7 6 5
4 3 2 1
'''
k=10
for i in range(0,4):
    for j in range(0,i+1):
        print(k,end=" ")
        k-=1
    print()