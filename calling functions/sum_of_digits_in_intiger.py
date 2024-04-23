'''
Exercise 32: Sum of the Digits in an Integer

Develop a program that reads a four-digit integer from the user and displays the sum
of its digits. For example, if the user enters 3141 then your program should display
3+1+4+1=9.

'''

def sumOfDigits(number):
    sum_of_digits = 0
    if number.isdigit() and len(number) == 4:
        int_no = int(number)
        thousands_digit = int_no // 1000
        hundred_digit = (int_no % 1000) // 100
        tens_digit = (int_no % 100) // 10
        ones_digit = int_no % 10
        sum_of_digits = thousands_digit + hundred_digit + tens_digit + ones_digit

    else:
        print("Enter a valid number!!!!!")
    return sum_of_digits


user_input = input("Enter a 4 digit number: ")
sum_of_digits = sumOfDigits(user_input)
print(sum_of_digits)
