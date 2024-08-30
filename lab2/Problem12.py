#Create a program that asks for an age and prints “Child” if the age is less than 12, “Teenager” if the age is between 13 and 19, and “Adult” for ages 20 and above
age=int(input("Enter the age"))
if age<=12:
    print("child")
elif age>=13 and age<=19:
    print("Teenager")
else:
    print("Adult")
    