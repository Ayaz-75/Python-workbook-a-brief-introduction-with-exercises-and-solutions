# Exercise 14: Height Units
'''
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters

'''

def compute_centimeters(no_feet, no_inches): # no_feet--> number of feet
                                             # no_inches--> number of inches
    cms_from_feet = (no_feet * 12) * 2.54
    cms_from_inches = no_inches * 2.54

    total_cms = cms_from_feet + cms_from_inches
    return total_cms



feet_input = int(input("Enter the feet: "))
inches_input = int(input("Enter the inches: "))

total_combined_cms = compute_centimeters(feet_input, inches_input)

print(f"Total height in Centimeters: {total_combined_cms}")
