'''
Exercise 72: Fizz-Buzz

Fizz-Buzz is a game that is sometimes played by children to help them learn about
division. The players are commonly arranged in a circle so that the game can progress
from player to player continually. The starting player begins by saying one, and then
play passes to the player to the left. Each subsequent player is responsible for the
next integer in sequence before play passes to the following player. On a player's
turn they must either say their number or one of following substitutions:

• If the player's number is divisible by 3 then the player says fizz instead of their
number.
• If the player's number is divisible by 5 then the player says buzz instead of their
number.

A player must say both fizz and buzz for numbers that are divisible by both 3
and 5. Any player that fails to perform the correct substitution or hesitates before
answering is eliminated from the game. The last player remaining is the winner.


Write a program that displays the answers for the first 100 numbers in the FizzBuzz game. 
Each answer should be displayed on its own line.
'''


# initializing the starting point for while loop to run
i = 1

# while number is less than or equal to the 100 keep loop running
while i <= 100:
    if i % 3 == 0 and i % 5 == 0: # if the number is divisible by both 3 and 5 print FizzBuzz instead of number
        print("FizzBuzz")
    elif i % 3 == 0: # if number(i) is divisible by 3 print Fizz instead of number
        print("Fizz")

    elif i % 5 == 0: # if number(i) is divisible by 5 print Buzz instead of number
        print("Buzz")

    else: # else print the actual number in the series
        print(i)
    i += 1

