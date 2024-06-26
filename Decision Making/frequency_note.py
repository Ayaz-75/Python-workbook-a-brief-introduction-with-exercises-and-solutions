'''
Exercise 42: Note to Frequency

The following table lists an octave of music notes, beginning with middle C, along
with their frequencies.

Note        Frequency (Hz)
 C4          261.63
 D4          293.66
 E4          329.63
 F4          349.23
 G4          392.00
 A4          440.00
 B4          493.88


Begin by writing a program that reads the name of a note from the user and
displays the note's frequency. Your program should support all of the notes listed
previously.

Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8. While this could be
done by adding many additional cases to your if statement, such a solution is
cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead,
you should exploit the relationship between notes in adjacent octaves. In particular, 
the frequency of any note in octave n is half the frequency of the corresponding 
note in octave n + 1. By using this relationship, you should be able to add support 
for the additional notes without adding additional cases to your if statement.


Hint: You will want to access the characters in the note entered by the user
individually when completing this exercise. Begin by separating the letter from
the octave. Then compute the frequency for that letter in the fourth octave using
the data in the table above. Once you have this frequency you should divide it
by 24-x , where x is the octave number entered by the user. This will halve or
double the frequency the correct number of times.

'''


def frequency_note(input_note):

    C4_FREQ = 261.63
    D4_FREQ = 293.66
    E4_FREQ = 329.63
    F4_FREQ = 349.23
    G4_FREQ = 392.00
    A4_FREQ = 440.00
    B4_FREQ = 493.88


    note = input_note[0]
    octave = int(input_note[1])

    if note == "C":
        freq = C4_FREQ 
    elif note == "D":
        freq = D4_FREQ
    elif note == "E":
        freq = E4_FREQ
    elif note == "F":
        freq = F4_FREQ 
    elif note == "G":
        freq = G4_FREQ 
    elif note == "A":
        freq = A4_FREQ 
    elif note == "B":
        freq = B4_FREQ

     
    freq = freq / 2 ** (4 - octave)
    print(f"The frequency for {input_note} is: {freq}")

user_given_note = input("Enter the note to find the freequency: ")
frequency_note(user_given_note)



