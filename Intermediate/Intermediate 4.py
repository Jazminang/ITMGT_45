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
print(ciphered_message)  # Output: "K A"
