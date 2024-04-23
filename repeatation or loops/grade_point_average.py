'''
Exercise 68: Compute a Grade Point Average

Exercise 52 includes a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 52 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line.
 ______________________________
|Letter Grade    |     Points  |
|________________|_____________|
|    A+          |       4.0   |
|    A           |       4.0   |
|    A-          |       3.7   |
|    B+          |       3.3   |
|    B           |       3.0   |
|    B-          |       2.7   |
|    C+          |       2.3   |
|    C           |       2.0   |
|    C-          |       1.7   |
|    D+          |       1.3   |
|    D           |       1.0   |
|    F           |       0     |
|________________|_____________|

'''

# iniatilise the variables for grade point total and keeping track of the iterations(count)
grade_point_total = 0 
count = 0

# Reading the first Grade point letter from user
user_provided_grade_letter = input("Enter the Grade point Letter: ")

# while user does not enters the blank line keep reading input from user
while user_provided_grade_letter != "":

    # checking for the given grade point letter condition
    if user_provided_grade_letter == "A+" or user_provided_grade_letter == "A":
        grade_point_total += 4.0

    elif user_provided_grade_letter == "A-":
        grade_point_total += 3.7

    elif user_provided_grade_letter == "B+":
        grade_point_total += 3.3

    elif user_provided_grade_letter == "B":
        grade_point_total += 3.0

    elif user_provided_grade_letter == "B-":
        grade_point_total += 2.7

    elif user_provided_grade_letter == "C+":
        grade_point_total += 2.3

    elif user_provided_grade_letter == "C":
        grade_point_total += 2.0

    elif user_provided_grade_letter == "C-":
        grade_point_total += 1.7

    elif user_provided_grade_letter == "D+":
        grade_point_total += 1.3

    elif user_provided_grade_letter == "D":
        grade_point_total += 1.0

    elif user_provided_grade_letter == "F":
        grade_point_total += 0

    else:
        print("Invalid input grade point letter !!!!!!!!!!!")

    # adding 1 to the count variable each time loop has completed
    count += 1

    # print(f"Total grade points: {grade_point_total}")
    # print(f"Repeatation has been occured {count} times")

    user_provided_grade_letter = input("Enter the next Grade point Letter: ")

grade_point_average = grade_point_total / count
print(f"Grade point Average is: {grade_point_average}")
