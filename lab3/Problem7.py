#Write a Python program to input n numbers from user; count the number of even and odd numbers from the input numbers and exit until the user input ‘0’. 
e=0
o=0
n=int(input("Enter the numbers"))
while(True):
    if n%2==0 and n!=0:
        e+=1
    elif n%2==1:
        o+=1
    else:
        print(f"The number of odd numbers: {o}")
        print(f"the number of even numbers: {e}")
        exit()
    n=int(input())