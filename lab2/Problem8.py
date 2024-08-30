# Write code to take input from user and store it in a variable spam then print Hello if 1 is stored in spam, print Hi if 2 is stored in spam, and print Greetings! if anything else is stored in spam.
spam=input("enter a string")
if "1" in spam:
    print("Hello")
elif "2" in spam:
    print("Hi")
else:
    print("Greetings!")