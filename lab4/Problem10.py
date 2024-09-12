#Write a Python Program to check if each number is prime in a given list of numbers. Print the prime numbers if any, otherwise print “no prime numbers”.
l=[2,3,4,5,6,7,8,9]
l=[4,6,8]
a=False
for i in l:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a=True
        print(i)
if not a:
    print("no prime numbers")