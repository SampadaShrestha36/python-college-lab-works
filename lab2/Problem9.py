#Write a Python script that takes two numbers as input and prints their sum, difference, product, and quotient using match case.
a,b=int(input("Enter two numbers:")),int(input())
n=input("Enter operation")
match n:
    case "+":
        print(f"The sum is {a+b}")
    case "-":
        print(f"The difference is {a-b}")
    case "*":
        print(f"The product is {a*b}")
    case "%":
        print(f"The quotient is {a//b}")
    case other:
        print("Invalid operation")
