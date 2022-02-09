# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

TEMPLATE = "./Input/Letters/starting_letter.txt"
NAMES = "./Input/Names/invited_names.txt"
OUT_TEMP = "./Output/ReadyToSend/[name].txt"

with open(NAMES, 'r') as name_file:
    for name in name_file:
        name = name.strip()
        with open(TEMPLATE, 'r') as template:
            new_mail = template.readlines()
            new_mail[0] = new_mail[0].replace("[name]", name)
            out_file = OUT_TEMP.replace("[name]", name)
            with open(out_file, 'w') as output:
                output.writelines(new_mail)

# starting_letter.txt
# Dear [name],
# 
# You are invited to my birthday this Saturday.
# 
# Hope you can make it!
# 
# Angela

# invited_names.txt
# Aang
# Zuko
# Appa
# Katara
# Sokka
# Momo
# Uncle Iroh
# Toph
