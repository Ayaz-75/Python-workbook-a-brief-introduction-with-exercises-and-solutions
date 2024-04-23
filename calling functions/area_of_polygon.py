'''
Exercise 23: Area of a Regular Polygon


A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:

area = (n * s^2) / 4 * (tan (π/n))

Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.

'''

from math import *

def areaOfPolygon(s, n): # s is the length of a side and n is the number of sides
    area = abs(n * (s**2) / 4 * (tan(pi/n)))
    return area


length_of_side = float(input("Enter the length of the each side in cm: "))
number_of_sides = int(input("Enter the number of sides of polygon: "))

area_of_polygon = areaOfPolygon(length_of_side, number_of_sides)
print("Area of polygon is: ", area_of_polygon)

