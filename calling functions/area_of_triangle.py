'''
Exercise 21: Area of a Triangle

The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = (b * h) / 2

Write a program that allows the user to enter values for b and h. The program should
then compute and display the area of a triangle with base length b and height h.

'''

def areaOfTriangle(b, h):
    a = ( b * h ) / 2
    return a


base_of_triangle = float(input("Enter the length of base of the triangle: "))
height_of_triangle = float(input("Enter the height of triangle: "))


area_of_triangle = areaOfTriangle(base_of_triangle, height_of_triangle)
print(area_of_triangle)
