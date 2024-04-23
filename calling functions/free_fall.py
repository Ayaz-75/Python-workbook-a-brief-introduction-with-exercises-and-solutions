
# Exercise 19: Free Fall

'''
Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2. You can use the formula (vf = √ vi^2 + 2ad) to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.

'''
from math import *

def determineSpeed(height):
    vi = 0
    a = 9.8
    vf = sqrt((vi ** 2) + 2*(a * height))

    return vf

height = float(input("Enter height: "))

final_velocity = determineSpeed(height)
print(final_velocity)


