'''
Exercise 70: Parity Bits

A parity bit is a simple mechanism for detecting errors in data transmitted over an
unreliable connection such as a telephone line. The basic idea is that an additional bit
is transmitted after each group of 8 bits so that a single bit error in the transmission
can be detected.
Parity bits can be computed for either even parity or odd parity. If even parity
is selected then the parity bit that is transmitted is chosen so that the total number
of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity
is selected the parity bit is chosen so that the total number of one bits transmitted
is odd.
Write a program that computes the parity bit for groups of 8 bits entered by the
user using even parity. Your program should read strings containing 8 bits until the
user enters a blank line. After each string is entered by the user your program should
display a clear message indicating whether the parity bit should be 0 or 1. Display
an appropriate error message if the user enters something other than 8 bits.
Hint: You should read the input from the user as a string. Then you can use
the count method to help you determine the number of zeros and ones in the
string. Information about the count method is available online.

'''

# in order to compute the parity bit we have the following methods
# 1- For odd parity, count the 1s in the message. If the count is even, add a 1; otherwise, add a 0.
# 2- For even parity, do the opposite: If the number of 1s is even, add a 0; otherwise, add a 1.

# first step is to read input from user for groups of 8 bits entered by the user using even parity
# program should read strings containing 8 bits until the user enters a blank line
# After each string is entered by the user your program should display a clear message indicating 
# whether the parity bit should be 0 or 1

# reading input from user for first string of 8 bits
user_input = input("Enter the first input of 8 bits: ")

# storing the parity bit value in a variable called a parity
parity = 0

# keeping track of zero and ones count 
zero_count = 0
ones_count = 0


# checking if the length of user input is exactly 8
if len(user_input) == 8:
    # keep reading the input from user until a blank line is enterd
    while user_input != "":
        for each_value in user_input: # this for loop is used to check the character is zero or 1
            if each_value == "0": # if the value is zero add 1 to the zero_count varible
                zero_count += 1 
            else: # if the value is 1 add 1 to the ones_count varible
                ones_count += 1
        if ones_count % 2 != 0: # condition to check if the parity is even or odd
            parity += 1
        else:
            parity = 0

        # taking the input for next 8 bit string from user
        user_input = input("Enter the Next input of 8 bits: ")

    print(f"Parity bit is: {parity}")
else:
    if len(user_input) < 8:
        print("Input string has length less than 8 bits")
    else:
        print("Input string has length grater than 8 bits")
 
