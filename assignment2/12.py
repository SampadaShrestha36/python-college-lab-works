'''
   1
  123
 12345
1234567
'''
for i in range(1,5):
    for j in range(4,i,-1):
        print(end=" ")
    for j in range(0,(2*i)-1):
        print(j+1,end="")
    print()