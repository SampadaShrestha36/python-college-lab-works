#  Add a method to the Car class that allows you to update the car's fuel_level. Then, create an instance of Car, update its fuel_level to 50, and call check_fuel_level() to verify the change.
class Car:
    fuel_level=100
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
    def update_fuel_level(self,fuel_level):
        self.fuel_level=fuel_level
    def check_fuel_level(self):
        print(self.fuel_level)
c1 = Car("toyota", "corolla", 2020)
c1.describe_car()
c1.update_fuel_level(50)
c1.check_fuel_level()