'''Exercise 46:What Color Is That Square?

Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below:

 ___________________________________________________________________
|     |  a   |  b   |   c   |   d   |   e   |    f  |   g   |   h   |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  1  |  X   |      |   X   |       |   X   |       |   X   |       |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  2  |      |  X   |       |   X   |       |   X   |       |   X   |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  3  |  X   |      |   X   |       |   X   |       |   X   |       |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  4  |      |  X   |       |   X   |       |   X   |       |   X   |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  5  |  X   |      |   X   |       |   X   |       |   X   |       |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  6  |      |  X   |       |   X   |       |   X   |       |   X   |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  7  |  X   |      |   X   |       |   X   |       |   X   |       |
|_____|______|______|_______|_______|_______|_______|_______|_______|
|  8  |      |  X   |       |   X   |       |    X  |       |   X   |
|_____|______|______|_______|_______|_______|_______|_______|_______|

Write a program that reads a position from the user. Use an if statement to
determine if the column begins with a black square or a white square. Then use
modular arithmetic to report the color of the square in that row. For example, if the
user enters a1 then your program should report that the square is black. If the user
enters d5 then your program should report that the square is white. Your program
may assume that a valid position will always be entered. It does not need to perform
any error checking.

'''
row1 = ["🏀","🏐","🏀","🏐","🏀", "🏐","🏀", "🏐"]
row2 = ["🏐","🏀","🏐","🏀","🏐", "🏀","🏐", "🏀"]
row3 = ["🏀","🏐","🏀","🏐","🏀", "🏐","🏀", "🏐"]
row4 = ["🏐","🏀","🏐","🏀","🏐", "🏀","🏐", "🏀"]
row5 = ["🏀","🏐","🏀","🏐","🏀", "🏐","🏀", "🏐"]
row6 = ["🏐","🏀","🏐","🏀","🏐", "🏀","🏐", "🏀"]
row7 = ["🏀","🏐","🏀","🏐","🏀", "🏐","🏀", "🏐"]
row8 = ["🏐","🏀","🏐","🏀","🏐", "🏀","🏐", "🏀"]


print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")


position_input = input("Enter the postion: ")

map_carta = [row1, row2, row3, row4, row5, row6, row7, row8]
selected_position = map_carta[int(position_input[0]) - 1][int(position_input[1]) - 1] 

print(f"Selected position contains a {selected_position} ")
# print(map_carta[int(position_input[0])][int(position_input[1])])
# print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}")




# if column_position == 'a':
#     column_position = 1

# elif column_position == 'b':
#     column_position == 2

# elif column_position == 'b':
#     column_position == 3

# elif column_position == 'b':
#     column_position == 4

# elif column_position == 'b':
#     column_position == 5

# elif column_position == 'b':
#     column_position == 6

# elif column_position == 'b':
#     column_position == 7

# elif column_position == 'b':
#     column_position == 8

