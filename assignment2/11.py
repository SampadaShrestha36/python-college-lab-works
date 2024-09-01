'''
  0
 101
21012
'''
for i in range(0,3):
    for j in range(2,i,-1):
        print(end=" ")
    for j in range(i,-1,-1):
        print(j,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()