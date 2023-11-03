'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def shift_letter(letter, shift):
    if letter.isalpha() and letter.isupper():
        # Get the ASCII code of the letter
        letter_code = ord(letter)
        # Calculate the shifted letter code
        shifted_code = (letter_code - ord('A') + shift) % 26 + ord('A')
        # Convert the shifted code back to a letter
        shifted_letter = chr(shifted_code)
        return shifted_letter
    elif letter == " ":
        return " "
    else:
        # Handle invalid input by returning the original character
        return letter

# Examples
print(shift_letter("A", 0)) 
print(shift_letter("A", 2)) 
print(shift_letter("Z", 1))  
print(shift_letter("X", 5)) 
print(shift_letter(" ", 3))  


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



def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    
    if letter.isalpha() and letter.isupper() and letter_shift.isalpha() and letter_shift.isupper():
        # Calculate the numerical equivalent of the shift letter
        shift_value = ord(letter_shift) - ord('A')
        # Get the ASCII code of the input letter
        letter_code = ord(letter)
        # Calculate the shifted letter code
        shifted_code = (letter_code - ord('A') + shift_value) % 26 + ord('A')
        # Convert the shifted code back to a letter
        shifted_letter = chr(shifted_code)
        return shifted_letter
    else:
        # Handle invalid input by returning the original character
        return letter

# Examples
print(shift_by_letter("A", "A"))  
print(shift_by_letter("A", "C"))  
print(shift_by_letter("B", "K"))  
print(shift_by_letter(" ", "K")) 

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.


def vigenere_cipher(message, key):
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Extend the key to match the length of the message
    extended_key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    
    encrypted_message = ""
    for i in range(len(message)):
        shift_value = ord(extended_key[i]) - ord('A')
        shifted_letter = shift_letter(message[i], shift_value)
        encrypted_message += shifted_letter
    
    # Reinsert spaces in the original positions
    j = 0
    final_message = ""
    for i in range(len(message)):
        if message[i] == " ":
            final_message += " "
        else:
            final_message += encrypted_message[j]
            j += 1
    
    return final_message


# Example
message =  input("Type message in all caps:")
key = "KEY"
ciphered_message = vigenere_cipher(message, key)
print(ciphered_message)  
