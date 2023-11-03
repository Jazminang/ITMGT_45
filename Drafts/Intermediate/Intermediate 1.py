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
