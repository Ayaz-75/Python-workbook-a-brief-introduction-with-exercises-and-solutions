# Exercise 16: Area and Volume
'''
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr^2. The
volume of a sphere is computed using the formula volume = 4/3πr^3.

'''
from math import *

def calculate_area_and_volumne(radius):
    area_of_circle = pi * (radius ** 2)
    volume_of_sphare = 4/3 * pi * (radius ** 3)

    return f"Area of circle: {area_of_circle}\nVolume of sphare: {volume_of_sphare}"


radius_input = int(input("Enter the radius 'r': "))


area_and_volume = calculate_area_and_volumne(radius_input)
print(area_and_volume)
