'''
Exercise 39: Month Name to Number of Days

The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.


'''
def numberOfDays(month_name):
    if month_name == "Feburary":
        print("28 | 29")
    else:
        print("30 | 31")


user_input = input("Enter the name of month: ")
numberOfDays(user_input)
