'''
    * 
   *** 
  ***** 
 ******* 
********* 
 ******* 
  ***** 
   *** 
    *
'''
for i in range(0,5):
    for j in range(4,i,-1):
        print(end=" ")
    for j in range(0,(i+1)*2-1):
        print("*",end="")
    print(end="\n")
for i in range(4,0,-1):
    for j in range(i-1,4):
        print(end=" ")
    for j in range(i*2-1,0,-1):
        print("*",end="")
    print(end="\n")