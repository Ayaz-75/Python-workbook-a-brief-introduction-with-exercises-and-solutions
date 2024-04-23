'''
Exercise 35: Even or Odd?

Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd.


'''

def checkEvenOdd(number):
    if number % 2 == 0:
        answer = f"{number} is even"
    else:
        answer = f"{number} is odd"

    return answer



input_number = int(input("Enter the number: "))
result = checkEvenOdd(input_number)
print(result)
