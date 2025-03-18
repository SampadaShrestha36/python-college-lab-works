# Modify the Car class so that it has a default value for an attribute called fuel_level, with a default value of 100. Add a method check_fuel_level() that prints the car's current fuel level.
class Car:
    fuel_level=100
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
    def check_fuel_level(self):
        print(self.fuel_level)
c1 = Car("toyota", "corolla", 2020)
c1.describe_car()
c1.check_fuel_level()