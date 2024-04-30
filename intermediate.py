def shift_letter(letter, shift):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.upper()
    
    if letter == " ":
        return " "
    else:
        letter_number = all_letters.index(letter)
        adjusted_shift = letter_number + shift
        answer = all_letters[adjusted_shift % 26]
        return answer

def caesar_cipher(message, shift):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codemessage = ""
    
    for letter in message:
        
        if letter == " ":
            codeletter = " "
            codemessage += codeletter
        else:
            letter = letter.upper()
            letter_number = all_letters.index(letter)
            letter_number = all_letters.index(letter)
            adjusted_shift = letter_number + shift
            codeletter = all_letters[adjusted_shift % 26]
            codemessage += codeletter

    return codemessage

def shift_by_letter(letter, letter_shift):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    letter_shift_number = all_letters.index(letter_shift)
    
    if letter == " ":
        return " "
    else:
        letter_number = all_letters.index(letter)
        adjusted_shift = letter_number + letter_shift_number
        answer = all_letters[adjusted_shift % 26]
        return answer

def vigenere_cipher(message, key):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    codemessage = ""
    message = message.upper()
    key = key.upper()
    
    key = key * (len(message) // len(key) + 1)
    key = key[:len(message)]

    for letter, key_letter in zip(message, key):
        if letter == " ":
            codeletter = " "
        else:
            key_letter_number = all_letters.index(key_letter)
            adjusted_shift = (all_letters.index(letter) + key_letter_number)
            codeletter = all_letters[adjusted_shift % 26]
        codemessage += codeletter
    return codemessage

def scytale_cipher(message, shift):
    if len(message) % shift != 0:
        message += '_' * (shift - len(message) % shift)
        
    encoded_message = ""
    
    for i in range(len(message)):
        adjusted = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[adjusted]

    return encoded_message

def scytale_decipher(message, shift):
    if len(message) % shift != 0:
        message += '_' * (shift - len(message) % shift)
        
    decoded_message = ""
    
    for i in range(len(message)):
        inverse = (i // (len(message) // shift)) + (i % (len(message) // shift)) * shift
        decoded_message += message[inverse]

    return decoded_message
