'''
Exercise 5: Bottle Deposits

--->In many jurisdictions a small deposit is added to drink containers to encourage people
    to recycle them. In one particular jurisdiction, drink containers holding one liter or
    less have a $0.10 deposit, and drink containers holding more than one liter have a
    $0.25 deposit.
    Write a program that reads the number of containers of each size from the user.
    Your program should continue by computing and displaying the refund that will be
    received for returning those containers. Format the output so that it includes a dollar
    sign and two digits to the right of the decimal point.

'''

def compute_refund(no_of_containers_above_litr, no_of_containers_below_litr):
    refund = (no_of_containers_above_litr * 0.25) + (no_of_containers_below_litr * 0.10)
    return f"Refund: ${round(refund, 3)}"



no_abo_ltr = float(input("Enter no of containers above 1 litre: "))
no_blo_ltr = float(input("Enter no of containers below 1 litre: "))


total_refund = compute_refund(no_abo_ltr, no_blo_ltr)
print(total_refund)
