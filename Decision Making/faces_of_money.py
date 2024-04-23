'''
Exercise 44: Faces on Money

It is common for images of a country's previous leaders, or other individuals of historical 
significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in below.

                    Individual           Amount
                    George Washington      $1
                    Thomas Jefferson       $2
                    Abraham Lincoln        $5
                    Alexander Hamilton     $10
                    Andrew Jackson         $20
                    Ulysses S. Grant       $50
                    Benjamin Franklin      $100

Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.

While two dollar banknotes are rarely seen in circulation in the United States,
they are legal tender that can be spent just like any other denomination. The
United States has also issued banknotes in denominations of $500, $1,000,
$5,000, and $10,000 for public use. However, high denomination banknotes
have not been printed since 1945 and were officially discontinued in 1969. As
a result, we will not consider them in this exercise.

'''

def facesOfMoney(banknote):
    if banknote == 1  :
        print(f"George Washington's picture appers on ${banknote} note!")
    elif banknote == 2  :
        print(f"Thomas Jefferson picture appers on ${banknote} note!")
    elif banknote == 5  :
        print(f"Abraham Lincoln picture appers on ${banknote} note!")
    elif banknote == 10 :
        print(f"Alexander Hamilton picture appers on ${banknote} note!")
    elif banknote == 20 :
        print(f"Andrew Jackson picture appers on ${banknote} note!")
    elif banknote == 50 :
        print(f"Ulysses S. Grant picture appers on ${banknote} note!")
    elif banknote == 100:
        print(f"Benjamin Franklin picture appers on ${banknote} note!")
    else:
        print("invalid banknote!!!!!")



user_input = int(input("Enter the banknote: $"))
facesOfMoney(user_input)
