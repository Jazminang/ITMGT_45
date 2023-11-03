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