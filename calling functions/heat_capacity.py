# Exercise 17: Heat Capacity

'''

The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material's specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
                                    q = mCΔT

Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.
'''
def find_total_energy(mass_of_some_water, delta_temp):
    q = mass_of_some_water * delta_temp
    return q


mass_of_water_by_user = float(input("Enter the mass of water: "))
temperature_change_from_user = float(input("Enter the temperature change by user: "))

total_energy = find_total_energy(mass_of_water_by_user, temperature_change_from_user)
print(f"Total energy required to achieve the desired temperature is: {total_energy}")

'''
Hint: The specific heat capacity of water is 4.186 Jg◦C. 
Because water has a density of 1.0 grams per milliliter, you can use grams and milliliters 
interchangeably in this exercise. Extend your program so that it also computes the 
cost of heating the water. Electricity is normally billed using units of kilowatt hours 
rather than Joules. In this exercise, you should assume that electricity costs 8.9 cents 
per kilowatt hour. Use your program to compute the cost of boiling the water needed for a 
cup of coffee.

Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.

'''



