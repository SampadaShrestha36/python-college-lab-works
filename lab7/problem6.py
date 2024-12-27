# Write a python function that accepts radius and returns the area and circumference of a circle. Import Pi from Math. 
from math import pi
def circle(r):
    a=pi*r*r
    p=2*pi*r
    return a,p
r=int(input("enter the radius"))
a,p=circle(r)
print(f"area={a} and circumference={p}")