'''
Exercise 7: Sum of the First n Positive Integers

Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum = (n)(n + 1)/2

'''

def find_sum_of_n(n):
    sum_of_n = 0
    for i in range(1, n+1):
        sum_of_n += i
    return sum_of_n



number = int(input("Enter the number: "))
result = find_sum_of_n(number)


print(result)

