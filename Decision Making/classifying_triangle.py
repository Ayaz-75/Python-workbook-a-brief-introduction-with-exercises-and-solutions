'''
Exercise 41: Classifying Triangles

A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
scalene. All three sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of the three sides of a triangle from the
user. Then display a message that states the triangle's type.

'''

def classifyTriangle(s1, s2,s3):
    if s1 == s2 == s3:
        print("Equilateral")

    if s1 == s2:
        if s1 and s2 != s3: 
            print("Isosceles")

    if s1 != s2 != s3:
        print("Scalene")


length_of_side1 = float(input("Enter length of side 1: "))
length_of_side2 = float(input("Enter length of side 2: "))
length_of_side3 = float(input("Enter length of side 3: "))

classifyTriangle(length_of_side1, length_of_side2, length_of_side3)
