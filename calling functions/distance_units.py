
# Exercise 15: Distance Units

'''
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don't have them memorized

'''

def convert_distance(input_in_feet):
    distance_in_inches = input_in_feet * 12
    distance_in_yards = input_in_feet * 0.333
    distance_in_miles =  input_in_feet * 0.000189394


    return f"Distance in inches: {distance_in_inches}\nDistance in yards: {distance_in_yards}\nDistance in miles: {distance_in_miles}"




user_input = int(input("Enter the feet: "))
all_distances = convert_distance(user_input)

print(all_distances)
