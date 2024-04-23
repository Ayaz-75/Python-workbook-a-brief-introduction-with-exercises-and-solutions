'''
Exercise 67: Compute the Perimeter of a Polygon

Write a program that computes the perimeter of a polygon. Begin by reading the
x and y coordinates for the first point on the perimeter of the polygon from the
user. Then continue reading pairs of values until the user enters a blank line 
for the x-coordinate. Each time you read an additional coordinate you should 
compute the distance to the previous point and add it to the perimeter. When a 
blank line is entered for the x-coordinate your program should add the distance 
from the last point back to the first point to the perimeter. Then the perimeter 
should be displayed. Sample input and output values are shown below. The input 
values entered by the user are shown in bold.

Enter the first x-coordinate: 0
Enter the first y-coordinate: 0
Enter the nextt x-coordinate (blank to quit): 1
Enter the nextt y-coordinate: 0
Enter the nextt x-coordinate (blank to quit): 0
Enter the nextt y-coordinate: 1
Enter the nextt x-coordinate (blank to quit):
The perimeter of that polygon is 3.414213562373095

'''

# Compute the perimeter of a polygon constructed from points entered by the user. 
# A blank line will be entered for the x-coordinate to indicate that all of the 
# points have been entered.

# import the sqrt function from maths module
from math import sqrt

# store the value of perimeter of polygon in a variable named perimeter
perimeter = 0

# rading the values for first two coordinates from the user
first_coordinate = float(input("Enter the value for first coordinate: "))
second_coordinate = float(input("Enter the value for second coordinate: "))

# provide values for previous x and previous y
previous_x = first_coordinate
previous_y = second_coordinate

# read the remaining coordinates
line = input("Enter the next x-coordinate (blank to quit): ")

while line != "":
    # convert the x-coordinate to the number and read the next y-coordinate
    x = float(line)
    y = float(input("Enter the next y-coordinate: "))
    distance = sqrt((previous_x - x) ** 2 + (previous_y - y) ** 2)
    
    # setup previous_x and previous_y for next iteration of loop
    previous_x = x
    previous_y = y

    # read the next line
    line = input("Enter the value for x-coordinate (blank to quit): ")


# Compute the distance from the last point to the first point and add it to the 
# perimeter
distance = sqrt((first_coordinate - x) ** 2 + (second_coordinate - y) ** 2)
perimeter = perimeter + distance
# Display the result
print("The perimeter of that polygon is", perimeter)
