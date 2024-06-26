'''
Exercise 22: Area of a Triangle (Again)


In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = √ s * (s - s1) * (s - s2) * (s - s3)


Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.

'''

import math

def calculatArea(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    area = math.sqrt(abs(s * ((s - s1) * (s - s2) * (s - s3))))
    return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))


total_area = calculatArea(side1, side2, side3)
print(total_area)
