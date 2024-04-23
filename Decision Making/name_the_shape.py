'''
Exercise 38: Name That Shape

Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.

'''


def nameShape(number_of_sides):
    if number_of_sides == 3:
        print("Shape is Triangle!")
    elif number_of_sides == 4:
        print("Shape is Square | Rectangle")
    elif number_of_sides == 5:
        print("Shape is Pentagone")
    elif number_of_sides == 6:
        print("Shape is Hexagone")
    elif number_of_sides == 7:
        print("Shape is Heptagone")
    elif number_of_sides == 8:
        print("Shape is Octagone")
    elif number_of_sides == 9:
        print("Shape is Nenagone")
    elif number_of_sides == 10:
        print("Shape is Decagone")
    else:
        print("Number of sides is out of range!!!!!!!!!!!!!!")


user_input = int(input("Enter number of sides: "))

nameShape(user_input)
