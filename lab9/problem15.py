# Assume you have another file called car.py that contains the Car class. Write a new Python script that imports the Car class from car.py, creates an instance of Car, and calls the describe_car() method. 
from problem10 import Car
c1 = Car("toyota", "corolla", 2020)
c1.describe_car()