# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')


# TODO 1. Create a dictionary in this format:
new_dict = {row.letter:row.code for (index,row) in data.iterrows()}
print(new_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word>: ").upper()
letter_list = [new_dict[letter] for letter in user_input]
print(letter_list)