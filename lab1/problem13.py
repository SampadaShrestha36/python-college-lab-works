#print sum of two numbers but if sum in between 15 and 20, print 20
a=int(input("enter a number"))
b=int(input("enter a number"))
sum=a+b
if not(sum>=15 and sum<=20):
    print(sum)
else:
    print("20")