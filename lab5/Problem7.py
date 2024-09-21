#Write a Python program to calculate the product, multiplying all the numbers in a given tuple. 
t1=(4, 3, 2, 2, -1, 18) 
t2=(2, 4, 8, 8, 3, 2, 9) 
m=1
print("Original Tuple:")
print(t1)
for i in t1:
    m=m*i
print("Product - multiplying all the numbers of the said tuple:",m)
print("Original Tuple:")
print(t2)
m=1
for i in t2:
    m=m*i
print("Product - multiplying all the numbers of the said tuple:",m)
