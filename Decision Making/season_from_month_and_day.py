'''
Exercise 47: Season from Month and Day

The year is divided into four seasons: spring, summer, fall (or autumn) and winter.
While the exact dates that the seasons change vary a little bit from year to year
because of the way that the calendar is constructed, we will use the following dates
for this exercise:

                                         __________________________
                                        |Season      |First Day    |
                                        |____________|_____________|
                                        |Spring      |March 20     |
                                        |____________|_____________|
                                        |Summer      |June 21      |
                                        |____________|_____________|
                                        |Fall        |September 22 |
                                        |____________|_____________|
                                        |Winter      |December 21  |
                                        |____________|_____________|


Create a program that reads a month and day from the user. The user will
enter the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.

'''

def seasonFromMonth(month, day):
    if month == "march" and day >= 20 and day <= 30 or month == "april" and day >=1 and day <= 30 or month == "may" and day >= 1 and day <=30 or month == "june" and day >= 1 and day < 21:
        return "Spring"
    
    elif month == "june" and day >= 21 and day <= 30 or month == "july" and day >=1 and day <= 30 or month == "august" and day >= 1 and day <=30 or month == "september" and day >= 1 and day <= 22:
        return "Summer"

    elif month == "september" and day > 22 and day <= 30 or month == "october" and day >=1 and day <= 30 or month == "november" and day >= 1 and day <=30 or month == "december" and day >= 1 and day <= 21:
        return "Fall | Autumn"
    
    elif month == "december" and day >= 21 and day <= 30 or month == "january" and day >=1 and day <= 30 or month == "feburary" and day >= 1 and day <=30 or month == "march" and day >= 1 and day < 20:
        return "Winter"
    
    else:
        return "Invalid month or date!!!"


month_input = input("Enter the month: ")
day_input = int(input("Enter the day: "))



season_from_month_and_day = seasonFromMonth(month_input, day_input)
print(season_from_month_and_day)
