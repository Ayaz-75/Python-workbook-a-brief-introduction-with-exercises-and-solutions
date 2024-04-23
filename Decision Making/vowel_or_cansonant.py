'''
Exercise 37:Vowel or Consonant

In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

'''

def checkVowel(letter):
    
    if letter == ('a', 'e', 'i', 'o', 'u'):
        print(f"You entered {letter} and it is Vowel")
    
    elif letter == 'y':
        print(f"Sometimes {letter} is a vowel and sometimes y is a consonant")

    else:
        print(f"You entered {letter} and it is a consonant")


user_input = input("Enter any letter from a to z: ").lower()
checkVowel(user_input)

        