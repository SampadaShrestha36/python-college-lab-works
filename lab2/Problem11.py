#Create a Python script that converts temperature from Fahrenheit to Celsius and vice versa, based on user input
f=int(input("enter the temperature in Fahrenheit"))
c=(f-32)*(5/9)
print("The temperature in celsius is",c)
g=int(input("Enter the temperature in celsius"))
d=(g*(9/5)+32)
print("The temperature in Fahrenheit is",d)