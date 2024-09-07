'''Write a Python program to construct the following pattern, using a nested for loop. 
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
*
'''

for i in range(1,10):
    if i<=5:
        for j in range(0,i):
            print('*',end="")
        print()
    else:
        for j in range(i,10):
            print('*',end="")
        print()
