# Create two instances from the Dog class. For the first instance, set the name to 'Bruno' and age to 2. For the second instance, set the name to 'Sher' and age to 3. Print out the information for both dogs. 
class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
d1=Dog('Bruno',2)
d2=Dog('Sher',3)
d1.display()
d2.display()