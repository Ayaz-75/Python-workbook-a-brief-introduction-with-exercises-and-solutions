'''
Exercise 57: Cell Phone Bill

A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.


Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.

'''

def billCounter(minutes, messages):
    
    cost = 0

    if minutes <= 50 and messages <= 50:
        cost = cost + 15.00
    elif minutes > 50 and messages > 50:
        cost = 15.00 + ((minutes - 50) * 0.25 + (messages - 50) * 0.15)

    return f"Total bill will be: ${cost}"


minutes = int(input("Enter the number of minutes: "))
text_messages = int(input("Enter the number of text messages: "))


result = billCounter(minutes, text_messages)
print(result)
