'''
Exercise 45: Date to Holiday Name

Canada has three national holidays which fall on the same dates each year.
                    
                    'Holiday'       |   'Date'   
                    ________________________________
                                    |
                    New Year's Day  |  January 1
                                    |
                    Canada Day      |   July 1
                                    |
                    Christmas Day   |  December 25


Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday's name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.

Canada has two additional national holidays, Good Friday and Labour Day,
whose dates vary from year to year. There are also numerous provincial and
territorial holidays, some of which have fixed dates, and some of which have
variable dates. We will not consider any of these additional holidays in this
exercise.

'''
def dateToholiday(month, day):
    if month == 'January' and day == 1:
        print("New Year's Day")
    elif month == 'July' and day == 1:
        print("Canada Day")
    elif month == "December":
        print("Christmas Day")
    else:
        print("The entered month and day do not correspond to a fixed-date holiday")


input_month = input("Enter the month: ")
input_day = int(input("Enter the month: "))


date_to_holiday = dateToholiday(input_month, input_day)
