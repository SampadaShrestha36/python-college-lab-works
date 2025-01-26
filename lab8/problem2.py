# Write a Python function to check whether a number falls within a given range.
def func(n):
    if n in range(10,101):
        print("It is in range 10 to 100")
    else:
        print("It is not in range 10 to 100")
n=int(input("Enter a numeber"))
func(n)