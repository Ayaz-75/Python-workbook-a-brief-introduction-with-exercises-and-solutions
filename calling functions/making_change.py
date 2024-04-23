# 13: Making Change

'''
Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.

Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.

A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
because one side of the coin has a loon (a type of bird) on it. The two dollar
coin, referred to as a toonie, was introduced 9 years later. It's name is derived
from the combination of the number two and the name of the loonie.

'''

def make_change(cents_user_gives):
    # A penny is equal to 1 cent. A nickel is equal to 5 cents. A dime is equal to 10 cents. 
    # A quarter is equal to 25 cents.
    total_amount = cents_user_gives
    nickles = total_amount * 0.2
    dimes = nickles * 0.1
    quarters = dimes * 0.04

    return f"Here is your change \nNickes: {round(nickles, 2)}, \nDimes: {round(dimes, 2)}\nQuarters: {round(quarters, 2)}"



input_cents = int(input("Enter the cents: "))


total = make_change(input_cents)
print(total)
