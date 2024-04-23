# Exercise 12: Distance Between Two Points on Earth

'''
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth's
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
The value 6371.01 in the previous equation wasn't selected at random. It is the
average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
Hint: Python's trigonometric functions operate in radians. As a result, you will
need to convert the user's input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians

'''

import math

def degrees_to_radians(degrees):
    return degrees * math.pi / 180

def find_distance_btw_two_points(t1, g1, t2, g2):
    t1 = degrees_to_radians(t1)
    g1 = degrees_to_radians(g1)
    t2 = degrees_to_radians(t2)
    g2 = degrees_to_radians(g2)

    distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2) * math.cos(g1 - g2))
    return distance



lat_1 = float(input("Enter the lattitude of first point: "))
long_1 = float(input("Enter the longitude of first point: "))

lat_2 = float(input("Enter the lattitude of second point: "))
long_2 = float(input("Enter the longitude of second point: "))


total_distance_in_km = find_distance_btw_two_points(lat_1, long_1, lat_2, long_2)

print(f"Total distance between two points on earth in kilometers is: {round(total_distance_in_km, 2)}")

