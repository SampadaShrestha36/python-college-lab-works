# Define a class named Car with attributes make, model, and year. Add a method describe_car() that prints a neatly formatted descriptive name of the car. Then, create an instance of Car and call this method. 
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
c1 = Car("toyota", "corolla", 2020)
c1.describe_car()