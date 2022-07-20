###
### A text-based Python program to convert Strings into Morse Code and back to plain text
###
import re

MORSE_CODE_DATA = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt_to_morse(msg):
    cipher_text = ''
    for i in msg:
        if not i == ' ':
            cipher_text += MORSE_CODE_DATA[i] + ' '
        else:
            cipher_text += ' '

    return cipher_text


def decrypt_to_text(msg):
    plain_text = ''
    msg = re.sub(r'  +', ' S ', msg)
    encrypted_text = re.split(r' +', msg)
    for i in encrypted_text:
        if i == 'S':
            plain_text += ' '
            continue
        for idx, val in MORSE_CODE_DATA.items():
            if val == i:
                plain_text += idx
    
    return plain_text

def is_morse_code(msg):
    if re.fullmatch(r'[ \-\.]+', msg) == None:
        return False
    return True

def main():
    message = input('Type message to encrypt or decrypt:\n')
    # Check if message is already encrypted
    if is_morse_code(message):
        # Decrypt message
        print(decrypt_to_text(message.upper()))
    else:
        # Encrypt message
        print(encrypt_to_morse(message.upper()))

if __name__ == '__main__':
    main()
