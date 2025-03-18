#  Create a child class called ElectricCar that inherits from the Car class. Add an attribute battery_size to the child class with a default value. Also, add a method describe_battery() that prints information about the battery size. 
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
class ElectricCar(Car):
    battery_size='75kWh'
    def describe_battery(self):
        print(self.battery_size)
c1=ElectricCar("Tesla", "Model S", 2022)
c1.describe_battery()