'''
Exercise 71: Approximate π

The value of π can be approximated by the following infinite series:
π ≈ 3 + 4/(2 * 3 * 4) - 4 /(4 * 5 * 6) + 4/(6 * 7 * 8) - 4/(8 * 9 * 10 +
4/(10 * 11 * 12) - ···

Write a program that displays 15 approximations of π. The first approximation 
should make use of only the first term from the infinite series. Each additional
approximation displayed by your program should include one more term in the series,
making it a better approximation of π than any of the approximations displayed previously

'''

# we will want compute the approximation of π 'pi'. 
# Initialize the total sum and the sign for alternating terms

pi_approximation = 3.0
sign = 1

# Loop to calculate and display 15 approximations
for n in range(2, 32, 2):  # We'll use terms 2, 4, 6, ..., 30 so that we can compute 15 terms.

    term = 4 / (n * (n + 1) * (n + 2))  # Calculate the next term
    pi_approximation += sign * term  # Add or subtract the term

    sign *= -1  # Alternate the sign for the next term
    print(f"Term computed form 4 / ({n} * {n} + 1 * {n} + 2) is: {term}")

    # Display the current approximation
    print()
    print(f"Approximation {n//2}: π ≈ {pi_approximation}")
