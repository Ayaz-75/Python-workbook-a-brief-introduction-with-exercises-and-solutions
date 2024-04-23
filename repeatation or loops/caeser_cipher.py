'''
Exercise 73: Caesar Cipher

One of the first known examples of encryption was used by Julius Caesar. Caesar
needed to provide written instructions to his generals, but he didn't want his enemies
to learn his plans if the message slipped into their hands. As a result, he developed
what later became known as the Caesar cipher.
The idea behind this cipher is simple (and as such, it provides no protection against
modern code breaking techniques). Each letter in the original message is shifted by
3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.

The last three letters in the alphabet are wrapped around to the beginning: X becomes
A, Y becomes B and Z becomes C. Non-letter characters are not modified by the
cipher.

Write a program that implements a Caesar cipher. Allow the user to supply the
message and the shift amount, and then display the shifted message. Ensure that
your program encodes both uppercase and lowercase letters. Your program should
also support negative shift values so that it can be used both to encode messages and
decode messages.

'''

message = input("Enter the message text: ")
shift_amount = int(input("Enter shift amount: "))

def caeserCipher(message, shift_amount):
    new_message = ""
    for character in message:
        if character >= "a" or character <= "z":
            if shift_amount < 0:
                new_order = ord(character) + shift_amount
            else:
                new_order = ord(character) - shift_amount
        new_message += chr(new_order)
    return new_message
print(caeserCipher(message, shift_amount))
