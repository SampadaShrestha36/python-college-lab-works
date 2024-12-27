# Write a function that takes two arguments, name and age and returns a dictionary with these as keys and their respective values. 
def func(name,age):
    d={}
    d['name']=name
    d['age']=age
    return d
name=input("enter your name")
age=input("enter your age")
print(func(name,age))