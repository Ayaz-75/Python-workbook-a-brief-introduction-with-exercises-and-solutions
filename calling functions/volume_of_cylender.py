
# Exercise 18: Volume of a Cylinder

'''
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place

'''
from math import *

def computeVolumeOfCylender(radius, height):
    # Formula to find volume of cylender: π * r^2 * h
      
    volume_of_cylender = pi * (radius **2) * height

    return volume_of_cylender


input_radius = float(input("Enter the radius of cylender: "))
input_height = float(input("Enter the height of cylender: "))

cylender_volmue = computeVolumeOfCylender(input_radius, input_height)
print(f"Volume of Cylender is: {round(cylender_volmue, 1)}")
