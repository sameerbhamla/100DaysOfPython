def caesar(word, shift_number, direction):
    caesar_text = ""
    for letter in word:
        position = alphabet.index(letter)
        if direction == 'encode':
            new_position = position + shift_number
            while new_position > 25:
                new_position -= 26
        elif direction == 'decode':
            new_position = position - shift_number
            while new_position < 0:
                new_position += 26
        new_letter = alphabet[new_position]
        caesar_text += new_letter
    print(f"The {direction}d text is {caesar_text}")

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
game_is_on = True
while game_is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(word=text, shift_number=shift, direction=direction)
    response = input("Do you want to play again?: (Y/N) ")
    if response.upper == 'Y':
        pass
    elif response.upper() == 'N':
        game_is_on = False
