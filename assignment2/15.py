'''
1 2
2 3
3 4
4 5
5 6
'''
for i in range(1,6):
    for j in range(i,i+2):
        print(j,end=" ")
    print(end="\n")