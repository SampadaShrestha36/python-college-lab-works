# Write a Python program to count the even and odd numbers from a given list and also print them separately. 
def count(l):
    even=0
    odd=0
    l1,l2=[],[]
    for i in l:
        if i%2==0:
            even=even+1
            l1.append(i)
        else:
            odd=odd+1
            l2.append(i)
    return even, odd, l1, l2
l=[1,2,3,4,5,6,7,8,9,10]
even,odd,l1,l2=count(l)
print("even numbers=",even,"odd numbers=",odd)
print("Even numbers are",l1)
print("Odd numbers are", l2)
        