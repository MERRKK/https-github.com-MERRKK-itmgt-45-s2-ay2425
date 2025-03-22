'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

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
    if letter == " ":
        return " "
    
    #Formula Declaration
    current_position = ord(letter) - ord('A') # order of the letter converts Unicode input into integer values
    updated_position = (current_position + shift) % 26 # ensures the cycle of the alphabet is upheld
    updated_character = chr(updated_position + ord('A'))

    return updated_character

#Sample output print(shift_letter("A",5))

def caesar_cipher(message, shift):
    '''Caesar Cipher.

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
    result = ""
    #Find position of letter and add shift later
    for char in message:
        if char.isalpha(): 
            #Formula Input -> 26 ensures that a cycle of the alphabet occurs
            moved_character = chr((ord(char) - ord ('A') + shift) % 26 + ord('A'))
            result += moved_character
        else:
            #If a space is inputted, display the character input instead 
            result += char 

    return result

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

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
    if letter == " ":
        return " "
    
    #Conversion of Shifted Letter to a Unicode Number
    shifted_value = ord(letter_shift) - ord('A')

    #Convert Input Letter to a Unicode Number
    letter_value = ord(letter) - ord ('A')

    #Calculations after shifting from the alphabet cycle
    updated_letter_value = (letter_value + shifted_value) % 26

    #Conversion back to a letter 
    updated_letter = chr(updated_letter_value + ord('A'))

    return updated_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

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
    pass
    extended_key = (key * ((len(message) + len(key) - 1) // len(key)))[:len(message)]
    encrypted = []

    for single_char, shifted_single_char in zip(message, extended_key):
        #if there is a space, append to encrypt w/o any modifications
        if single_char == ' ':
            encrypted.append(' ')
        else:
        #calculate shift if a character is provided
            shift = ord(shifted_single_char) - ord('A')
            encrypted_char = chr((ord(single_char) - ord('A') + shift) % 26 + ord('A'))
            encrypted.append(encrypted_char)

    return ''.join(encrypted)

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #calculate message length number 
    message_length = len(message)
    
    # Check if the length of the message is a multiple of the shift
    if message_length % shift != 0:
        #if the inputted letter is not enough, add underscores at the end of the message until it becomes
        ## a multiple of the shift        
        message += "_" * (shift - (message_length % shift))
    
    encoded_message = ""
    
    for i in range(len(message)):
        # Calculate the index of the character in the raw message
        raw_index = (i // shift) + (len(message) // shift) * (i % shift)
        
        encoded_message += message[raw_index]
    
    return encoded_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

     # Calculate the number of rows after shift
    rows = shift
    
    # Number of columns based on shifts and length of msg
    cols = len(message) // rows
    
    # Condition: +1 column if there are remaining characters left 
    if len(message) % rows != 0:
        cols += 1
    
    # Make empty grid with the calculated number of rows and columns above
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    
    # Message inputs must fill all the grids
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(message):
                grid[row][col] = message[index]
                index += 1
    
    # print / read the grid row by row to get the deciphered message
    deciphered_message = ''.join(''.join(row) for row in grid)
    
    return deciphered_message