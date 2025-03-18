#  Override the describe_car() method in the ElectricCar class to include information about its battery size along with the car's make, model, and year.
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
    battery_size=75
    def __init__(self,make,model,year,battery_size):
        self.battery_size=battery_size
        super().__init__(make,model,year)
    def describe_battery(self):
        print(self.battery_size)
    def calculate_range(self):
        range_in_miles = self.battery_size * 4  # Assume 4 miles per kWh
        print(f"This electric car can travel approximately {range_in_miles} miles on a full charge.")
    def describe_car(self):
        print(self.make,self.model,self.year,self.battery_size)
c1=ElectricCar("Tesla", "Model S", 2022,70)
c1.describe_car()
