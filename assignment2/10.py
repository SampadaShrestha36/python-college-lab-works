'''
   1
  121
 12321
1234321
'''
for i in range(0,4):
    for j in range(3,i,-1):
        print(end=" ")
    for j in range(1,i+2):
        print(j,end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()
   #or print(end="\n")
