import pandas

nato_phonetic_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
code_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}
# print(code_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
result = [code_dict[letter] for letter in user_input if letter in code_dict]
print(result)
