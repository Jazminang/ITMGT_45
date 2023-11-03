def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def shift_letter(letter, shift):
    if letter.isalpha() and letter.isupper():
        letter_code = ord(letter)
        shifted_code = (letter_code - ord('A') + shift) % 26 + ord('A')
        shifted_letter = chr(shifted_code)
        return shifted_letter
    elif letter == " ":
        return " "
    else:
        return letter

def caesar_cipher(message, shift):
    shifted_message = ""
    for char in message:
        shifted_char = shift_letter(char, shift)
        shifted_message += shifted_char
    return shifted_message

# Example
message = input("Type message in all caps:")
shift = 3
ciphered_message = caesar_cipher(message, shift)
print(ciphered_message)
