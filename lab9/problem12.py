#  Modify the ElectricCar class to include an __init__() method that properly initializes the parent class's attributes as well as its own attribute battery_size.
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
    def __init__(self,make,model,year,battery_size):
        self.battery_size=battery_size
        super().__init__(make,model,year)
    def describe_battery(self):
        print(self.battery_size)
c1=ElectricCar("Tesla", "Model S", 2022,'70kWh')
c1.describe_battery()