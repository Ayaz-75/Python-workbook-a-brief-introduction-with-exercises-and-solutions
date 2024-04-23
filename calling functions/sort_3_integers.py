'''
Exercise 33: Sort 3 Integers

Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.

'''

def sortThree(n1, n2, n3):
    minimum_value = min(n1, n2, n3)
    maximum_value = max(n1, n2, n3)

    sum_of_three = n1 + n2 + n3
    middle_value = sum_of_three - (minimum_value + maximum_value)

    final_sorted_values = (minimum_value, middle_value, maximum_value)

    return final_sorted_values


sorted_values = sortThree(3, 1, 5)
print(sorted_values)
