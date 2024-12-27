#Write a Python function to find the maximum of three input numbers. 
def maximum(a,b,c):
    if a>b and a>c:
        print(f"{a} is maximum")
    elif b>a and b>c:
        print(f"{b} is maximum")
    elif c>a and c>b:
        print(f"{c} is maximum")
    else:
        print("They are equal")
a,b,c=int(input("Enter three numbers")),int(input()),int(input())
maximum(a,b,c)

    