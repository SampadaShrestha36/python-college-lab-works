#Write a  Python program to insert n values in a list and find those values in a list that are greater than a specified number.
l=[]
n=int(input("Enter the number of values to be inserted"))
while n>0:
    a=int(input("enter the element"))
    l.append(a)
    n-=1
a=int(input("enter the number "))
print(f"The values greater than {a} are:")
for j in l:
    if j>a:
        print(j,end=" ")
    
