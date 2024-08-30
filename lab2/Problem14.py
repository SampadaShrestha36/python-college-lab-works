#Write a python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”, or “Invalid” for non-integer inputs. This program should first check if the input is a valid integer “Invalid” for non-integer inputs. This program should first check if the input is a valid integer and then check for the other conditions.
n=input("Enter a number")
if(n.isdigit()):
    n=int(n)
    if(n%2==0 and n!=0):
        print("It is even")
    elif n%2==1:
        print("It is odd")
    else:
        print("It is zero")
else:
    print("Invalid input")
