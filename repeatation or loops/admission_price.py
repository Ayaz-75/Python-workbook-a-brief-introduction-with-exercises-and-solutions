'''
Exercise 69: Admission Price

A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.

Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.

'''

age_of_guest = input("Enter the age of 1st member of group: ")

ticket_cost = 0

while age_of_guest != "":
    age_of_guest = float(age_of_guest)
    if age_of_guest > 0 and age_of_guest <=2:
        ticket_cost += 0
    elif age_of_guest >= 3 and age_of_guest <= 12:
        ticket_cost += 14
    elif age_of_guest >= 65 and age_of_guest < 150:
        ticket_cost += 18
    elif age_of_guest <= 0 or age_of_guest >= 150:
        print(f"Invalid age entered for {age_of_guest} !!!")
        break
    else:
        ticket_cost += 23

    age_of_guest = input("Enter the age of next member of group: ")

print(f"Admission cost for the entire group is: ${ticket_cost}")

