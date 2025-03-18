# Write a Python class named Dog that has two attributes: name and age. Then, create an instance of your Dog class and print out the name and age of the dog. 

class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

d1=Dog('border collie','8')
print(d1.name)
print(d1.age)
    